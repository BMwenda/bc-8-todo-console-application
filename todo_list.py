import todo_item
class ToDoList(object):
	def __init__(self, name, description, todo_items):
		self.name = name
		self.description = description
		self.todo_items = todo_items

	def add_todo(self, content, complete = False, *args):
		todo_item = todo_item(content, complete, *args)
		self.todo_items.append(todo_item)

	def finish_item(self, index):
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
