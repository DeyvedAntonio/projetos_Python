from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = 500, 400
Window.clearcolor = (233/255, 255/255, 216/255, 1)


class Home(BoxLayout):
    def digito(self, num):
        self.ids.entrada.text += str(num)


class Calculadora(App):
    def build(self):
        return Home()


if __name__ == '__main__':
    Calculadora().run()