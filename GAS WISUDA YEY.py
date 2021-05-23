from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineListItem
from kivy.lang.builder import Builder
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.uix.button import Button
from kivymd.uix.button import MDRoundFlatButton,MDRectangleFlatButton,MDFlatButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextField
from kivymd.theming import ThemeManager
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem, \
    ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivy.core.window import Window

import mysql.connector


#cari cara untuk size_texture biar GUI jadi gampang

class Screen1(Screen):

    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        layout = MDCard(size_hint=(None, None), size=(300, 500), pos_hint={"center_x": 0.5, "center_y": 0.5},
                        elevation=10, padding=25, spacing=25, orientation='vertical')
        label = MDLabel(text="Welcome",
                font_style="H4",
                halign="center",
                size_hint_y=None,
                padding_y=15,height=150)
        textfield= MDTextField(hint_text= "Username",
        helper_text = "Username Gabole Kosong",
        helper_text_mode= "on_focus",
        icon_right= "account",
        size_hint_x= None,
        width= 200,
        font_size= 18,
        pos_hint= {"center_x": 0.5},height=600)
        textfieldd= MDTextField(
                hint_text="Password",
                icon_right="eye-off",
                helper_text="Password Gabole Kosong",
                helper_text_mode="on_focus",
                size_hint_x=None,
                width=200,
                font_size=18,
                pos_hint={"center_x":0.5},
                password=True)
        buttonlogin= MDRectangleFlatButton(text="Login",
                font_size=12,pos_hint={'center_x':0.5})
        buttondaftar = MDRectangleFlatButton(text="Daftar",
                                       font_size=12, pos_hint={'center_x': 0.5})
#
        layout.add_widget(label)
        layout.add_widget(textfield)
        layout.add_widget(textfieldd)
        layout.add_widget(buttonlogin)
        layout.add_widget(buttondaftar)
        self.add_widget(layout)



        # if self.textfield.text =='':
        #     peringatan = "Username gabole Kosong"
        #     self.dialog=MDDialog(title='Hallo', text=peringatan, size_hint=(0.7, 1))
        #     self.dialog.open()
        # else:
        #     un = self.textfield.text
        #     pw = self.textfieldd.text
        #     con = mysql.connector.connect(db="u4026527_dbkepin", host="156.67.215.51", user="u4026527_dbkepin",
        #                                   passwd="Animals1",
        #                                   port=3306)
        #     cur = con.cursor()
        #     query = "SELECT * FROM Username WHERE Username = %s and Password = %s"
        #     val = (un, pw)
        #
        #     try:
        #         cur.execute(query, val)
        #         result = cur.fetchall()
        #         if result:
        #             for i in result:
        #                 self.root.ids.welcome_label.text = "akdioad"
        #         else:
        #             print("salah")
        #
        #         con.commit()
        #         con.close()
        #
        #     except:
        #         print("ada yang salah")



class myapp(MDApp):
    def build(self):

        self.theme_cls.primary_palette = "Red"

        self.theme_cls.theme_style = "Light"
        sm = ScreenManager()
        Window.size = (300, 500)
        sm.add_widget(Screen1(name='s1'))
        return sm


if __name__ == "__main__":
    myapp().run()
