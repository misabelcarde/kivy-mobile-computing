from kivy.uix.gridlayout import GridLayout

from kivy.lang import Builder
Builder.load_string('''
<BaseOwnBoard>:
	id: baseOwnBoardID
	cols: 2
''')


class BaseOwnBoard(GridLayout):
	def __init__(self, **kwargs):
		super(BaseOwnBoard, self).__init__(**kwargs)
		self.matrix = self.initialize()

	def initialize(self):
		return [[0 for x in range(0,10)] for y in range (0,10)]

	def getMatrix(self):
		return self.matrix

	def setMatrix(self,newMatrix):
		self.matrix = newMatrix