from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class NameList(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.make_boxes()
        return self.root

    def make_boxes(self):
        names = ['Alice', 'Bob', 'Charlie', 'David']
        for name in names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

NameList().run()
