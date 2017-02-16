""""The Operations of the todo program"""
import shelve
from os.path import join, expanduser


def get_all():
    """Returns a list of all todos"""
    todo_db = open_db()
    todos = get_todos_from_db(todo_db)
    todo_db.close()
    return [todo for todo in todos]


def add_todo(description):
    """Appends a todo to the todo list and saves it"""
    todo_db = open_db()
    todos = get_todos_from_db(todo_db)
    todos.append({'description': description, 'completed': False})
    todo_db['todos'] = todos
    todo_db.close()


def complete_todo(index):
    """Completes a todo on the given index"""
    todo_db = open_db()
    todos = get_todos_from_db(todo_db)
    todos[index]['completed'] = True
    todo_db['todos'] = todos
    todo_db.close()


def delete_todo(index):
    """Deletes a todo from the list"""
    todo_db = open_db()
    todos = get_todos_from_db(todo_db)
    del todos[index]
    todo_db['todos'] = todos
    todo_db.close()


def get_todos_from_db(todo_db):
    return todo_db['todos'] if todo_db.__contains__('todos') else []


def open_db():
    return shelve.open(join(expanduser('~'), 'todo'), 'c')
