from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.uix.boxlayout import BoxLayout


from kivy.config import Config

# Controllers
from Controllers.Homepage import Homepage
from Controllers.SpiceSelection import SpiceSelection
from Controllers.Banner import Banner


# Initial Configuration
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
Config.set('graphics', 'resizable', 0)

# Load File from Views
Builder.load_file("Views/Homepage.kv")
Builder.load_file("Views/SpiceSelection.kv")
Builder.load_file("Views/Banner.kv")
# Add to screen manager
screenManager = ScreenManager(transition=FadeTransition())
screenManager.add_widget(Homepage(name='Homepage'))
screenManager.add_widget(SpiceSelection(name='SpiceSelection'))

layout = BoxLayout(orientation='vertical')
# layout.add_widget(Banner())
layout.add_widget(screenManager)


class SpiceMixerApp(App):
    def build(self):
        return layout


if __name__ == '__main__':
    SpiceMixerApp().run()
