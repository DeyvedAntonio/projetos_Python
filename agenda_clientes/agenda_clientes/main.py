from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from sqlalchemy import (create_engine, MetaData, Column,
                        Table, Integer, String, DateTime)


Window.size = 800, 500
Window.clearcolor = (233/255, 233/255, 233/255, 1)


class Main(App):
    def build(self):
        return Gerenciador_telas()


class Gerenciador_telas(ScreenManager):
    pass


class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def verificar_status(self):
        app = App.get_running_app()
        app.root.current = 'tela_home'


class Home(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


Main().run()
