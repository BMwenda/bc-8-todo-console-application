import unittest
import todo_list
import todo_item

class TodoTests(unittest.TestCase):
	def test_todo_list_instantiation(self):
		test_list = todo_list.ToDoList()
		self.assertEqual(type(todo_list.ToDoList('My List', 'A list containing test to do items', [todo_item.ToDoItem('to do item 1')])), type(test_list))

	def test_todo_item_instantiation(self):
		test_item = todo_item.ToDoItem()
		self.assertEqual(type(todo_item.ToDoItem()), type(test_item))

	def test_todo_list_with_non_string_name(self):
		test_list = todo_list.ToDoList(12, 'A list containing test to do items', ['to do item 1', 'to do item 2'])
		self.assertEqual(test_list.name, 'Enter valid name')

	def test_todo_list_with_non_string_description(self):
		test_list = todo_list.ToDoList('My List', 22, ['to do item 1', 'to do item 2'])
		self.assertEqual(test_list.description, 'Enter valid description')

	def test_todo_list_items_attribute_type(self):
		test_list = todo_list.ToDoList('My List', 'A list containing test to do items', [todo_item.ToDoItem()])
		self.assertEqual(type(test_list.todo_items), type(todo_item.ToDoItem))

	def test_adding_of_item_with_none_string_content(self):
		test_list = todo_list.ToDoList('My List', 'A list containing test to do items', [todo_item.ToDoItem()])
		test_list.add_todo(23)
		self.assertEqual(test_list.todo_items[-1], 'Enter valid content')

	def test_adding_of_item_with_non_boolean_complete(self):
		test_list = todo_list.ToDoList('My List', 'A list containing test to do items', [todo_item.ToDoItem()])
		test_list.add_todo('Test to do item', 23)
		self.assertEqual(test_list.todo_items[-1].complete, False)

	def test_finish_item_out_of_range_index(self):
		test_list = todo_list.ToDoList('My List', 'A list containing test to do items', [todo_item.ToDoItem('to do item 1')])
		(test_list.finish_item(5), 'That to do item does not exist')
