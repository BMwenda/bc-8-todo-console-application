"""Usage:
	myapp.py create_todo <name> <description>
	myapp.py open_todo <name>
	myapp.py delete_todo <name>
	myapp.py add_item <content> <name>
	myapp.py finish_item (<number>|<content>)
	myapp.py list (todos|items <todo-name>)
	myapp.py quit

Options:
	-h --help         Show this screen
	--version         Show version
commands:
	create
	open
	add
	finish
	list
	quit
"""
import os
import sys
import cmd
from termcolor import cprint, colored
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit
import todo_item
import todo_list

spacer = " "
border = colored("*" * 5, 'red')

def introduction():
	os.system('clear')
	print(colored("*" * 167, 'red').center(100))
	cprint(figlet_format('CROLLO APPLICATION'), 'red', attrs = ['bold'])
	print(colored("*" * 167, 'red').center(100))
	print(border)
	print(spacer)
	print("WELCOME TO CROLLO!")
	print(spacer)
	print("TO DO LIST CREATING CONSOLE APPLICATION:")
	print(spacer)
	print("1. create_todo <name> <description>")
	print("2. add_item <content> <name>")
	print("3. open_todo <name>")
	print("4. finish_item (<number>|<content>)")
	print("5. list (todos|items <todo-name>)")
	print("6. delete_todo <name>")
	print(spacer)
	print("OTHER COMMANDS:")
	print(spacer)
	print("1. help")
	print("2. quit")
	print(spacer)
	print(border)

if __name__ == '__main__':
	arguments  = docopt(__doc__,  sys.argv[1:], version = 'myapp 1.0.1')

	if arguments['create_todo']:
		mylist = todo_list.ToDoList(arguments['<name>'], arguments['<description>'])
		mylist.save_list()
		cprint('list added', 'green')
		cprint('1st item added by default', 'green')

	if arguments['delete_todo']:
		mylist = todo_list.ToDoList(arguments['<name>'])
		mylist.delete_list()

	if arguments['list'] and arguments['todos']:
		for todo in todo_list.ToDoList().get_todos():
			print("{0}, {1}".format(todo[0], todo[1]))

			for item in todo_item.ToDoItem().get_items:
				cprint("---------{0}, {1}".format(item[0], item[1]), 'red')

	if arguments['list'] and arguments['items']:
		conn = sqlite3.connect('crollodb.db')
		c = conn.cursor()
		SQL = "SELECT content, complete, listname FROM TODOITEM WHERE listname = '{0}'".format(arguments['<todo-name>'])
		resset = c.execute(SQL)
		print("list '{0}' todo items:".format(arguments['<todo-name>']))

		for row in resset:
			if row[1] == 0:
				color = 'red'

			else:
				color = 'green'
			cprint("---------'{0}', '{1}', '{2}'".format(row[0], row[1], row[2]), color)
		conn.close()

	if arguments['add_item']:
		SQL = "INSERT INTO todoitem (CONTENT, COMPLETE, LISTNAME) VALUES ('{0}', 0, '{1}')".format(arguments['<content>'], arguments['<name>'])
		conn = sqlite3.connect('crollodb.db')
		c = conn.cursor()
		c.execute(SQL)
		conn.commit()
		conn.close()
		cprint('todo added', 'green')




