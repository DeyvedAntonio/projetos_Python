from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class Main(App):
    def build(self):
        return Gerenciador_telas()


class Gerenciador_telas(ScreenManager):
    pass


class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


Main().run()
