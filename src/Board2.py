from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from Singleton import *
from Instructions import Instructions
from OwnBoard import BaseOwnBoard
from BoardFunctions import *

from kivy.lang import Builder
Builder.load_string(''' 
<Board2>:
	id: board2ID
	cols: 11
	rows: 11
''')


class Board2(GridLayout):
	'''Generation of the board and functions for complete it'''
	def __init__(self, **kwargs):
		''''''
		super(Board2, self).__init__(**kwargs)
		self.dicc = {}
		self.generateBoard()
		self.instructions = Instructions()
		self.base = Singleton()
		
	def generateBoard(self):
		'''Generation of buttons and labels. Buttons are added to a dictionary where key:id and value:button'''
		letters = ('A','B','C','D','E','F','G','H','I','J')
		self.add_widget(Label(text=''))
		for i in range(1,11):
			self.add_widget(Label(text=str(i)))

		for j in range(0,len(letters)):
		 	self.add_widget(Label(text=letters[j]))
		 	for k in range(0,10):
		 		button=Button(id=(str(j)+'_'+str(k)),background_color=(0,2,255,1))
		 		button.bind(on_press=self.putBoat)
		 		self.add_widget(button)
		 		self.dicc[str(j)+'_'+str(k)]=button
	
	def putBoat(self, button):
		'''Behaviour of board's cells (buttons)'''
		limits = getLimitingButtons(button)
		boatsIds = getBoatsIds()
		pos = getButtonPosition(button)
		if button.background_color == [0,2,255,1]:
			button.background_color = [0,1,0,1]
			#button.text = button.id
			self.base.matrix2[pos[0]][pos[1]] = 1

			#EN PROCESO... CAMBIO DE IMAGENES AL SELECCIONAR:
			
			# changeDone=False
			# if not changeDone: 
			# 	for boat41 in boatsIds['41Ids']:
			# 		barco = self.instructions.boardDicc[boat41]
			# 		if barco.source == "../img/LightBlueCircle.png":
			# 			if exixtsLimits(button, self.dicc, limits):
			# 				if not colourUp(self.dicc, limits) and not colourDown(self.dicc, limits) and not colourLeft(self.dicc, limits) and not colourRight(self.dicc, limits):
			# 					barco.source = "../img/DarkBlueCircle.png"
			# 					changeDone = True
			# 					break
			# 			elif exixtsLimitsNoUp(button, self.dicc, limits):
			# 				if not colourDown(self.dicc, limits) and not colourLeft(self.dicc, limits) and not colourRight(self.dicc, limits):
			# 					barco.source = "../img/DarkBlueCircle.png"
			# 					changeDone = True
			# 					break
			# 			elif exixtsLimitsNoDown(button, self.dicc, limits):
			# 				if not colourUp(self.dicc, limits) and not colourLeft(self.dicc, limits) and not colourRight(self.dicc, limits):
			# 					barco.source = "../img/DarkBlueCircle.png"
			# 					changeDone = True
			# 					break
			# 			elif exixtsLimitsNoLeft(button, self.dicc, limits):
			# 				if not colourUp(self.dicc, limits) and not colourDown(self.dicc, limits) and not colourRight(self.dicc, limits):
			# 					barco.source = "../img/DarkBlueCircle.png"
			# 					changeDone = True
			# 					break
			# 			elif exixtsLimitsNoRight(button, self.dicc, limits):
			# 				if not colourUp(self.dicc, limits) and not colourDown(self.dicc, limits) and not colourLeft(self.dicc, limits):
			# 					barco.source = "../img/DarkBlueCircle.png"
			# 					changeDone = True
			# 					break
			# 			elif exixtsLimitsNoUpLeft(button, self.dicc, limits):
			# 				if not colourDown(self.dicc, limits) and not colourRight(self.dicc, limits):
			# 					barco.source = "../img/DarkBlueCircle.png"
			# 					changeDone = True
			# 					break
			# 			elif exixtsLimitsNoUpRight(button, self.dicc, limits):
			# 				if not colourDown(self.dicc, limits) and not colourLeft(self.dicc, limits):
			# 					barco.source = "../img/DarkBlueCircle.png"
			# 					changeDone = True
			# 					break
			# 			elif exixtsLimitsNoDownLeft(button, self.dicc, limits):
			# 				if not colourUp(self.dicc, limits) and not colourRight(self.dicc, limits):
			# 					barco.source = "../img/DarkBlueCircle.png"
			# 					changeDone = True
			# 					break
			# 			elif exixtsLimitsNoDownRight(button, self.dicc, limits):
			# 				if not colourUp(self.dicc, limits) and not colourLeft(self.dicc, limits):
			# 					barco.source = "../img/DarkBlueCircle.png"
			# 					changeDone = True
			# 					break



			# if not changeDone: 
			# 	for boat32 in boatsIds['32Ids']:
			# 		barcoLeft = self.instructions.boardDicc[boat32[0]]
			# 		barcoRight = self.instructions.boardDicc[boat32[1]]
			# 		if barcoLeft.source == "../img/LightBlueMidCircleLeft.png" and barcoRight.source == "../img/LightBlueMidCircleRight.png":

			# 			if exixtsLimits(button, self.dicc, limits):
			# 				if noColourLimitsLessUp(self.dicc, limits) and not colourLimitUp2(self.dicc, limits):
			# 					barcoLeft.source = "../img/DarkBlueMidCircleLeft.png"
			# 					barcoRight.source = "../img/DarkBlueMidCircleRight.png"
			# 					changeDone = True
			# 					break

			# 				elif noColourLimitsLessDown(self.dicc, limits):
			# 					if (self.dicc[limits['down2']].background_color != [1,0.65,0,1]):
			# 						barcoLeft.source = "../img/DarkBlueMidCircleLeft.png"
			# 						barcoRight.source = "../img/DarkBlueMidCircleRight.png"
			# 						changeDone = True
			# 						break

			# 				elif noColourLimitsLessLeft(self.dicc, limits):
			# 					if (self.dicc[limits['left2']].background_color != [1,0.65,0,1]):
			# 						barcoLeft.source = "../img/DarkBlueMidCircleLeft.png"
			# 						barcoRight.source = "../img/DarkBlueMidCircleRight.png"
			# 						print("Izq")
			# 						changeDone = True
			# 						break

			# 				elif noColourLimitsLessRight(self.dicc, limits):
			# 					if (self.dicc[limits['right2']].background_color != [1,0.65,0,1]):
			# 						barcoLeft.source = "../img/DarkBlueMidCircleLeft.png"
			# 						barcoRight.source = "../img/DarkBlueMidCircleRight.png"
			# 						print("derecha")
			# 						changeDone = True
			# 						break


			# 	for boat41 in boatsIds['41Ids']:
			# 		barco = self.instructions.boardDicc[boat41]
			# 		if barco.source == "../img/DarkBlueCircle.png":
			# 			if exixtsLimits(button, self.dicc, limits):
			# 				if ((colourUp(self.dicc, limits) and not colourUp2(self.dicc, limits)) or (colourDown(self.dicc, limits) and not colourDown2(self.dicc, limits)) or (colourLeft(self.dicc, limits) and not colourLeft2(self.dicc, limits)) or (colourRight(self.dicc, limits) and not colourRight2(self.dicc, limits))):
			# 					barco.source = "../img/LightBlueCircle.png"
			# 					break
			# 			elif exixtsLimitsNoUp(button, self.dicc, limits):
			# 				if ((colourDown(self.dicc, limits) and not colourDown2(self.dicc, limits)) or (colourLeft(self.dicc, limits) and not colourLeft2(self.dicc, limits)) or (colourRight(self.dicc, limits) and not colourRight2(self.dicc, limits))):								
			# 					barco.source = "../img/LightBlueCircle.png"
			# 					break
			# 			elif exixtsLimitsNoDown(button, self.dicc, limits):
			# 				if ((colourUp(self.dicc, limits) and not colourUp2(self.dicc, limits)) or (colourLeft(self.dicc, limits) and not colourLeft2(self.dicc, limits)) or (colourRight(self.dicc, limits) and not colourRight2(self.dicc, limits))):
			# 					barco.source = "../img/LightBlueCircle.png"
			# 					break
			# 			elif exixtsLimitsNoLeft(button, self.dicc, limits):
			# 				if ((colourUp(self.dicc, limits) and not colourUp2(self.dicc, limits)) or (colourDown(self.dicc, limits) and not colourDown2(self.dicc, limits)) or (colourRight(self.dicc, limits) and not colourRight2(self.dicc, limits))):
			# 					barco.source = "../img/LightBlueCircle.png"
			# 					break
			# 			elif exixtsLimitsNoRight(button, self.dicc, limits):
			# 				if ((colourUp(self.dicc, limits) and not colourUp2(self.dicc, limits)) or (colourDown(self.dicc, limits) and not colourDown2(self.dicc, limits)) or (colourLeft(self.dicc, limits) and not colourLeft2(self.dicc, limits))):
			# 					barco.source = "../img/LightBlueCircle.png"
			# 					break
			# 			elif exixtsLimitsNoUpLeft(button, self.dicc, limits):
			# 				if ((colourDown(self.dicc, limits) and not colourDown2(self.dicc, limits)) or (colourRight(self.dicc, limits) and not colourRight2(self.dicc, limits))):
			# 					barco.source = "../img/LightBlueCircle.png"
			# 					break
			# 			elif exixtsLimitsNoUpRight(button, self.dicc, limits):
			# 				if ((colourDown(self.dicc, limits) and not colourDown2(self.dicc, limits)) or (colourLeft(self.dicc, limits) and not colourLeft2(self.dicc, limits))):
			# 					barco.source = "../img/LightBlueCircle.png"
			# 					break
			# 			elif exixtsLimitsNoDownLeft(button, self.dicc, limits):
			# 				if ((colourUp(self.dicc, limits) and not colourUp2(self.dicc, limits)) or (colourRight(self.dicc, limits) and not colourRight2(self.dicc, limits))):
			# 					barco.source = "../img/LightBlueCircle.png"
			# 					break
			# 			elif exixtsLimitsNoDownRight(button, self.dicc, limits):
			# 				if ((colourUp(self.dicc, limits) and not colourUp2(self.dicc, limits)) or (colourLeft(self.dicc, limits) and not colourLeft2(self.dicc, limits))):
			# 					barco.source = "../img/LightBlueCircle.png"
			# 					break			




						



			




			if(limits['upLeft'] in self.dicc):
				buttonUpLeft = self.dicc[limits['upLeft']]
				buttonUpLeft.disabled = True

			if(limits['upRight'] in self.dicc):
				buttonUpRight = self.dicc[limits['upRight']]
				buttonUpRight.disabled = True

			if(limits['downLeft'] in self.dicc):
				buttonDownLeft = self.dicc[limits['downLeft']]
				buttonDownLeft.disabled = True

			if(limits['downRight'] in self.dicc):
				buttonDownRight = self.dicc[limits['downRight']]
				buttonDownRight.disabled = True


		else:

			button.background_color = [0,2,255,1]
			self.base.matrix2[pos[0]][pos[1]] = 0


			if(limits['upLeft'] in self.dicc):
				buttonUpLeft = self.dicc[limits['upLeft']]
				# posUpLeft = getButtonPosition(buttonUpLeft)
				# self.base.matrix[posUpLeft[0]][posUpLeft[1]] = 0
				# buttonUpLeft.background_color = [1,1,1,1]
				buttonUpLeft.disabled = False

			if(limits['upRight'] in self.dicc):
				buttonUpRight = self.dicc[limits['upRight']]
				# posUpRight = getButtonPosition(buttonUpRight)
				# self.base.matrix[posUpRight[0]][posUpRight[1]] = 0
				# buttonUpRight.background_color = [1,1,1,1]
				buttonUpRight.disabled = False

			if(limits['downLeft'] in self.dicc):
				buttonDownLeft = self.dicc[limits['downLeft']]
				# posDownLeft = getButtonPosition(buttonDownLeft)
				# self.base.matrix[posDownLeft[0]][posDownLeft[1]] = 0
				# buttonDownLeft.background_color = [1,1,1,1]
				buttonDownLeft.disabled = False

			if(limits['downRight'] in self.dicc):
				buttonDownRight = self.dicc[limits['downRight']]
				# posDownRight = getButtonPosition(buttonDownRight)
				# self.base.matrix[posDownRight[0]][posDownRight[1]] = 0
				# buttonDownRight.background_color = [1,1,1,1]
				buttonDownRight.disabled = False

	
