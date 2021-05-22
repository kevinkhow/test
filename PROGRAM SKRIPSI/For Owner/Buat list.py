from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton, MDFloatingActionButtonSpeedDial, MDIconButton, \
    MDFloatingActionButton, MDCustomRoundIconButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem, \
    ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget,ImageLeftWidget
from kivymd.uix.list import IconRightWidget
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.size= (300,500)

# UNTUK LIST YANG SESUAI KEINGINAN
# class list(MDApp):
#     def build(self):
#         screen = Screen()
#         scroll = ScrollView()
#
#
#         list_view = MDList()
#         scroll.add_widget(list_view)
#
#         item1= OneLineListItem(text='Pemasukan')
#         item2 = OneLineListItem(text='Pengeluaran')
#         item3 = OneLineListItem(text='Grafik')
#
#         list_view.add_widget(item1)
#         list_view.add_widget(item2)
#         list_view.add_widget(item3)
#         screen.add_widget(scroll)
#
#         return screen
#
# list().run()


# # List banyak sesuai N (one list item<< ubah di from)
# class list(MDApp):
#     def build(self):
#         screen = Screen()
#         scroll = ScrollView()
#
#
#         list_view = MDList()
#         scroll.add_widget(list_view)
#
#         for i in range (30):
#             item = OneLineListItem(text="Barang ke - "+ str(i))
#
#
#
#
#             list_view.add_widget(item)
#
#         screen.add_widget(scroll)
#
#         return screen
#
# list().run()


# List banyak sesuai N (two list item<< ubah di from)
# class list(MDApp):
#     def build(self):
#         screen = Screen()
#         scroll = ScrollView()
#
#
#         list_view = MDList()
#         scroll.add_widget(list_view)
#
#         for i in range (30):
#             item = TwoLineListItem(text="Barang ke - "+ str(i),secondary_text="Harga")
#
#
#
#
#             list_view.add_widget(item)
#
#         screen.add_widget(scroll)
#
#         return screen
#
# list().run()

# List banyak sesuai N (three list item<< ubah di from + gambar, kalau mau jadi icon tinggal ganti yg avatar jadi icon)
class list(MDApp):
    def build(self):
        screen = Screen()
        scroll = ScrollView()

        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(30):
            image = ImageLeftWidget(source="Win iPhone X.ico")

            item = ThreeLineAvatarListItem(text="Barang ke - " + str(i), secondary_text="Harga",
                                         tertiary_text="tanggal sampai")
            item.add_widget(image)
            list_view.add_widget(item)

        screen.add_widget(scroll)

        return screen


list().run()
