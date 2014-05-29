from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty

from kivy.lang import Builder
Builder.load_string(''' 
<Vacio>:
	id: vacioID
	orientation: 'vertical'
	size_hint_x: 0.7	
		
''')

class Vacio(BoxLayout):
	def __init__(self, **kwargs):
		super(Vacio, self).__init__(**kwargs)
		self.add_widget(BoxLayout())

	def getBoatIcons(self):

		box41 = BoxLayout(id="box_4_1")
		img410 = Image(id="4_1_0",source="../img/LightBlueCircle.png")
		box41.add_widget(img410)
		self.add_widget(box41)