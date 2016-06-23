"""Usage:
	myapp.py create_todo <name> <description>
	myapp.py open_todo <name>
	myapp.py delete_todo <name>
	myapp.py add_item <content> [--completed=complete]
	myapp.py finish_item (<number>|<content>)
	myapp.py list (todos|items <todo-name>)
	myapp.py (-i | --interactive)
	myapp.py quit

Options:
	-h --help		Show this screen
	-v --version	Show version
	-i --interactive  Interactive Mode
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
import sqlite3
import todo_item
import todo_list
from colorama import init
spacer = " "
border = colored("*" * 5, 'red')

def introduction():
	os.system('clear')
	cprint(figlet_format('CROLLO APPLICATION'), 'red', attrs = ['bold'])
	print(border)
	print(spacer)
	print("WELCOME TO CROLLO!")
	print(spacer)
	print("TO DO LIST CREATING CONSOLE APPLICATION:")
	print(spacer)
	print("1. create_todo <name> <description>")
	print("2. add_item <content> [--completed=complete]")
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


class Interactive (cmd.Cmd):

	intro = introduction()
	prompt = "(crollo)"
	def emptyline(self):
		introduction()

	def do_quit(self, args):
		exit()

	def do_create_todo(self, arguments):
		argslist = arguments.split(' ')
		mylist = todo_list.ToDoList(argslist[0], argslist[1])
		mylist.save_list()
		cprint('new list and a default item added', 'green')

	def do_delete_todo(self, arguments):
		argslist = arguments.split(' ')
		mylist = todo_list.ToDoList(argslist[0])
		mylist.delete_list()
		cprint('list and its items deleted', 'green')

if __name__ == '__main__':
	arguments  = docopt(__doc__,  sys.argv[1:], version = 'myapp 1.0.1')
	if arguments['--interactive']:
		Interactive().cmdloop()

	if arguments['create_todo']:
		mylist = todo_list.ToDoList(arguments['<name>'], arguments['<description>'])
		mylist.save_list()
		cprint('list added', 'green')
		cprint('1st item added by default', 'green')

	if arguments['delete_todo']:
		conn = sqlite3.connect('crollodb.db')
		c = conn.cursor()
		SQL = "SELECT * FROM TODOLIST WHERE name = '{0}'".format(arguments['<name>'])
		resset = c.execute(SQL)
		if resset == 0:
			print('no to do list going by that name')
		else:
			c.execute("DELETE FROM TODOLIST WHERE name = '{0}';".format(arguments['<name>']))
			c.execute("DELETE FROM TODOITEM WHERE listname = '{0}';".format(arguments['<name>']))
		cprint('list and its items deleted', 'green')
		conn.commit()
		conn.close()

	if arguments['list'] and arguments['todos']:
		conn = sqlite3.connect('crollodb.db')
		c = conn.cursor()
		SQL = "SELECT NAME, DESCRIPTION FROM TODOLIST"
		for todo in c.execute(SQL):
			print("{0}, {1}".format(todo[0], todo[1]))
			SQL2 = "SELECT CONTENT, COMPLETE FROM TODOITEM WHERE listname = '{0}'".format(todo[0])
			c2 = conn.cursor()
			for item in c2.execute(SQL2):
				cprint("---------{0}, {1}".format(item[0], item[1]), 'red')
		conn.close()

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


