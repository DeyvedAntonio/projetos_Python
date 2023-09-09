from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from sqlalchemy import (create_engine, MetaData, Column,
                        Table, Integer, String, DateTime)


engine = create_engine('sqlite:///infra/agenda_clientes.db',
                       echo=True)

metadata = MetaData(engine)

class Main(App):
    def build(self):
        return Gerenciador_telas()


class Gerenciador_telas(ScreenManager):
    pass


class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


Main().run()
