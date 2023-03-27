import function
import PySimpleGUI as psg

label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter to-do", key="todo")
add_button = psg.Button("Add")

window = psg.Window('My ToDo App',
                    layout=[[label], [input_box, add_button]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
        case psg.WIN_CLOSED:
            break



window.close()
