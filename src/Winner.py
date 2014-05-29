from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty


from kivy.lang import Builder
Builder.load_string(''' 
<Winner>:
	id: winnerID
	orientation: 'vertical'
	size_hint_x: 0.7	
		
''')

class Winner(BoxLayout):
	def __init__(self, **kwargs):
		super(Winner, self).__init__(**kwargs)
		self.boardDicc = {}
		self.getBoatIcons()
		self.add_widget(BoxLayout())

	
	def getBoatIcons(self):

		box = BoxLayout(id="box_1_4")
		img = Image(source="../img/winner.png")
		box.add_widget(img)
		self.add_widget(box)
