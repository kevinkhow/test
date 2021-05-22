from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

# Objek list ditentukan
# list_helper = """
# Screen:
#     ScrollView:
#         MDList:
#             OneLineListItem:
#                 text:"item1"
#             OneLineListItem:
#                 text:"item2" 
#
#
# """

list_helper = """
Screen:
    ScrollView:
        MDList:
            id:container

"""


class List(MDApp):
    def build(self):
        screen = Builder.load_string(list_helper)

        return screen

    def on_start(self):
        for i in range (20):
            item = OneLineListItem(text="Item"+ str(i))
            self.root.ids.container.add_widget(item)  #<< itu mengarah ke id = container


List().run()