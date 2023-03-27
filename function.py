def get_todos():
    """ Read to text file and return the list of
    todo items """
    with open("Files/Todo.txt", 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="Files/Todo.txt"):
    """ Write the todo items in the list """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

