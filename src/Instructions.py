from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty

from kivy.lang import Builder
Builder.load_string(''' 
<Instructions>:
	id: instructionsID
	orientation: 'vertical'
	size_hint_x: 0.7

<Continue>:
	anchor_x: 'center'
	anchor_y: 'center'

	Button:
		id: 'continueButton'
		name: 'continueButton'
		text: 'Continue'
		size_hint_x: 0.5
		size_hint_y: 0.5
		
''')
#on_press: root.manager.current = 'secondBoard'

class Instructions(BoxLayout):
	def __init__(self, **kwargs):
		super(Instructions, self).__init__(**kwargs)
		#self.text = self.getInstructions('es')
		self.getBoatIcons()
		self.add_widget(Continue())

	# def getTexts(self):
	# 	instructions = {}
	# 	instructions['numbers'] = [[1,4],[2,3],[3,2],[4,1]]
	# 	instructions['es'] = ['COMO JUGAR','Coloca los barcos en el tablero:\n',[' barco de ',' casillas\n'],
	# 	[' barcos de ',' casillas\n'],[' barcos de ',' casillas\n'],[' barcos de ',' casilla']]

	# 	return instructions

	# def getInstructions(self,language):
	# 	texts = self.getTexts() 
	# 	ins = texts[language]
	# 	numbers = texts['numbers']
		
	# 	for i in range(0,len(ins)):
	# 		if i==2:
	# 			textLabel = str(numbers[0][0]) + ins[i][0] + str(numbers[0][1]) + ins[i][1]
	# 			idLabel = str(numbers[0][0]*10 + numbers[0][1])
	# 			self.add_widget(Label(text=textLabel,id=idLabel))

	# 		elif i==3:
	# 			textLabel = str(numbers[1][0]) + ins[i][0] + str(numbers[1][1]) + ins[i][1]
	# 			idLabel = str(numbers[1][0]*10 + numbers[1][1])
	# 			self.add_widget(Label(text=textLabel,id=idLabel))

	# 		elif i==4:
	# 			textLabel = str(numbers[2][0]) + ins[i][0] + str(numbers[2][1]) + ins[i][1]
	# 			idLabel = str(numbers[2][0]*10 + numbers[2][1])
	# 			self.add_widget(Label(text=textLabel,id=idLabel))

	# 		elif i==5:
	# 			textLabel = str(numbers[3][0]) + ins[i][0] + str(numbers[3][1]) + ins[i][1]
	# 			idLabel = str(numbers[3][0]*10 + numbers[3][1])
	# 			self.add_widget(Label(text=textLabel,id=idLabel))

	# 		else:
	# 			self.add_widget(Label(text=ins[i]))
	def getBoatIcons(self):
		box14 = BoxLayout(id="box_1_4")
		box14.add_widget(Image(id="1_4_0",source="../img/LightBlueMidCircleLeft.png"))
		box14.add_widget(Image(id="1_4_1",source="../img/LightBlueSquare.png"))
		box14.add_widget(Image(id="1_4_2",source="../img/LightBlueSquare.png"))
		box14.add_widget(Image(id="1_4_3",source="../img/LightBlueMidCircleRight.png"))
		#---------------------------------------------------------------------------------#
		box23 = BoxLayout(id="box_2_3")
		box23_0 = BoxLayout(id="box_2_3_0")
		box23_0.add_widget(Image(id="2_3_0_0",source="../img/LightBlueMidCircleLeft.png"))
		box23_0.add_widget(Image(id="2_3_0_1",source="../img/LightBlueSquare.png"))
		box23_0.add_widget(Image(id="2_3_0_2",source="../img/LightBlueMidCircleRight.png"))

		box23_1 = BoxLayout(id="box_2_3_1")
		box23_1.add_widget(Image(id="2_3_1_0",source="../img/LightBlueMidCircleLeft.png"))
		box23_1.add_widget(Image(id="2_3_1_1",source="../img/LightBlueSquare.png"))
		box23_1.add_widget(Image(id="2_3_1_2",source="../img/LightBlueMidCircleRight.png"))
		
		box23.add_widget(box23_0)
		box23.add_widget(box23_1)
		#---------------------------------------------------------------------------------#
		box32 = BoxLayout(id="box_3_2")
		box32_0 = BoxLayout(id="box_3_2_0")
		box32_0.add_widget(Image(id="3_2_0_0",source="../img/LightBlueMidCircleLeft.png"))
		box32_0.add_widget(Image(id="3_2_0_1",source="../img/LightBlueMidCircleRight.png"))

		box32_1 = BoxLayout(id="box_3_2_1")
		box32_1.add_widget(Image(id="3_2_1_0",source="../img/LightBlueMidCircleLeft.png"))
		box32_1.add_widget(Image(id="3_2_1_1",source="../img/LightBlueMidCircleRight.png"))

		box32_2 = BoxLayout(id="box_3_2_2")
		box32_2.add_widget(Image(id="3_2_2_0",source="../img/LightBlueMidCircleLeft.png"))
		box32_2.add_widget(Image(id="3_2_2_1",source="../img/LightBlueMidCircleRight.png"))

		box32.add_widget(box32_0)
		box32.add_widget(box32_1)
		box32.add_widget(box32_2)
		#---------------------------------------------------------------------------------#
		box41 = BoxLayout(id="box_4_1")
		box41_0 = BoxLayout(id="box_4_1_0")
		box41_0.add_widget(Image(id="4_1_0",source="../img/LightBlueCircle.png"))

		box41_1 = BoxLayout(id="box_4_1_1")
		box41_1.add_widget(Image(id="4_1_1",source="../img/LightBlueCircle.png"))

		box41_2 = BoxLayout(id="box_4_1_2")
		box41_2.add_widget(Image(id="4_1_2",source="../img/LightBlueCircle.png"))

		box41_3 = BoxLayout(id="box_4_1_3")
		box41_3.add_widget(Image(id="4_1_3",source="../img/LightBlueCircle.png"))
		
		box41.add_widget(box41_0)
		box41.add_widget(box41_1)
		box41.add_widget(box41_2)
		box41.add_widget(box41_3)
		#---------------------------------------------------------------------------------#
		self.add_widget(box14)
		self.add_widget(box23)
		self.add_widget(box32)
		self.add_widget(box41)

	#show when all boats are in the board
class Continue(AnchorLayout):
	pass
		