import importlib
import os
import logging

class PluginManager:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def discover_plugins(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py"):
                plugin_name = filename[:-3]
                self.plugins[plugin_name] = importlib.import_module(plugin_name)

    def load_plugin(self, plugin_name):
        if plugin_name in self.plugins:
            return self.plugins[plugin_name]
        else:
            logging.error(f"Plugin {plugin_name} not found")
            return None

    def unload_plugin(self, plugin_name):
        if plugin_name in self.plugins:
            del self.plugins[plugin_name]

    def get_plugins(self):
        return list(self.plugins.keys())

class Plugin:
    def __init__(self, name, description, version):
        self.name = name
        self.description = description
        self.version = version

    def activate(self):
        logging.info(f"Activating plugin {self.name}")
        # Perform plugin activation logic here

    def deactivate(self):
        logging.info(f"Deactivating plugin {self.name}")
        # Perform plugin deactivation logic here

# Example plugin
class MyPlugin(Plugin):
    def __init__(self):
        super().__init__("MyPlugin", "This is my plugin", "1.0")

    def activate(self):
        super().activate()
        # Perform custom activation logic here

    def deactivate(self):
        super().deactivate()
        # Perform custom deactivation logic here

# Create a plugin manager instance
plugin_manager = PluginManager("plugins")

# Discover plugins
plugin_manager.discover_plugins()

# Load a plugin
my_plugin = plugin_manager.load_plugin("my_plugin")

# Activate the plugin
if my_plugin:
    my_plugin.activate()

# Get all plugins
plugins = plugin_manager.get_plugins()
print(plugins)

# Unload a plugin
plugin_manager.unload_plugin("my_plugin")
