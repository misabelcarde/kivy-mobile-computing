from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

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
		super(Board, self).__init__(**kwargs)
		self.generateBoard()

	def generateBoard(self):
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

	
	def putBoat(self, button):
		if button.background_color == [1,1,1,1]:
			button.background_color = (1,0.65,0,1)
		else:
			button.background_color = (1,1,1,1)
