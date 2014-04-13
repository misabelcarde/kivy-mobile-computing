from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.core.window import Window
from kivy.config import Config

from Board import Board

#Builder.load_file('Board.kv')
Builder.load_string('''
<Main>:
	cols: 2

<Board>:
	cols: 11
	rows: 11	

<Instructions>:
	orientation: 'vertical'
	size_hint_x: 0.7
''')


class Main(GridLayout):
	pass

class Instructions(BoxLayout):
	def __init__(self, **kwargs):
		super(Instructions, self).__init__(**kwargs)
		self.text = self.getInstructions('es')

	def getTexts(self):
		instructions = {}
		instructions['numbers'] = [[1,4],[2,3],[3,2],[4,1]]
		instructions['es'] = ['COMO JUGAR','Coloca los barcos en el tablero:\n',[' barco de ',' casillas\n'],
		[' barcos de ',' casillas\n'],[' barcos de ',' casillas\n'],[' barcos de ',' casilla']]

		return instructions

	def getInstructions(self,language):
		texts = self.getTexts() 
		ins = texts[language]
		numbers = texts['numbers']
		
		for i in range(0,len(ins)):
			if i==2:
				textLabel = str(numbers[0][0]) + ins[i][0] + str(numbers[0][1]) + ins[i][1]
				idLabel = str(numbers[0][0]*10 + numbers[0][1])
				self.add_widget(Label(text=textLabel,id=idLabel))

			elif i==3:
				textLabel = str(numbers[1][0]) + ins[i][0] + str(numbers[1][1]) + ins[i][1]
				idLabel = str(numbers[1][0]*10 + numbers[1][1])
				self.add_widget(Label(text=textLabel,id=idLabel))

			elif i==4:
				textLabel = str(numbers[2][0]) + ins[i][0] + str(numbers[2][1]) + ins[i][1]
				idLabel = str(numbers[2][0]*10 + numbers[2][1])
				self.add_widget(Label(text=textLabel,id=idLabel))

			elif i==5:
				textLabel = str(numbers[3][0]) + ins[i][0] + str(numbers[3][1]) + ins[i][1]
				idLabel = str(numbers[3][0]*10 + numbers[3][1])
				self.add_widget(Label(text=textLabel,id=idLabel))

			else:
				self.add_widget(Label(text=ins[i]))
	


class BattleshipApp(App):
	def build(self):
		
		main = Main()
		main.add_widget(Board())
		main.add_widget(Instructions())
		return main

if __name__ == '__main__':
	BattleshipApp().run()


#Quitar las funciones como generateBoard del build