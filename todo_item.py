class ToDoItem(object):
	"""docstring for ToDoItem"""
	def __init__(self, content, complete = False, *args):
		if type(content) != type(''):
			self.content = 'Invalid content'
		else:
			self.content = content
			
		if type(complete) != type(True):
			self.complete = False
		else:
			self.complete = complete
		self.args = args
		