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
from kivy.uix.switch import Switch
from kivy.core.audio import SoundLoader
from kivy.uix.textinput import TextInput
from Singleton import *
from OwnBoard import BaseOwnBoard
from Board import Board
from Instructions import Instructions
from Winner import *
from BoardMe import BoardMe
from BoardPlay import *
from BoardPlay2 import *
from Board2 import *
from SendPackage import *
import socket

Builder.load_file('Battleship.kv')	


sound = SoundLoader.load('../sound/pirata.wav')
sound2 = SoundLoader.load('../sound/piratasCaribe.wav')
sound.loop = True
sound2.loop = True

class MenuScreen(Screen):
	pass
class PlayerOnlineScreen(Screen):
	def saveIP(self):
		Singleton().opponentIP = self.ids.ipText.text
		self.manager.current = 'OwnBoardScreen'
		

class SettingsScreen(Screen):

	def back_to_menu(self, instance):
		self.manager.current = 'menu'

	def switch_sound(self, instance, value):
		if instance.active == False:
			sound.stop()
			sound2.stop()
			Singleton().soundState = False
		elif instance.active == True:
			sound.play()
			sound2.play()


class OwnBoardScreen(Screen):
    def choose_next_screen(self):
    	sound.stop()
    	if(Singleton().mode == 'TwoPlayers'):
        	self.manager.current = 'gameBoard2'
    	else:
        	send(Singleton().opponentIP , '1,'+str(Singleton().matrix))
        	self.manager.current = 'gameBoard'


class PreOwnBoardScreen(Screen):
	def __init__(self, **kwargs):
		''''''
		super(PreOwnBoardScreen, self).__init__(**kwargs)

	def on_pre_enter(self):
		Singleton().mode = 'TwoPlayers'


class GameBoardScreen(Screen):
	def __init__(self, **kwargs):
		''''''
		super(GameBoardScreen, self).__init__(**kwargs)

	def on_pre_enter(self):
		if(Singleton().soundState==True):
			sound2.play()

		Singleton().gameboard.add_widget(Image(source='../img/background_wood.png'))
		grid = GridLayout(cols=2,rows=2)
		grid.add_widget(Label(text='[color=fc9701]Opponent[/color]',markup = True, font_size=26, size_hint_y=0.05))
		grid.add_widget(Label(text='[color=fc9701]My board[/color]',markup = True, font_size=26, size_hint_y=0.05))
		grid.add_widget(BoardPlay(name='opponent'))
		grid.add_widget(BoardMe(name='myBoard'))
		Singleton().gameboard.add_widget(grid)
		
class GameBoardScreen2(Screen):
	
	def __init__(self, **kwargs):
		''''''
		super(GameBoardScreen2, self).__init__(**kwargs)
		

	def on_pre_enter(self):
		
		if(Singleton().soundState==True):
			sound2.play()
		if(Singleton().winner==1):
			grid = GridLayout(cols=1)
			grid.add_widget(Board().winner)
			
			Singleton().gameboard2 = grid

		else:
			Singleton().gameboard2.add_widget(Image(source='../img/background_wood.png'))
			grid = GridLayout(cols=2,rows=2)
			grid.add_widget(Label(text='[color=fc9701]Player 1[/color]',markup = True, font_size=26, size_hint_y=0.05))
			grid.add_widget(Label(text='[color=fc9701]Player 2[/color]',markup = True, font_size=26, size_hint_y=0.05))
			grid.add_widget(BoardPlay(name='player1'))
			grid.add_widget(BoardPlay2(name='player2'))
			Singleton().gameboard2.add_widget(grid)		


class BattleshipApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MenuScreen(name='menu'))

		ownBoardScreen = OwnBoardScreen(name='OwnBoardScreen')
		base = GridLayout(cols=2)
		board = Board()
		ins = board.instructions
		base.add_widget(board)
		base.add_widget(ins)
		ownBoardScreen.add_widget(base)
		sm.add_widget(ownBoardScreen)

		preOwnBoardScreen = PreOwnBoardScreen(name='PreOwnBoardScreen')
		base2 = GridLayout(cols=2)
		board2 = Board2()
		ins2 = board2.instructions
		base2.add_widget(board2)
		base2.add_widget(ins2)
		preOwnBoardScreen.add_widget(base2)
		sm.add_widget(preOwnBoardScreen)
		
		gameBoard = GameBoardScreen(name='gameBoard')
		Singleton().gameboard = gameBoard
		sm.add_widget(gameBoard)

		gameBoard2 = GameBoardScreen2(name='gameBoard2')
		Singleton().gameboard2 = gameBoard2
		sm.add_widget(gameBoard2)


		settingsScreen = SettingsScreen(name='SettingsScreen')
		anchor = AnchorLayout(anchor_x='right', anchor_y='bottom')
		backButton = Button(background_normal= '../img/menu.png', background_down= '../img/menu2.png',size_hint=(0.4,0.2))
		backButton.bind(on_press=settingsScreen.back_to_menu)
		anchor.add_widget(backButton)

		settingsGrid = GridLayout(cols=6)
		sw = Switch(active=False)
		sw.bind(active=settingsScreen.switch_sound)
		settingsGrid.add_widget(Label(text='[color=fc9701]Sound[/color]',markup = True, font_size=22))
		settingsGrid.add_widget(sw)

		settingsScreen.add_widget(settingsGrid)
		settingsScreen.add_widget(anchor)
		sm.add_widget(settingsScreen)	

		playerOnlineScreen = PlayerOnlineScreen(name='PlayerOnlineScreen')

		sm.add_widget(playerOnlineScreen)



		return sm

if __name__ == '__main__':
	BattleshipApp().run()