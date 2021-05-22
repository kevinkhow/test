from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import os

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="TEST"))
        self.mybox = BoxLayout(orientation='vertical')
        self.button1 = Button(text="Load")
        self.button2 = Button(text="Cancel")
        self.save = Button(text="Save")
        self.mybox.add_widget(self.button1)
        self.mybox.add_widget(self.button2)
        self.mybox.add_widget(self.save)
        self.add_widget(self.mybox)



class Epicapp(App):

    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager



if __name__ == "__main__":
    chat_app = Epicapp()
    chat_app.run()