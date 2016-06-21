import todo_item
class ToDoList(object):
	def __init__(self, name, description, todo_items):
		if type(name) != type(''):
			self.name = 'Enter valid name'
		else:
			self.name = name
		if type(description) != type(''):
			self.description = 'Enter valid description'
		else:
			self.description = description
		self.todo_items = todo_items

	def add_todo(self, content, complete = False, *args):
		if type(complete) != type(True):
			self.complete = False
			return
		if type(content) != type(''):
			return 'Enter valid content'
		item = todo_item.ToDoItem(content, complete, *args)
		self.todo_items.append(item)

	def finish_item(self, index):
		if index >= len(self.todo_items) or index < 0:
			return 'That to do item does not exist'
		self.todo_items[index] = True

	def edit_item(self, index, content):
		self.todo_items[index] = content

	def delete_item(self, index):
		del self.todo_items[index]

	def percentage_completed(self):
		completed_items = 0
		for item in self.todo_items:
			if item.complete:
				completed_items += 1
		percentage = 100 * (completed_items/len(self.todo_items))
		return percentage
