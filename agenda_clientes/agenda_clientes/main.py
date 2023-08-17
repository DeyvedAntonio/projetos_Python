from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Main(App):
    def build(self):
        return Login()
    

class Login(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


Main().run()
