import kivy
import datetime

from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder 
from kivy.properties import StringProperty
from datetime import date
from kivy.uix.behaviors import FakeRectangularElevationBehavior
from kivy.core import Window

Window.size = (350, 600)

class ToDoApp(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file())

if __name__ == "__main__":
    ToDoApp().run()