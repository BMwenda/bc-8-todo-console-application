import todo_item
import sqlite3


class ToDoList(object):
	def __init__(self, name, description, todo_items = [todo_item.ToDoItem()]):
		if type(name) != type(''):
			self.name = 'Enter valid name'
		else:
			self.name = name
		if type(description) != type(''):
			self.description = 'Enter valid description'
		else:
			self.description = description
		self.todo_items = todo_items

	def add_todo(self, content, complete = 0, *args):
		if type(complete) != type(1):
			self.complete = 0
			return
		if type(content) != type(''):
			return 'Enter valid content'
		item = todo_item.ToDoItem(content, complete, *args)
		self.todo_items.append(item)

	def finish_item(self, index):
		if index >= len(self.todo_items) or index < 0:
			return 'That to do item does not exist'
		self.todo_items[index].complete = 1
		conn = sqlite3.connect('crollodb.db')
		c = conn.cursor()
		SQL = "UPDATE todoitem SET COMPLETE = 1 WHERE LISTNAME = '{0}' AND CONTENT = '{1}'"
		c.execute(SQL.format(self.name, self.todo_items[index].content))
		conn.commit()
		conn.close()

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
		for item in self.todo_items:
			item.save_item(self.name)
		SQL = "INSERT INTO todolist (NAME, DESCRIPTION) VALUES ('{0}', '{1}')"
		c.execute(SQL.format(self.name, self.description))
		conn.commit()
		conn.close()

	def delete_list(self):
		conn = sqlite3.connect('crollodb.db')
		c = conn.cursor()
		if len(self.todo_items) > 0:
			for item in self.todo_items:
				item.delete_item(self.name)
		SQL = "DELETE FROM todolist WHERE NAME = '{0}'".format(self.name)
		c.execute(SQL)
		conn.commit()
		conn.close()