# community_plugins/custom_plugin2.py
from plugin_architecture.plugin_manager import Plugin

class CustomPlugin2(Plugin):
    def __init__(self):
        super().__init__("Custom Plugin 2", "This is a custom plugin 2")

    def activate(self):
        print("Activating Custom Plugin 2")

    def deactivate(self):
        print("Deactivating Custom Plugin 2")

    def do_something_else(self):
        print("Doing something else with Custom Plugin 2")
