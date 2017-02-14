"""todo main application"""

import argparse
from tabulate import tabulate
from .todo import add_todo, delete_todo, complete_todo, get_all

def execute():
    """executes the todo program"""
    parser = argparse.ArgumentParser(description="A TODO command line app")
    parser.add_argument("-a", help="Add a todo to the list", type=str, metavar='Description')
    parser.add_argument("-d", help="Delete a todo from the list", type=int, metavar='ID')
    parser.add_argument("-c", help="Complete a todo from the list", type=int, metavar='ID')

    args = parser.parse_args()

    if args.a is not None:
        add_todo(args.a)

    if args.d is not None:
        delete_todo(args.d)

    if args.c is not None:
        complete_todo(args.c)

    todo_list = [[values for values in todos.values()] for todos in get_all()]
    print(tabulate(todo_list, headers=['ID', 'Completed', 'Description'], showindex="always"))
