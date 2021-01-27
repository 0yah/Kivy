from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder

Builder.load_string("""
<MyRecycleView>:
    viewclass: 'Button'
    RecycleBoxLayout:    
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
""")

class MyRecycleView(RecycleView):

    def __init__(self, **kwargs):

        super(MyRecycleView, self).__init__(**kwargs)

        self.data = [{'text': str(x)} for x in range(20)]

class RecycleApp(App):

    def build(self):

        return MyRecycleView()

RecycleApp().run()