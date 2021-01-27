from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

#Loading widgets from Kv strings
Builder.load_string("""
<ImageButton>:
    Label:
        text: "[u][color=ff0066][b]Welcome[/b][/color] To [i][color=ff9933]Like[/i]Geeks[/color][/u]"
        font_size: '30'
        markup: True
        
    Button:
        text: "Hello Button!"
        size_hint: .12, .12
        Image:
            source: 'ok.png'
            center_x: self.parent.center_x
            center_y: self.parent.center_y

""")

#Widgets can be loaded using 
# Builder.load_file("imagebtn.kv")
# The widget name must be the same name with class

class ImageButton(App,BoxLayout):
    def build(self):
        return self

ImageButton().run()