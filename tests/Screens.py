#http://kivy.org/docs/api-kivy.uix.screenmanager.html

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

from OwnBoard import BaseOwnBoard
from Board import Board
from Instructions import Instructions, Continue
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    Button:
        text: 'Jugar'
        on_press: root.manager.current = 'ownBoard'

<OwnBoardScreen>:
    Button:
        text: 'Back to menu'
        on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class OwnBoardScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(OwnBoardScreen(name='ownBoard'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()