"""Usage:
	myapp.py create_todo <name> <description>
	myapp.py open_todo <name>
	myapp.py delete_todo <name>
	myapp.py add_item <content> <name>
	myapp.py list (todos|items <todo-name>)
	myapp.py quit

Options:
	-h --help         Show this screen
	--version         Show version
commands:
	create_todo
	open_todo
	delete_todo
	add_item
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

if __name__ == '__main__':
	arguments  = docopt(__doc__,  sys.argv[1:], version = 'crollo 1.0.1')

	if arguments['create_todo']:
		mylist = todo_list.ToDoList(arguments['<name>'], arguments['<description>'])
		mylist.save_list()
		cprint('list added', 'green')
		cprint('1st item added by default', 'green')

	if arguments['delete_todo']:
		mylist = todo_list.ToDoList(arguments['<name>'])
		mylist.delete_list()

	if arguments['list'] and arguments['todos']:
		for todo in todo_list.ToDoList('').get_todos():
			print("{0} || {1}:".format(todo[0], todo[1]))
			print('=' * 90)
			for item in todo_item.ToDoItem().get_items(todo[0]):
				if item[1] == 1:
					color = 'green'
				else:
					color = 'red'
				cprint("---------{0}, {1}".format(item[0], item[1]), color)
				print('=' * 90)
	if arguments['list'] and arguments['items']:
		resset = todo_item.ToDoItem().get_items(arguments['<todo-name>'])
		print("list '{0}' todo items:".format(arguments['<todo-name>']))

		for row in resset:
			if row[1] == 0:
				color = 'red'
			else:
				color = 'green'

			cprint("---------'{0}', '{1}'".format(row[0], row[1]), color)

	if arguments['add_item']:
		if todo_list.ToDoList(arguments['<name>']).todo_exists():
			todo_item.ToDoItem(arguments['<content>'], 0).save_item(arguments['<name>'])
			cprint('todo added', 'green')
		else:
			cprint('error specified todo list does not exist', 'red')

	if arguments['open_todo']:
		resset = todo_item.ToDoItem().get_items(arguments['<name>'])
		print("list '{0}' todo items:".format(arguments['<name>']))		
		datalist =[]
		item_no = 0
		for row in resset:
			if row[1] == 0:
				color = 'red'
			else:
				color = 'green'
			datalist.append(row)
			cprint("{0}---------'{1}', '{2}'".format(item_no, row[0], row[1]), color)
			item_no += 1
		while True:
			action = input('"quit" to quit or "finish"/"unfinish" <item-no> to mark as complete/incomplete : ').split(' ')
			if action == '':
				continue
			if action[0] == 'quit':
				print('bye :) ')
				break
			elif action[0] == 'finish':
				todo_item.ToDoItem('').finish_item(datalist[int(list(action)[1])][0], arguments['<name>'], 1)
				cprint('item marked as done', 'green')

			elif action[0] == 'unfinish':
				todo_item.ToDoItem('').finish_item(datalist[int(list(action)[1])][0], arguments['<name>'], 0)
				cprint('item marked as undone', 'green')








