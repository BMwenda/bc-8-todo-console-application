from database import conn2, c2

class ToDoItem(object):
	"""docstring for ToDoItem"""
	def __init__(self, content = '1st item', complete = 0):
		self.content = content
		self.complete = complete

	def save_item(self, listname):
		SQL = "INSERT INTO todoitem (CONTENT, COMPLETE, LISTNAME) VALUES ('{0}', '{1}', '{2}')"\
		.format(self.content, self.complete, listname)
		c2.execute(SQL)
		conn2.commit()

	def delete_item(self, listname):
		SQL = "DELETE FROM todoitem WHERE CONTENT = '{0}' AND LISTNAME = '{1}'".format(self.content, listname)
		c2.execute(SQL)
		conn2.commit()

	def delete_all(self, listname):
		SQL = "DELETE FROM todoitem WHERE LISTNAME = '{0}'".format(listname)
		c2.execute(SQL)
		conn2.commit()

	def get_items(self, listname):
		SQL = "SELECT CONTENT, COMPLETE FROM todoitem WHERE LISTNAME = '{0}'".format(listname)
		return c2.execute(SQL)

	def edit_item(self, content):
		self.content = content

	def finish_item(self, content, listname, num):
		self.complete = 1
		SQL = "UPDATE todoitem SET COMPLETE = {0} WHERE CONTENT = '{1}' AND LISTNAME = '{2}'".format(num, content, listname);
		c2.execute(SQL)
		conn2.commit()
