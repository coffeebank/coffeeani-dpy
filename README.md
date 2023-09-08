# coffee-dpy ☕

## 📦 A drop-in Discord.py wrapper for Red-DiscordBot cogs.

Coffee-dpy lets you run cogs built for [Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot/) independently with only [Discord.py](https://github.com/Rapptz/discord.py).

This wrapper aims to be a simple, lightweight, and portable way to package and redistribute Red cogs easily for use, with minimal changes to Red cogs when possible.

Discord intents are not required by default.


## Alpha Release

This project is still in alpha stage development, and may not work with all cogs. Contributions are welcome.


## Usage

### Step 1: Add your cogs

Clone this project. Then, create a new `cogs` folder and place your Red cogs inside.

### Step 2: Add your Discord Bot info

Make an `.env` file, and:
- Add your bot's token to `dpy_token`
- Add your bot's User ID to `dpy_user_id`

The bot prefix is @ping or Slash command.

### Step 3: Run the Bot

Setup a [venv](https://docs.python.org/3/library/venv.html) using Python >=3.9 and install requirements

```
python3.9 -m venv ~/dpyenv
source ~/dpyenv/bin/activate
pip install -r requirements.txt
```

In the future, you can run your bot anytime using
```
source ~/dpyenv/bin/activate
python3 -m main
```
