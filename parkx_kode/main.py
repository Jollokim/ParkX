from kivy.app import App
from kivy.config import Config

from parkx_kode.controller.ParkingController import ParkingController
from parkx_kode.repository.ListRepository import ListRepository
from parkx_kode.view.gui import Gui


class MyApp(App):
    title = "ParkX"
    icon = ""

    def build(self):
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '800')

        gui = Gui()

        controller = ParkingController(gui, ListRepository())

        gui.controller = controller

        return gui


if __name__ == '__main__':
    MyApp().run()
