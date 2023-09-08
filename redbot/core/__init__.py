import importlib
import sys

class Config():
    def get_conf(self, identifier):
        config = {}
        config[self.__class__.__name__] = { str(identifier): {} }
        return config

# Define a custom import hook
class RedbotImportHook:
    def find_spec(self, fullname, path, target=None):
        if fullname == 'redbot.core.app_commands':
            return importlib.util.find_spec('discord.app_commands')
        if fullname == 'redbot.core.checks':
            return importlib.util.find_spec('discord.ext.commands')
        if fullname == 'redbot.core.commands':
            return importlib.util.find_spec('discord.ext.commands')
        return None

# Create an instance of the import hook
redbot_import_hook = RedbotImportHook()

# Register the import hook
sys.meta_path.insert(0, redbot_import_hook)
