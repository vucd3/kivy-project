import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    acc = ObjectProperty(None)
    passw = ObjectProperty(None)
    '''
    def check(self):
        if self.acc.text == "Mai Xuan Vu" and self.passw.text == "maixuanvu123":
            print("Sign In Succesfully!")
            self.acc.text = ""
            self.passw.text = ""
        else:
            print("Sign In Failed!")
            self.acc.text = ""
            self.passw.text = ""
    '''
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()