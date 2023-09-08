import asyncio
import json
import os
import pkg_resources
import subprocess
import sys
import traceback

# Discord.py setup
import discord
from discord.ext import commands
from discord.ext.commands import ExtensionFailed, ExtensionNotFound, NoEntryPointError
from dotenv import load_dotenv
load_dotenv()
intents = discord.Intents.default()
cogs_to_load = json.loads(str(os.getenv("cogs_to_load", "")))
bot_prefix = f'<@{os.getenv("dpy_user_id", "")}> '

# Bot setup
intents.message_content = False
embed_colour = None


class Bot(commands.Bot):
    debug: bool
    bot_app_info: discord.AppInfo

    def __init__(self) -> None:
        super().__init__(command_prefix=bot_prefix, case_insensitive=True, intents=intents)

    async def on_ready(self) -> None:
        print(f"\nLogged in as {self.user}")
        print(f"\nCogs to load: {cogs_to_load}")
        await self.load_cogs(cogs_to_load)

    async def get_embed_colour(self, *args):
        return embed_colour
    async def get_embed_color(self, *args):
        return await self.get_embed_colour(self)

    async def get_shared_api_tokens(self, service):
        identifier = str(service)+"_api_key"
        api_key = os.getenv(str(identifier), None)
        if api_key not in [None, "", "None"]:
            return {
                "api_key": api_key
            }
        else:
            return {}

    async def load_cogs(self, cogs_to_load) -> None:
        loaded_cogs = []
        for ext in cogs_to_load:
            print("\n> Importing", ext)
            DpyUtils.fetch_and_install_requirements(ext)
            try:
                await self.load_extension(ext)
                loaded_cogs.append(str(ext))
                print("> Loaded", str(ext))
            except (
                ExtensionNotFound,
                NoEntryPointError,
                ExtensionFailed,
            ):
                print(f"Failed to load extension {ext}.", file=sys.stderr)
                traceback.print_exc()
        print("\nBot ready!", len(loaded_cogs), "loaded cogs:", loaded_cogs)

    async def start(self, debug: bool = False) -> None:
        self.debug = debug
        return await super().start(os.getenv("dpy_token"), reconnect=True)


class DpyUtils():
    def fetch_and_install_requirements(cog_entry):
        cog_name = str(cog_entry).replace('cogs.', '')
        cog_info_json_path = f"cogs/{cog_name}/info.json"
        with open(cog_info_json_path) as f:
            data = json.load(f)
            requirements = data.get('requirements', [])
            print("> Requirements:", requirements)
            for requirement in requirements:
                try:
                    if not DpyUtils.is_package_installed(requirement):
                        DpyUtils.install(requirement)
                except Exception as err:
                    return print(err)

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    def is_package_installed(package):
        try:
            pkg_resources.get_distribution(package)
            return True
        except pkg_resources.DistributionNotFound:
            return False


def run_bot() -> None:
    bot = Bot()
    asyncio.run(bot.start())

if __name__ == "__main__":
    run_bot()
