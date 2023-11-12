from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = 500, 400
Window.clearcolor = (233/255, 255/255, 216/255, 1)


class Home(BoxLayout):
    def digito(self, value):
        """
        Inserção dos dígitos no display de entrada.
        
        Args:
            value (int): inserir os números no primeiro display da calculadora
        """
        if len(self.ids.entrada.text) < 8:
            self.ids.entrada.text += str(value)

    def limpar(self):
        """
        Limpeza do display de entrada.
        """
        self.ids.entrada.text = ''

    def limpar_tudo(self):
        """
        Limpeza das das exibições
        :return:
        None
        """
        self.ids.saida.text = ''
        self.limpar()


class Calculadora(App):
    def build(self):
        return Home()


if __name__ == '__main__':
    Calculadora().run()
