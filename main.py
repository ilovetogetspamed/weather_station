import os
import sys

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase, Label
from kivy.config import Config

#from kivy.properties import NumericProperty
from kivy.lang import Factory

from modules.navbar import NavBar
from modules.splashscreen import SplashScreen
from modules.weatherscreen import WeatherScreen

# Adjust for RasPi touch screen size
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')

APP_PATH = os.path.dirname(__file__)

LabelBase.register(name='FontAwesome',
                   fn_regular='assets/fonts/font-awesome-4.6.3/fonts/fontawesome-webfont.ttf')

LabelBase.register(name='LCDMono',
                   fn_regular='assets/fonts/LCDMonoWinTT/LCDM2N__.TTF',
                   fn_bold='assets/fonts/LCDMonoWinTT/LCDM2B__.TTF')



class ScreenManagerApp(App):

    def build(self):

        # # Common modules
        Factory.register('NavBar', module='modules.navbar')
        Factory.register('SplashScreen', module='modules.splashscreen')
        Factory.register('WeatherScreen', module='modules.weatherscreen')

        splash_screen = SplashScreen(name='splash_screen')
        weather_screen = WeatherScreen(name='weather_screen')

        root = ScreenManager()

        root.add_widget(splash_screen)
        root.add_widget(weather_screen)

        root.current = 'splash_screen'
        return root

if __name__ == '__main__':
    ScreenManagerApp().run()