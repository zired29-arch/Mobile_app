from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import instruction
import ruffier

class My(App):
    def build(self):
        screen_manager = ScreenManager()
        Window.clearcolor = (0.5, 0.5, 0.5, 0.7)
        screen_manager.add_widget(FirstScreen(name = 'FirstScreen'))
        screen_manager.add_widget(SecondScreen(name = 'SecondScreen'))
        screen_manager.add_widget(ThirdScreen(name = 'ThirdScreen'))
        screen_manager.add_widget(FourthScreen(name = 'FourthScreen'))
        screen_manager.add_widget(FifthScreen(name = 'FifthScreen'))
        return screen_manager


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = 'vertical', spacing = '20px', padding = '20px')
        name_input = TextInput(hint_text = 'Введите имя..', size_hint = (0.5, 0.1), pos_hint = {'center_x': 0.5}, multiline = False)
        self.age_input = TextInput(hint_text = 'Введите ваш возраст', size_hint = (0.5, 0.1), pos_hint = {'center_x': 0.5}, multiline = False)
        next_screen_button = Button(text = 'Дальше', size_hint = (0.4, 0.3), pos_hint = {'center_x': 0.5})
        next_screen_button.on_press = self.set_next_screen
        label = Label(text = instruction.txt_instruction, font_size = 17, halign = 'center')
        main_layout.add_widget(label)
        main_layout.add_widget(name_input)
        main_layout.add_widget(self.age_input)
        main_layout.add_widget(next_screen_button)
        self.add_widget(main_layout)
    
    def set_next_screen(self):
        try:
            app.age = int(self.age_input.text)
            self.manager.current = 'SecondScreen'
        except ValueError:
            pass



class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = 'vertical', spacing = '20px', padding = '20px')
        button = Button(text = 'Продолжить', size_hint = (0.4, 0.3), pos_hint = {'center_x': 0.5})
        self.result_input = TextInput(hint_text = 'Введите результат..', size_hint = (0.5, 0.1), pos_hint = {'center_x': 0.5}, multiline = False)
        label = Label(text = instruction.txt_test1, font_size = 23, halign = 'center')
        button.on_press = self.set_next_screen
        main_layout.add_widget(label)
        main_layout.add_widget(self.result_input)
        main_layout.add_widget(button)
        self.add_widget(main_layout)
    
    def set_next_screen(self):
        try:
            app.pulse1 = int(self.result_input.text)
            self.manager.current = 'ThirdScreen'
        except ValueError:
            pass
        

class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = 'vertical', spacing = '20px', padding = '20px')
        button = Button(text = 'Продолжить', size_hint = (0.4, 0.3), pos_hint = {'center_x': 0.5})
        button.on_press = self.set_next_screen
        label = Label(text = instruction.txt_test2, font_size = 18, halign = 'center')
        main_layout.add_widget(label)
        main_layout.add_widget(button)
        self.add_widget(main_layout)
    
    def set_next_screen(self):
        self.manager.current = 'FourthScreen'


class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = 'vertical', spacing = '20px', padding = '20px')
        button = Button(text = 'Продолжить', size_hint = (0.4, 0.3), pos_hint = {'center_x': 0.5})
        self.result_before_input = TextInput(hint_text = 'Введите результат..', size_hint = (0.5, 0.1), pos_hint = {'center_x': 0.5}, multiline = False)
        self.result_after_input = TextInput(hint_text = 'Введите результат после отдыха', size_hint = (0.5, 0.1), pos_hint = {'center_x': 0.5}, multiline = False)
        button.on_press = self.set_next_screen
        label = Label(text = instruction.txt_test3, halign = 'center', font_size = 18)
        main_layout.add_widget(label)
        main_layout.add_widget(self.result_before_input)
        main_layout.add_widget(self.result_after_input)
        main_layout.add_widget(button)
        self.add_widget(main_layout)
    
    def set_next_screen(self):
        try:
            app.pulse2 = int(self.result_before_input.text)
            app.pulse3 = int(self.result_after_input.text)
            self.manager.current = 'FifthScreen'
        except ValueError:
            pass

class FifthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = 'vertical', spacing = '20px', padding = '20px')
        self.text_label = Label(halign = 'center', font_size = 22)
        self.result_label = Label(halign = 'center', font_size = 22)
        main_layout.add_widget(self.text_label)
        main_layout.add_widget(self.result_label)
        self.on_enter = self.print_result
        self.add_widget(main_layout)
    
    def print_result(self):
        result = ruffier.test(app.pulse1, app.pulse2, app.pulse3, app.age)
        if type(result) == tuple:
            self.text_label.text = result[0]
            self.result_label.text = result[1]
        else:
            self.text_label.text = result


app = My()
app.run()