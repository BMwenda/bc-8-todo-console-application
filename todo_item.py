from database import conn, c

class ToDoItem(object):
	"""docstring for ToDoItem"""
	def __init__(self, content = '1st item', complete = 0):
		self.content = content
		self.complete = complete

	def save_item(self, listname):
		SQL = "INSERT INTO todoitem (CONTENT, COMPLETE, LISTNAME) VALUES ('{0}', '{1}', '{2}')"
		c.execute(SQL.format(self.content, self.complete, listname))
		conn.commit()

	def delete_item(self, listname):
		SQL = "DELETE FROM todoitem WHERE CONTENT = '{0}' AND LISTNAME = '{1}'".format(self.content, listname)
		c.execute(SQL)
		conn.commit()

	def get_items(self, listname):
		SQL = "SELECT CONTENT, COMPLETE FROM todoitem WHERE LISTNAME = '{0}'".format(self.listname)
		return c.execute(SQL)

	def edit_item(self, content):
		self.content = content

	def finish_item(self):
		self.complete = 1
		