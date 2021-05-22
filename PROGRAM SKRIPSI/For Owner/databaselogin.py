from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import mysql.connector


class MyApp(App):
    def build(self):
        layout = GridLayout(cols=1)
        self.username=TextInput(text="masuk ke database username")
        self.password= TextInput(text="masuk ke database username password")
        submit = Button(text="submit", on_press= self.submit) #on press tu ketika ditekan
        delete = Button(text="delete database")
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(submit)
        layout.add_widget(delete)
        return layout



    def submit(self,obj):
        un=self.username.text
        pw=self.password.text
        con = mysql.connector.connect(db="u4026527_dbkepin", host="156.67.215.51", user="u4026527_dbkepin", passwd="Animals1",
                               port=3306)
        cur = con.cursor()
        query="SELECT* from Username(Username,Password) VALUES (%s,%s)"

        val= (un,pw)
        cur.execute(query,val)
        con.commit()
        con.close()
if __name__=="__main__":
    MyApp().run()



