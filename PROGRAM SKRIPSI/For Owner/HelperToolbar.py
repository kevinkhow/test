from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size= (300,500)

screen_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout
                    orientation : 'vertical'
                    MDToolbar:
                        title:"Pembukuan Otomatis"
                        left_action_items:[["menu",lambda x : nav_drawer.toggle_nav_drawer()]] #<<icon #hiraukan lambda
                        right_action_items:[["clock",lambda x : app.navigation_draw()]] #<<icon
                        elevation:12
                    MDLabel:
                        text: "konten dsni "
                        halign: "center"
                  
                    MDBottomAppBar:
                        MDToolbar:
                            title:"help?"
                            left_action_items:[["account-star",lambda x : app.navigation_draw()]] #<<icon #hiraukan lambda
                            mode:'end' #posisi android (free-end, end)
                            type:"bottom"
                            icon : 'language-python' 
                            #on_action_button : app.navigation_draw() itu untuk kalau simbolnya diteken akan trigger
                            elevation:12
        MDNavigationDrawer:
            id:nav_drawer
            BoxLayout:
                orientation:'vertical'
                spacing : '8dp'
                padding : '8dp' #spasi di image sama label
                
                Image:
                    source:'acai.jpg'
                MDLabel:
                    text:"  kevin"
                    fontstyle:"Subtitle1"
                    size_hint_y:None
                    height:self.texture_size[1]
                    
                MDLabel:
                    text:"  abcd @gmail.com"
                    fontstyle:"Caption"
                    size_hint_y:None
                    height:self.texture_size[1]
                
                ScrollView:   #buattampilan jadi keatas smua
                    MDList:
                        OneLineIconListItem:
                            text:"Panduan"
                            IconLeftWidget:
                                icon: 'account-supervisor-circle'
                        OneLineIconListItem:
                            text:"Back"
                            IconLeftWidget:
                                icon: 'arrange-send-to-back'
                        OneLineIconListItem:
                            text:"Log Out"
                            IconLeftWidget:
                                icon: 'logout-variant'
"""

class toolbar(MDApp):
    def build(self):
        self.theme_cls.primary_palette ="Red" #<<UBAH TITLE BAR NYA
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print ("adjaiwdjaiwodjoi")



toolbar().run()