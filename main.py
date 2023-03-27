import function
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("Time is ", now)


while True:

    user_action = input("Tpye add,show,edit,complete,exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = function.get_todos()

        todos.append(todo + '\n')

        function.write_todos(todos)

    elif user_action.startswith('show'):
        todos = function.get_todos()

        """#no_space_todos = []
        #for items in todos:
           #new_items = items.strip("\n")
           #no_space_todos.append(new_items)
        #no_space_todos = [item.strip('\n') for item in todos]"""

        for index, item in enumerate(todos):
            item = item.strip('\n')
            new_todo = f"{index + 1}.{item}"
            print(new_todo)

    elif user_action.startswith('edit'):
        try:
            index_number = int(user_action[5:])
            print(index_number)
            index_number = index_number-1

            todos = function.get_todos()

            replaced_by = input("New value:")

            todos[index_number] = replaced_by + '\n'

            function.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            task = int(user_action[9:])

            todos = function.get_todos()

            index = task-1
            todo_to_remove = todos[index]
            todos.pop(index)

            function.write_todos(todos)

            message = f"Todo {todo_to_remove}was removed"
            print(message)
        except ValueError:
            print("Enter correct index")
            continue
        except IndexError:
            print("There in no item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is invalid")

print('Bye!!')





