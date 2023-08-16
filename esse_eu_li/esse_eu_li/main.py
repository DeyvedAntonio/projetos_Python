from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import sqlite3

Window.size = (600, 500)
Window.clearcolor = (233/255, 225/255, 216/255, 1)

class Home(BoxLayout):
    pass


class Main(App):
    def build(self):
        return Home()
    

Main().run()