"""Usage:
	myapp.py create_todo <name> <description>
	myapp.py open_todo <name>
	myapp.py delete_todo <name>
	myapp.py add_item <content> [--completed=complete]
	myapp.py finish_item (<number>|<content>)
	myapp.py list (todos|items (<todo-name>|<todo-id>))
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
import sys
import cmd
from termcolor import cprint, colored
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit
import todo_item
import todo_list
#from db.database import Database
from colorama import init
#init(strip=not sys.stdout.isatty())
spacer = " "
border = colored("*" * 5, 'red')



class Interactive (cmd.Cmd):

	cprint(figlet_format('CROLLO APPLICATION'), 'red', attrs=['bold'])

	def introduction():
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
		print("5. list (todos|items (<todo-name>|<todo-id>))")
		print(spacer)
		print("OTHER COMMANDS:")
		print(spacer)
		print("1. help")
		print("2. quit")
		print(spacer)
		print(border)


	intro = introduction()
	prompt = "(crollo)"

	def do_quit(self, args):
		exit()


# def handle(argsdict):
#     if 'interactive' in argsdict:
#     	Interactive().cmdloop()

if __name__ == '__main__':
	arguments  = docopt(__doc__,  sys.argv[1:], version = 'myapp 1.0.1')
	print(arguments)
	if arguments['--interactive']:
		Interactive().cmdloop()

	if arguments['create_todo']:
		mylist = todo_list.ToDoList(arguments['<name>'], arguments['<description>'])
