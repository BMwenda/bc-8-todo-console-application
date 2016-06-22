import todo_item
import sqlite3
class ToDoItem(object):
	"""docstring for ToDoItem"""
	def __init__(self, content = '1st item', complete = 0, *args):
		if type(content) != type(''):
			self.content = 'Invalid content'
		else:
			self.content = content
			
		if type(complete) != type(1):
			self.complete = 0
		else:
			self.complete = complete
		self.args = args

	def save_item(self, listname):
		conn = sqlite3.connect('crollodb.db')
		c = conn.cursor()
		SQL = "INSERT INTO todoitem (CONTENT, COMPLETE, LISTNAME) VALUES ('{0}', '{1}', '{2}')"
		c.execute(SQL.format(self.content, self.complete, listname))
		conn.commit()
		conn.close()

	def delete_item(self, listname):
		conn = sqlite3.connect('crollodb.db')
		c = conn.cursor()
		SQL = "DELETE FROM todoitem WHERE CONTENT = '{0}' AND LISTNAME = '{1}'".format(self.content, listname)
		c.execute(SQL)
		conn.commit()
		conn.close()

		