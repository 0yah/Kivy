from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class ClearApp(App):
    def build(self):
        self.box = BoxLayout(orientation='horizontal',spacing=20)
        self.txt = TextInput(hint_text="Write Here",size_hint=(.5,.1))
        self.btn = Button(text="Clear All",on_press=self.clearText,size_hint=(.1,.1))
        #Add Widgets to the layout
        self.box.add_widget(self.txt)
        self.box.add_widget(self.btn)
        return self.box

    def clearText(self,instance):
        self.txt.text = ""

ClearApp().run()