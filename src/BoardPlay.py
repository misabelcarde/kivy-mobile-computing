from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from Singleton import *
from Instructions import Instructions
from OwnBoard import BaseOwnBoard
from BoardFunctions import *
from SendPackage import *

from kivy.lang import Builder
Builder.load_string(''' 
<BoardPlay>:
	id: boardPlayID
	cols: 11
	rows: 11
''')


class BoardPlay(GridLayout):
	'''Generation of the board and functions for complete it'''
	def __init__(self, **kwargs):
		super(BoardPlay, self).__init__(**kwargs)
		self.diccp = {}
		self.generateBoard()
		self.base = Singleton()

	def generateBoard(self):
		'''Generation of buttons and labels. Buttons are added to a dictionary where key:id and value:button'''
		letters = ('A','B','C','D','E','F','G','H','I','J')
		self.add_widget(Label(text=''))
		if(Singleton().mode == 'TwoPlayers'):
			for i in range(1,11):
				self.add_widget(Label(text=str(i)))

			for j in range(0,len(letters)):
			 	self.add_widget(Label(text=letters[j]))
			 	for k in range(0,10):
			 		button=Button(id=(str(j)+'_'+str(k)),background_color=(0,2,255,1))
			 		button.bind(on_press=self.putBoat)
			 		self.add_widget(button)
			 		self.diccp[str(j)+'_'+str(k)]=button
			 		if Singleton().matrix[j][k] == 2:
						 button.background_color = [255,0,0,1]
						 button.text = "BOM"
						 button.disabled = True
			 		elif Singleton().matrix[j][k] == -1:
						 button.background_color = [0,2,255,1]
						 button.text ='·' 
						 button.font_size = 50
						 button.disabled = True
			 		if Singleton().turno == 1 :
			 			button.disabled = True
		
		else:
			#ListenSocket()
			for i in range(1,11):
				self.add_widget(Label(text=str(i)))

			for j in range(0,len(letters)):
			 	self.add_widget(Label(text=letters[j]))
			 	for k in range(0,10):
			 		button=Button(id=(str(j)+'_'+str(k)),background_color=(0,2,255,1))
			 		button.bind(on_press=self.putBoat)
			 		self.add_widget(button)
			 		self.diccp[str(j)+'_'+str(k)]=button
			 		if Singleton().matrix2[j][k] == 2:
						 button.background_color = [255,0,0,1]
						 button.text = "BOM"
						 button.disabled = True
			 		elif Singleton().matrix2[j][k] == -1:
						 button.background_color = [0,2,255,1]
						 button.text ='·' 
						 button.font_size = 50
						 button.disabled = True
		
	
	def putBoat(self, button):
		'''Behaviour of board's cells (buttons)'''
		limits = getLimitingButtons(button)
		boatsIds = getBoatsIds()
		pos = getButtonPosition(button)

		if(Singleton().mode == 'TwoPlayers'):
			if self.base.matrix[pos[0]][pos[1]] == 1:
				self.base.matrix[pos[0]][pos[1]] = 2
				button.background_color = [255,0,0,1]
				button.text = "BOM"
				button.disabled = True
				self.base.aux+=1
				if self.base.aux == 20:
					self.base.winner=1
				
			elif self.base.matrix[pos[0]][pos[1]] == 0:
				self.base.matrix[pos[0]][pos[1]] = -1
				button.background_color = [0,2,255,1]
				button.text ='·' 
				button.font_size = 50
				button.disabled = True
			self.base.turno = 1

		else:
			if self.base.matrix2[pos[0]][pos[1]] == 1:
				self.base.matrix2[pos[0]][pos[1]] = 2
				button.background_color = [255,0,0,1]
				button.text = "BOM"
				button.disabled = True
				self.base.aux+=1
				if self.base.aux == 20:
					self.base.winner=1
			
			elif self.base.matrix2[pos[0]][pos[1]] == 0:
				self.base.matrix2[pos[0]][pos[1]] = -1
				button.background_color = [0,2,255,1]
				button.text ='·' 
				button.font_size = 50
				button.disabled = True
			#solo para 2 jugadores self.base.turno = 1
		
		Singleton().gameboard.clear_widgets(children=None)
		Singleton().gameboard2.clear_widgets(children=None)

		if self.base.mode == 'TwoPlayers':
			Singleton().gameboard2.on_pre_enter()
		else:
			Singleton().gameboard.on_pre_enter()
			send(Singleton().opponentIP,str(self.base.matrix2))