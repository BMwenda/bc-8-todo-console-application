class ToDoItem(object):
	"""docstring for ToDoItem"""
	def __init__(self, content, complete = False, *args):
		self.content = content
		self.complete = complete
		self.args = args
		