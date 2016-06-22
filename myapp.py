"""Usage:
	myapp.py create_todo <name> [ --desc=description]
	myapp.py open_todo <name>
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
border = colored("*" * 5, 'red').center(80)



class Interactive (cmd.Cmd):

	cprint(figlet_format('CROLLO APPLICATION'), 'red', attrs=['bold'])

	def introduction():
		print(border)
		print(spacer)
		print("WELCOME TO CROLLO!".center(70))
		print(spacer)
		print("TO DO LIST CREATING CONSOLE APPLICATION:".center(70))
		print(spacer)
		print("1. create_todo <name> [ --desc=description]".center(70))
		print("2. add_item <content> [--completed=complete]".center(70))
		print("3. open_todo <name>".center(70))
		print("4. finish_item (<number>|<content>)".center(70))
		print("5. list (todos|items (<todo-name>|<todo-id>))".center(70))
		print(spacer)
		print("OTHER COMMANDS:".center(70))
		print(spacer)
		print("1. help".center(70))
		print("2. quit".center(70))
		print(spacer)
		print(border)


	intro = introduction()
	prompt = "(crollo) "

	def do_quit(self, args):
		exit()


# def handle(argsdict):
#     if 'interactive' in argsdict:
#     	Interactive().cmdloop()

if __name__ == '__main__':
    arguments  = docopt(__doc__,  sys.argv[1:], version = 'myapp 1.0.1')
    Interactive().cmdloop()
