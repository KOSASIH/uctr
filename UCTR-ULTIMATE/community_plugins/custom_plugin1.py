# community_plugins/custom_plugin1.py
from plugin_architecture.plugin_manager import Plugin

class CustomPlugin1(Plugin):
    def __init__(self):
        super().__init__("Custom Plugin 1", "This is a custom plugin 1")

    def activate(self):
        print("Activating Custom Plugin 1")

    def deactivate(self):
        print("Deactivating Custom Plugin 1")

    def do_something(self):
        print("Doing something with Custom Plugin 1")
