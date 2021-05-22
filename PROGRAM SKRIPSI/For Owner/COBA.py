from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem


from HELPERLogin import username_helper


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        label = MDLabel(text="Hello world", halign="center", theme_text_color="Custom",
                        text_color=(236 / 255.0, 98 / 255.0, 81 / 255.0, 1),
                        font_style="H1")
        # halign = horizontal align
        screen = Screen()   
        a = MDRectangleFlatButton(text="Pencet",
                                  pos_hint={'center_x': 0.5, 'center_y': 0.4}, on_release=self.show_data)

        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(a)
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            check_string ="Username gabole kosong"

        else:
            check_string =self.username.text + " "+ "(Benar Sudah Terdaftar)"

        buttontutup = MDRectangleFlatButton(text='Tutup',on_release = self.tutupdialog)
        buttonpertanyaan = MDRectangleFlatButton(text='Pertanyaan??',on_release = self.listitem)

        self.dialog = MDDialog(title='Hallo', text=check_string, size_hint=(0.7, 1),
                          buttons=[buttonpertanyaan, buttontutup])

        self.dialog.open()


    def tutupdialog(self,obj):
        self.dialog.dismiss()

    def listitem(self,obj):

        screen= Screen()
        item1 = OneLineListItem(text='Item 1')
        item2 = OneLineListItem(text='Item 2')
        screen.add_widget(item1)
        screen.add_widget(item2)
        return screen


DemoApp().run()
