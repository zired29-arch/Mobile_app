from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput

class My(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(FirstScreen(name = 'FirstScreen'))
        screen_manager.add_widget(SecondScreen(name = 'SecondScreen'))
        return screen_manager


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = 'vertical')
        name_input = TextInput()
        next_screen_button = Button(text = 'Дальше', size_hint = (0.5, 0.3), pos_hint = {'center_x': 0.5})
        next_screen_button.on_press = self.set_second_screen
        label = Label(text = 'Надпись')
        main_layout.add_widget(label)
        main_layout.add_widget(next_screen_button)
        self.add_widget(main_layout)
    
    def set_second_screen(self):
        self.manager.current = 'SecondScreen'



class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = 'vertical')
        button = Button(text = 'Нажми!')
        label = Label(text = 'Надпись')
        button.on_press = self.set_first_screen
        main_layout.add_widget(label)
        main_layout.add_widget(button)
        self.add_widget(main_layout)
    
    def set_first_screen(self):
        self.manager.current = 'FirstScreen'

app = My()
app.run()