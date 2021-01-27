from functools import partial
from kivy.app import App
from kivy.uix.button import Button



class MyButtonInterface(App):
    def disable(self, instance, *args):
        instance.disabled = True

    def update(self,instance,*args):
        instance.text = "I am disabled!"

    def build(self):
        disabledButton = Button(text="My Button interface", background_color=(155, 0, 23, 12),pos=(300,350),size_hint=(.25,.18))
        disabledButton.bind(on_press=partial(self.disable,disabledButton))
        disabledButton.bind(on_press=partial(self.update,disabledButton))
        return disabledButton

MyButtonInterface().run()
