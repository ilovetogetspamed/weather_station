from kivy.uix.actionbar import ActionBar
from kivy.lang import Builder
from kivy.logger import Logger

Builder.load_string('''
#:import h2c kivy.parser.parse_color

<ActionButton>:
    font_name: 'FontAwesome'
    font_size: 48
    markup: True

<NavBar>
    id: nav_bar
    top: root.height
    pos_hint: {'top':1}
    size_hint: 1, None
    manager:
    ActionView:
        use_separator: True
        ActionPrevious:
            title: 'Weather Station'
            with_previous: False
        ActionOverflow:
        ActionButton:           # UNLOCK/LOCK Button
            id: ab_lock
#                text: u'\uF09C'    # UNLOCK Glyph
            text: u'\uF023'     # LOCK Glyph
            on_release: root.open_loginlogout()
        ActionGroup:            # Menu
            id: ag_menu
            mode: 'spinner'
            font_name: 'FontAwesome'
            text: u'\uF039'
            font_size: 48
            markup: True
            ActionButton:
                id: ab_menu_head_errors
                text: u'\uF127'
                on_release: root.open_menu_head_errors()
            ActionButton:
                id: ab_menu_kpi
                text: u'\uF080'
                on_release: root.open_menu_kpi()
            ActionButton:
                id: ab_menu_weather     # Weather App
                text: u'\uF0E9'
                on_release: root.open_menu_weather()
        ActionButton:          # Display Network Settings
            id: ab_network
            text: u'\uF1EB'
            color: h2c('#2ECC71')
            on_release: root.open_networking()
        ActionButton:           # Application Settings
            id: ab_settings
            text: u'\uF013'
            on_release: root.open_settings()
        # ActionGroup:            # I18n L10n Button Group
            # font_name: 'FontAwesome'
            # text: u'\uF11D'
            # mode: 'normal'
            # markup: True
        ActionButton:
            id: ab_lang_gb
            text: u'\uF13a'
            icon: './assets/UK.png'
            markup: True
            on_release: root.i18n_English()
        ActionButton:
            id: ab_lang_de
            text: u'\uF13a'
            icon: './assets/DE.png'
            markup: True
            on_release: root.i18n_German()
#            ActionButton:
#                id: ab_lang_es
#                text: 'Btn6'
#                icon: './assets/ES.png'
#                on_release: root.i18n_English()
#            ActionButton:
#                id: ab_lang_cn
#                text: 'Btn7'
#                icon: './assets/CN.png'
#                on_release: root.i18n_English()
''')


class NavBar(ActionBar):

    logged_in = False

    pass

    def open_loginlogout(self):
        Logger.info('Weather Station: login/logout')

        # Do Login Here..:
        self.logged_in ^= True  # toggle settings for now...

        if self.logged_in:
            # if..then..else for type of login here
            # just go to operator panel for now
            self.parent.current = 'operator_panel_screen'
            # unlock the screen..
            # self.root.ids.nav_bar.ab_lock.text = u'\uF09C'
        else:
            self.parent.current = 'splash_screen'
            # self.root.ids.ab_lock.text = u'\uF23C'  # Lock
        Logger.info('Weather Station: Logged In==' + repr(self.logged_in))

    def open_networking(self):
        Logger.info('Weather Station: open_networking')

    def open_settings(self, *largs):
        Logger.info('Weather Station: open settings')

    def open_menu_head_errors(self):
        Logger.info('Weather Station: open menu head breaks')

    def open_menu_operator_kpi(self):
        Logger.info('Weather Station: open menu KPI')

    def open_menu_weather(self):
        Logger.info('Weather Station: open menu weather')
        my_parent = self.parent
        print 'My Parent: {0}'.format(my_parent)
        my_parents_parent = my_parent.parent
        print 'My Parent\'s Parent: {0}'.format(my_parents_parent)
        my_parents_parent.current_screen = 'weather_screen'

    def i18n_English(self):
        Logger.info('Weather Station: switching language to English')

    def i18n_German(self):
        Logger.info('Weather Station: switching language to German')

    def i18n_Spanish(self):
        Logger.info('Weather Station: switching language to Spanish')

    def i18n_Chinese(self):
        Logger.info('Weather Station: switching language to Chinese')
