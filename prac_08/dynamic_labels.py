from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class DynamicLabelsApp(App):
    names = ['Eren', 'Mikasa', 'Armin', 'Erwin', 'Levi']

    def build(self):
        layout = BoxLayout(orientation='vertical')
        for name in self.names:
            label = Label(text=name)
            layout.add_widget(label)
        return layout


if __name__ == '__main__':
    DynamicLabelsApp().run()
