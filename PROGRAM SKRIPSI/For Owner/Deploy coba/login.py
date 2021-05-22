from kivy.lang.builder import Builder
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.theming import ThemeManager
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem, \
    ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget,ImageLeftWidget
from kivy.core.window import Window
import mysql.connector

class loginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        Window.size = (300, 500)
        return Builder.load_file("login.kv")

    def logger(self):
        un = self.root.ids.user.text
        pw = self.root.ids.password.text
        con = mysql.connector.connect(db="u4026527_dbkepin", host="156.67.215.51", user="u4026527_dbkepin",
                                      passwd="Animals1",
                                      port=3306)
        cur = con.cursor()
        query = "INSERT INTO Username(Username,Password) VALUES (%s,%s)"
        val = (un, pw)
        try:
            cur.execute(query, val)
            con.commit()
            con.close()
            print("udah bener sayang")
            print("id nya adalah" + " " + un)
            print("password adalah " + pw)
        except:
            print("ada yg salah")

    def tutupdialog(self, obj):
        self.dialog.dismiss()
    def listitem(self, obj):
        self.dialog.dismiss()
    def clear(self):
        self.root.ids.welcome_label.text = 'Welcome'
        self.root.ids.user.text = ''
        self.root.ids.password.text = ''
    def list_barang(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)
        for i in range(30):
            item = ThreeLineAvatarListItem(text="Barang ke - " + str(i), secondary_text="Harga",
                                         tertiary_text="tanggal sampai")
            list_view.add_widget(item)

        screen.add_widget(scroll)
        return screen

if __name__ == "__main__":
    loginApp().run()
