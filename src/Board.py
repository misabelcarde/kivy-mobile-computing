from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from Instructions import Instructions

from kivy.lang import Builder
Builder.load_string(''' 
<Board>:
	id: boardID
	cols: 11
	rows: 11
''')


class Board(GridLayout):
	'''Generation of the board and functions for complete it'''

	def __init__(self, **kwargs):
		''''''
		super(Board, self).__init__(**kwargs)
		self.dicc = {}
		self.generateBoard()
		self.instructions = Instructions()
		
	def generateBoard(self):
		'''Generation of buttons and labels. Buttons are added to a dictionary where key:id and value:button'''
		letters = ('A','B','C','D','E','F','G','H','I','J')
		self.add_widget(Label(text=''))
		for i in range(1,11):
			self.add_widget(Label(text=str(i)))

		for j in range(0,len(letters)):
		 	self.add_widget(Label(text=letters[j]))
		 	for k in range(0,10):
		 		button=Button(id=(str(j)+'_'+str(k)),background_color=(1,1,1,1))
		 		button.bind(on_press=self.putBoat)
		 		self.add_widget(button)
		 		self.dicc[str(j)+'_'+str(k)]=button
	
	def putBoat(self, button):
		'''Behaviour of board's cells (buttons)'''
		idSplit = button.id.split("_")
		row = int(idSplit[0])
		col = int(idSplit[1])
		up = str (row-1)+"_"+str(col)
		down = str (row+1)+"_"+str(col)
		right = str (row)+"_"+str(col+1)
		left = str (row)+"_"+str(col-1)
		upLeft = str (row-1)+"_"+str(col-1)
		upRight = str (row-1)+"_"+str(col+1)
		downLeft = str (row+1)+"_"+str(col-1)
		downRight = str (row+1)+"_"+str(col+1)

		boats41Ids = ["4_1_0", "4_1_1", "4_1_2", "4_1_3"]
		boats32Ids = ["3_2_0_0", "3_2_0_1", "3_2_1_0", "3_2_1_1","3_2_2_0","3_2_2_1"]
		boats23Ids = ["2_3_0_0","2_3_0_1","2_3_0_2","2_3_1_0","2_3_1_1","2_3_1_2"]
		boats14Ids = ["1_4_0", "1_4_1", "1_4_2", "1_4_3"]

		if button.background_color == [1,1,1,1]:
			button.background_color = (1,0.65,0,1)
			button.text = button.id

			boats41Done = False
			for boat41 in boats41Ids:
				barco = self.instructions.boardDicc[boat41]
				if barco.source == "../img/LightBlueCircle.png":
					if (up in self.dicc) and (down in self.dicc) and (left in self.dicc) and (right in self.dicc) :
						if (self.dicc[up].background_color != [1,0.65,0,1]) and (self.dicc[down].background_color != [1,0.65,0,1]) and (self.dicc[left].background_color != [1,0.65,0,1]) and (self.dicc[right].background_color != [1,0.65,0,1]):
							barco.source = "../img/DarkBlueCircle.png"
							self.instructions.boardDicc[boat41] = barco
							break
					elif (up not in self.dicc):
						
						barco.source = "../img/DarkBlueCircle.png"
						self.instructions.boardDicc[boat41] = barco
						break
				else:
					boats41Done = True

			if(upLeft in self.dicc):
				buttonUpLeft = self.dicc[upLeft]
				buttonUpLeft.disabled = True
				self.dicc[upLeft] = buttonUpLeft

			if(upRight in self.dicc):
				buttonUpRight = self.dicc[upRight]
				buttonUpRight.disabled = True
				self.dicc[upRight] = buttonUpRight

			if(downLeft in self.dicc):
				buttonDownLeft = self.dicc[downLeft]
				buttonDownLeft.disabled = True
				self.dicc[downLeft] = buttonDownLeft

			if(downRight in self.dicc):
				buttonDownRight = self.dicc[downRight]
				buttonDownRight.disabled = True
				self.dicc[downRight] = buttonDownRight

		else:

			button.background_color = (1,1,1,1)

	
