# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string('''
#:import h2c kivy.parser.parse_color

<WeatherScreen>:
    id: 'weather_screen'
    GridLayout:
        rows: 3
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: '[color=#3498DB]Temperature and Humidity[/color]'
                font_size: 48
                markup: True
        BoxLayout:
            orientation: 'horizontal'
            BoxLayout:
                orientation: 'vertical'
                Label:
                    id: txt_temperature
                    text: '999 °C'
                    font_size: 48
                Label:
                    text: 'Temperature'
                    font_size: 24
            BoxLayout:
                orientation: 'vertical'
                Label:
                    id: txt_humidity
                    text: '999 %'
                    font_size: 48
                Label:
                    text: 'Humidity'
                    font_size: 24
        BoxLayout:
            padding: [250, 50]
            Button:
                id: weather_btn_OK
                font_size: 28
                text: 'OK'
                background_normal: ''
                background_color: h2c('#3498DB')
                on_press: root.weather_btn_ok()
''')


class WeatherScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    def build(self):
        return self

    def weather_btn_ok(self):
        self.parent.current = 'splash_screen'