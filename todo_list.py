import todo_item
import sqlite3


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
		self.save_list()


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

	def save_list(self):
		conn = sqlite3.connect('crollodb.db')
		c = conn.cursor()
		SQL = "INSERT INTO todolist (NAME, DESCRIPTION) VALUES ('{0}', '{1}')"
		c.execute(SQL.format(self.name, self.description))
		conn.commit()
		conn.close()

	def delete_list(self):
		conn = sqlite3.connect('crollodb.db')
		c = conn.cursor()
		if len(self.todo_items) > 0:
			for item in self.todo_items:
				SQL = "DELETE FROM todoitem WHERE CONTENT = {0}".format(item)
				c.execute(SQL)
			SQL = "DELETE FROM todolist WHERE NAME = {0}".format(self.name)
		conn.commit()
		conn.close()
