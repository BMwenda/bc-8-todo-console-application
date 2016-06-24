# bc-8-todo-console-application
Andela bootcamp 'TO DO' python console application
A simple command line application that stores data in an Sqlite3 database
See usage below:


# Crollo To Do Console Application
A Python console application for organizing of to do lists with various to do items.

## Installation
Clone the repo from GitHub:
```
git clone https://github.com/davidnjakai/bc-8-todo-console-application.git
```

Navigate to the root folder:
```
cd bc-8-todo-console-application
```

Install the required packages:
```
pip install -r requirements.txt
```

## Usage
1. ```myapp.py create_todo <name> <description>``` Create a named todo list along with a description. Example: ``` create_todo 'bootcamp project' 'list of items to check on when working on project' ```

2. ```myapp.py open_todo <name>``` Open a predefined todo list. From here you are able to mark list items as finished or unfinished. Example: ```myapp.py open_todo "bootcamp project"```

3. ```myapp.py delete_todo <name>```Delete a named to do list along with its list items. Example: ```myapp.py delete "bootcamp project"```

4. ```myapp.py add_item <content> <name>``` Load a list item to a specified list with the specified contents. Example: ```myapp.py add_item "Ensure virutal environment is set up for console application development" "bootcamp project"

5. ```list (todos|items <todo-name>)``` Display a list of to do lists along with their items or print items from a selected to do list. Example: ```list todos``` or ```list items "bootcamp project"

## Testing
To test, run the ```tests.py``` file.

## Credits

[David Njakai](https://github.com/davidnjakai)