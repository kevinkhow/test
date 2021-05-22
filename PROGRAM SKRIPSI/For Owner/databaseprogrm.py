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

        self.mauubahapa = TextInput(text="apa yang mau diubah")
        self.jadiapa = TextInput(text="jadiapa")


        submit = Button(text="submit", on_press= self.submit) #on press tu ketika ditekan
        delete = Button(text="delete database", on_press=self.delete)
        update = Button(text="update database",on_press=self.update)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.mauubahapa)
        layout.add_widget(self.jadiapa)
        layout.add_widget(submit)
        layout.add_widget(update)
        layout.add_widget(delete)

        return layout

    def update(self,obj):
        un = self.mauubahapa.text
        pw = self.jadiapa.text
        con = mysql.connector.connect(db="u4026527_dbkepin", host="156.67.215.51", user="u4026527_dbkepin",
                                      passwd="Animals1",
                                      port=3306)
        cur = con.cursor()
        query = "UPDATE Username SET Username=%s WHERE Username=%s"  #PATTERNNYA SET TUH MENJADI APA WHERE ITU APA YG MAU DIUBAH

        val = (pw,un) #patternnya MENJADI APA ,  APA YG DIUBAH
        try:
            cur.execute(query,val)
            con.commit()
            con.close()
            print("udah bener")
        except:
            print("ada yg salah")


    def submit(self,obj):
        un=self.username.text
        pw=self.password.text
        con = mysql.connector.connect(db="u4026527_dbkepin", host="156.67.215.51", user="u4026527_dbkepin", passwd="Animals1",
                               port=3306)
        cur = con.cursor()
        query="INSERT INTO Username(Username,Password) VALUES (%s,%s)"
        val= (un,pw)
        try:
            cur.execute(query,val)
            con.commit()
            con.close()
            print("udah benersayanag")  
            print("id nya adalah" + " " +un)
            print("password adalah " + pw)
        except:
            print("ada yg salah")

    def delete(self,obj):
        un=self.username.text
        pw=self.password.text
        con = mysql.connector.connect(db="u4026527_dbkepin", host="156.67.215.51", user="u4026527_dbkepin", passwd="Animals1",
                               port=3306)
        cur = con.cursor()
        query="DELETE FROM Username WHERE Username =%s AND Password = %s" #HARUS PAKE AND KEKNYA
        val= (un,pw)
        try:
            cur.execute(query,val)
            con.commit()
            con.close()
            print("udah benersayanag")

            print("password adalah " + pw)
        except:
            print("ada yg salah")
if __name__=="__main__":
    MyApp().run()



