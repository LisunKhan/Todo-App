import function
import PySimpleGUI as psg
import time
import os

if not os.path.exists("Files/Todo.txt"):
    with open("Files/Todo.txt", "w") as file:
        pass

psg.theme("Black")
clock = psg.Text('',key="clock")
label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter to-do", key="todo")
add_button = psg.Button("Add")
list_box = psg.Listbox(values=function.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")

window = psg.Window('My ToDo App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            try:
                todos = function.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except TypeError:
                psg.popup("Please enter an item", font=('Helvetica', 20))

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                psg.popup("Please select an item", font=('Helvetica', 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                psg.popup("Please select an item", font=('Helvetica', 20))

        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case psg.WIN_CLOSED:
            break

window.close()
