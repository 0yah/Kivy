from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button


class MyClock(App):
    i=0

    def build(self):
        self.mybtn = Button(text="Number of calls")
        Clock.schedule_interval(self.Clock_Callback,2)
        return self.mybtn

    def Clock_Callback(self,dt):
        self.i = self.i + 1
        self.mybtn.text = "Call = %d"%self.i

MyClock().run()