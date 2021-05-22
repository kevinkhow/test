from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from functools import partial

import mysql.connector


class MyApp(App):
    sm = ScreenManager()

    def com1(self, instance, *args):
        label1 = Label(text="Hi")
        return label1

    def com2(self, instance, *args):
        label = Label(text="Bye")

    def build(self):
        button1 = Button(text="Hi", size_hint=(0.25, 0.18), pos=(200, 100))
        button1.bind(on_press=partial(self.com1, button1))
        button2 = Button(text="Bye", size_hint=(0.25, 0.18), pos=(350, 200))
        button2.bind(on_press=partial(self.com2, button2))
        boxlayout = BoxLayout()
        boxlayout.add_widget(button1)
        boxlayout.add_widget(button2)
        return boxlayout


if __name__ == "__main__":
    MyApp().run()
