from kivy.app import App
from kivy.config import Config

from view.gui import Gui


class MyApp(App):
    title = "ParkX"
    icon = ""

    def build(self):
        Config.set('graphics', 'width', '700')
        Config.set('graphics', 'height', '700')

        gui = Gui()

        return gui


if __name__ == '__main__':
    MyApp().run()
