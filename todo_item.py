class ToDoItem(object):
	"""docstring for ToDoItem"""
	def __init__(self, content, complete = False, *args):
		self.content = content
		if type(complete) != type(True):
			self.complete = False
		else:
			self.complete = complete
		self.args = args
		