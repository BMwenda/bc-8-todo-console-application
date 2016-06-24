import todo_item
from database import conn, c

class ToDoList(object):
	def __init__(self, name, description = 'A generic to do list', todo_items = [todo_item.ToDoItem()]):
		self.name = name
		self.description = description
		self.todo_items = todo_items

	def add_todo(self, content, complete = 0):
		item = todo_item.ToDoItem(content, complete)
		self.todo_items.append(item)

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
		for item in self.todo_items:
			item.save_item(self.name)
		SQL = "INSERT INTO todolist (NAME, DESCRIPTION) VALUES ('{0}', '{1}')"
		c.execute(SQL.format(self.name, self.description))
		conn.commit()

	def delete_list(self):
		SQL = "DELETE FROM todolist WHERE NAME = '{0}'".format(self.name)
		todo_item.ToDoItem('').delete_all(self.name)
		c.execute(SQL)
		conn.commit()

	def get_todos(self):
		SQL = "SELECT NAME, DESCRIPTION FROM todolist"
		return c.execute(SQL)

	def todo_exists(self):
		SQL = "SELECT NAME, DESCRIPTION FROM todolist WHERE NAME = '{0}'".format(self.name)
		if len(c.execute(SQL).fetchall()) > 0:
			return True
		return False