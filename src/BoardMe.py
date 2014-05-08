from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.lang import Builder
Builder.load_string(''' 
<BoardMe>:
	id: boardMeID
	cols: 11
	rows: 11
''')

#TODO
class BoardMe(GridLayout):
	'''Generation of the board and functions for complete it'''
	def __init__(self, **kwargs):
		super(BoardMe, self).__init__(**kwargs)
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
		 		button.disabled = True
		 		self.add_widget(button)

	
	
