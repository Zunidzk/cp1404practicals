from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Label"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        names = ['John', 'Mary', 'David', 'Emma']
        for name in names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
