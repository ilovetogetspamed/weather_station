from kivy.uix.screenmanager import Screen
from modules.navbar import NavBar
from kivy.lang import Builder

splash_screen = Builder.load_string('''
<SplashScreen>:
    id: 'splash_screen'
    # Image:
    #     source: 'assets/splash.png'
    #     # size_hint: .8, .8
    #     pos_hint: {'center_x': .5, 'center_y': .5}
    Label:
        text: 'Weather Station'
        font_size: 64
        pos_hint: {'center_x': .5, 'center_y': .5}
    NavBar:
''')


class SplashScreen(Screen):

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    def build(self):
        return self