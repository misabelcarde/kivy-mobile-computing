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
from Instructions import Instructions
from BoardMe import BoardMe

#Builder.load_file('Battleship.kv')	
Builder.load_string('''
<MenuScreen>:
    Image: 
    	source: '../img/index.jpg'

    AnchorLayout:
		anchor_x: 'right'
		anchor_y: 'bottom'
		Button:
			text: 'Play'
			size_hint_x: 0.20
			size_hint_y: 0.10
			on_release: root.manager.current = 'ownBoard'

	AnchorLayout:
		anchor_x: 'left'
		anchor_y: 'bottom'
		Button:
			text: 'Settings'
			size_hint_x: 0.20
			size_hint_y: 0.10
			on_release: root.manager.current = 'ownBoard'


<OwnBoardScreen>:
	AnchorLayout:
		anchor_x: 'right'
		anchor_y: 'bottom'
		Button:
			id: 'continueButton'
			name: 'continueButton'
			text: 'Continue'
			size_hint_x: 0.40
			size_hint_y: 0.20
			on_release: root.manager.current = 'gameBoard'		

''')

class MenuScreen(Screen):
    pass

class OwnBoardScreen(Screen):
    pass

class GameBoardScreen(Screen):
	pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

own = OwnBoardScreen(name='ownBoard')
base = GridLayout(cols=2)
board = Board()
ins = board.instructions
base.add_widget(board)
base.add_widget(ins)
own.add_widget(base)
sm.add_widget(own)

boardMe = GameBoardScreen(name='gameBoard')
grid = GridLayout(cols=2)
grid.add_widget(Board(name='player1'))
grid.add_widget(BoardMe(name='player2'))
boardMe.add_widget(grid)
sm.add_widget(boardMe)

class BattleshipApp(App):
	def build(self):
		return sm

if __name__ == '__main__':
	BattleshipApp().run()