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

#Builder.load_file('Battleship.kv')	
Builder.load_string('''

''')

class BattleshipApp(App):
	def build(self):
		# sm = ScreenManager(id= 'smID')
		# sc = Screen(name='secondBoard')
		

		base = BaseOwnBoard()
		base.add_widget(Board())
		base.add_widget(Instructions())


		# sc.add_widget(base)
		

		# sc2 = Screen(name='holascreen')
		# sc2.add_widget(Label(text='hola screeennenene'))
		# sm.add_widget(sc)
		# sm.add_widget(sc2)

		return base

if __name__ == '__main__':
	BattleshipApp().run()