from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import OneLineListItem
from kivy.core.window import Window

class Main(MDApp):

    def build(self):
        Window.size = (360, 640)
        return Builder.load_file('multiscreen.kv')

    def add_to_list(self):
        item = OneLineListItem(
                    text="new item"
                )
        self.root.ids.lst.add_widget(item)

if __name__ == '__main__':
    Main().run()
