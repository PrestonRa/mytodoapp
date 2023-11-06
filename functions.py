#from functions import get_todos, write_todos
#import functions

""" We use import function here to keep our code clean
and we can reuse our unique codes in other projects.
We connect the codes from "function" using:
"functions.code" such as functions.get_todos()
"""

FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
"""This is a doc string, this is my practice app to 
learn how to use simple python functions. Above is a 
unique function we made that finds and pulls up our .txt
file so we can make a to do list.
"""

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
"""We don't need to return the write_todos function
because it does not need to be called upon/shown
or "returned". It simply is altering the file that was
returned.
"""

if __name__ == "__main__":
    print("hello")
    """We use __name__ == "__main__ when we want
    the function to run in the original .py file
    but not in another .py file where we are using
    the other functions."""