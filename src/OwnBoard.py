class BaseOwnBoard():
	def __init__(self, **kwargs):
		super(BaseOwnBoard, self).__init__(**kwargs)
		self.matrix = self.initialize()

	def initialize(self):
		return [[0 for x in range(0,10)] for y in range (0,10)]