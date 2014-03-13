from kivy.uix.accordion import Accordion, AccordionItem
from kivy.app import App
from kivy.lang import Builder

Builder.load_string('''
<MyAccordion>:
	orientation: 'vertical'
	AccordionItem:
		title: 'Vista 1'
		Label:
			text: 'First tab content area'
	
	AccordionItem:
		title: 'Vista 2'
		BoxLayout:
			orientation: 'horizontal'
			Label:
				text: 'Second tab content area'
			Button:
				text: 'Button that does nothing'

	AccordionItem:
		title: 'Vista 3'
		RstDocument:
			text: '\\n'.join(("Hello world", "-----------", "You are in the third tab."))
''')
class MyAccordion(Accordion):
	pass

class TestApp(App):
	def build(self):
		return MyAccordion()

if __name__ == '__main__':
	TestApp().run()