from kivy.uix.label import Label
from kivy.properties import BooleanProperty


class Timer(Label):
    done = BooleanProperty(False)
    
    def __init__(self, time_value, **kwargs):
        self.time_value = time_value
        self.done = False
        self.current_time = 0
        my_text = 'Прошло секунд: ' + str(self.current_time)
        super().__init__(self, text = my_text, **kwargs)