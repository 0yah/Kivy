from kivy.app import App
from kivy.uix.label import Label

#Definition of a class that inherits from the App class
class MyInterface(App):

    def build(self):
        return Label(text="My interface")


MyInterface().run()