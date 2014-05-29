from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from Singleton import *
from Instructions import Instructions
from OwnBoard import BaseOwnBoard
from BoardFunctions import *


from kivy.lang import Builder
Builder.load_string(''' 
<BoardPlay2>:
	id: boardPlay2ID
	cols: 11
	rows: 11
''')


class BoardPlay2(GridLayout):
	'''Generation of the board and functions for complete it'''
	def __init__(self, **kwargs):
		super(BoardPlay2, self).__init__(**kwargs)
		self.diccp = {}
		self.generateBoard()
		self.base = Singleton()

	def generateBoard(self):
		'''Generation of buttons and labels. Buttons are added to a dictionary where key:id and value:button'''
		letters = ('A','B','C','D','E','F','G','H','I','J')
		self.add_widget(Label(text=''))
		sing = Singleton()
		for i in range(1,11):
			self.add_widget(Label(text=str(i)))

		for j in range(0,len(letters)):
		 	self.add_widget(Label(text=letters[j]))
		 	for k in range(0,10):
		 		button=Button(id=(str(j)+'_'+str(k)),background_color=(0,2,255,1))
		 		button.bind(on_press=self.putBoat)
		 		self.add_widget(button)
		 		self.diccp[str(j)+'_'+str(k)]=button
		 		if sing.matrix2[j][k] == 2:
						 button.background_color = [255,0,0,1]
						 button.text = "BOM"
						 button.disabled = True
			 	elif sing.matrix2[j][k] == -1:
						 button.background_color = [0,2,255,1]
						 button.text ='·' 
						 button.font_size = 50
						 button.disabled = True
		 		if sing.turno == 0 :
		 			button.disabled = True
		
	
	def putBoat(self, button):
		'''Behaviour of board's cells (buttons)'''
		limits = getLimitingButtons(button)
		boatsIds = getBoatsIds()
		pos = getButtonPosition(button)
		
		#if button.background_color == [1,1,1,1]:
		#if self.base.matrix[pos[0]][pos[1]] == 1:
		if self.base.matrix2[pos[0]][pos[1]] == 1:
			self.base.matrix2[pos[0]][pos[1]] = 2
			button.background_color = [255,0,0,1]
			button.background_normal = '../img2/explosion2.jpg'
			button.background_down = '../img2/explosion2.jpg'
			# button.background_disable_down = '../img2/explosion2.jpg'
			# button.background_disable_normal = '../img2/explosion2.jpg'
			button.text = "BOM"
			button.disabled = True
			self.base.aux2+=1
			if self.base.aux2 == 20:
				self.base.winner=1

		elif self.base.matrix2[pos[0]][pos[1]] == 0:
			self.base.matrix2[pos[0]][pos[1]] = -1
			button.background_color = [0,2,255,1]
			button.text ='·' 
			button.font_size = 50
			button.disabled = True
		self.base.turno = 0
		Singleton().gameboard2.clear_widgets(children=None)
		Singleton().gameboard2.on_pre_enter()
