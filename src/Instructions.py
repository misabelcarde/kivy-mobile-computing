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
		
''')

class Instructions(BoxLayout):
	def __init__(self, **kwargs):
		super(Instructions, self).__init__(**kwargs)
		#self.text = self.getInstructions('es')
		self.boardDicc = {}
		self.getBoatIcons()
		self.add_widget(BoxLayout())


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
		
		img140 = Image(id="1_4_0",source="../img/LightBlueMidCircleLeft.png")
		img141 = Image(id="1_4_1",source="../img/LightBlueSquare.png")
		img142 = Image(id="1_4_2",source="../img/LightBlueSquare.png")
		img143 = Image(id="1_4_3",source="../img/LightBlueMidCircleRight.png")
		
		box14.add_widget(img140)
		box14.add_widget(img141)
		box14.add_widget(img142)
		box14.add_widget(img143)
		
		self.boardDicc["1_4_0"] = img140
		self.boardDicc["1_4_1"] = img141
		self.boardDicc["1_4_2"] = img142
		self.boardDicc["1_4_3"] = img143

		#---------------------------------------------------------------------------------#
		box23 = BoxLayout(id="box_2_3")
		box23_0 = BoxLayout(id="box_2_3_0")

		img2300 = Image(id="2_3_0_0",source="../img/LightBlueMidCircleLeft.png")
		img2301 = Image(id="2_3_0_1",source="../img/LightBlueSquare.png")
		img2302 = Image(id="2_3_0_2",source="../img/LightBlueMidCircleRight.png")

		box23_0.add_widget(img2300)
		box23_0.add_widget(img2301)
		box23_0.add_widget(img2302)

		box23_1 = BoxLayout(id="box_2_3_1")

		img2310 = Image(id="2_3_1_0",source="../img/LightBlueMidCircleLeft.png")
		img2311 = Image(id="2_3_1_1",source="../img/LightBlueSquare.png")
		img2312 = Image(id="2_3_1_2",source="../img/LightBlueMidCircleRight.png")

		box23_1.add_widget(img2310)
		box23_1.add_widget(img2311)
		box23_1.add_widget(img2312)

		box23.add_widget(box23_0)
		box23.add_widget(box23_1)

		self.boardDicc["2_3_0_0"] = img2300
		self.boardDicc["2_3_0_1"] = img2301
		self.boardDicc["2_3_0_2"] = img2302
		self.boardDicc["2_3_1_0"] = img2310
		self.boardDicc["2_3_1_1"] = img2311
		self.boardDicc["2_3_1_2"] = img2312
		#---------------------------------------------------------------------------------#
		box32 = BoxLayout(id="box_3_2")
		box32_0 = BoxLayout(id="box_3_2_0")

		img3200 = Image(id="3_2_0_0",source="../img/LightBlueMidCircleLeft.png")
		img3201 = Image(id="3_2_0_1",source="../img/LightBlueMidCircleRight.png")
		img3210 = Image(id="3_2_1_0",source="../img/LightBlueMidCircleLeft.png")
		img3211 = Image(id="3_2_1_1",source="../img/LightBlueMidCircleRight.png")
		img3220 = Image(id="3_2_2_0",source="../img/LightBlueMidCircleLeft.png")
		img3221 = Image(id="3_2_2_1",source="../img/LightBlueMidCircleRight.png")


		box32_0.add_widget(img3200)
		box32_0.add_widget(img3201)

		box32_1 = BoxLayout(id="box_3_2_1")
		box32_1.add_widget(img3210)
		box32_1.add_widget(img3211)

		box32_2 = BoxLayout(id="box_3_2_2")
		box32_2.add_widget(img3220)
		box32_2.add_widget(img3221)

		box32.add_widget(box32_0)
		box32.add_widget(box32_1)
		box32.add_widget(box32_2)

		self.boardDicc["3_2_0_0"] = img3200
		self.boardDicc["3_2_0_1"] = img3201
		self.boardDicc["3_2_1_0"] = img3210
		self.boardDicc["3_2_1_1"] = img3211
		self.boardDicc["3_2_2_0"] = img3220
		self.boardDicc["3_2_2_1"] = img3221
		

		#---------------------------------------------------------------------------------#
		

		box41 = BoxLayout(id="box_4_1")
		box41_0 = BoxLayout(id="box_4_1_0")

		img410 = Image(id="4_1_0",source="../img/LightBlueCircle.png")
		img411 = Image(id="4_1_1",source="../img/LightBlueCircle.png")
		img412 = Image(id="4_1_2",source="../img/LightBlueCircle.png")
		img413 = Image(id="4_1_3",source="../img/LightBlueCircle.png")

		box41_0.add_widget(img410)

		box41_1 = BoxLayout(id="box_4_1_1")
		box41_1.add_widget(img411)

		box41_2 = BoxLayout(id="box_4_1_2")
		box41_2.add_widget(img412)

		box41_3 = BoxLayout(id="box_4_1_3")
		box41_3.add_widget(img413)
		
		box41.add_widget(box41_0)
		box41.add_widget(box41_1)
		box41.add_widget(box41_2)
		box41.add_widget(box41_3)

		self.boardDicc["4_1_0"] = img410
		self.boardDicc["4_1_1"] = img411
		self.boardDicc["4_1_2"] = img412
		self.boardDicc["4_1_3"] = img413
		#---------------------------------------------------------------------------------#
		self.add_widget(box14)
		self.add_widget(box23)
		self.add_widget(box32)
		self.add_widget(box41)
