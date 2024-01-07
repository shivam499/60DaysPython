import streamlit as st


def read_file(filename='todos.txt'):
    with open(filename, 'r') as file:  # with context manager
        return file.readlines()


def write_file(todo_val, filename='todos.txt'):
    with open(filename, 'w') as file:  # with context manager
        file.writelines(todo_val)


def add_todo(todo):
    todos = read_file()
    new_todo = todo + "\n"
    if len(new_todo.strip("\n")) > 0:
        todos.append(new_todo)
        write_file(todos)
    # else:
    #     st.warning("Todos is empty")


def edit_todo(todo, old_todo):
    todo_to_edit = old_todo
    new_todo = todo+"\n"
    todos = read_file()
    index = todos.index(todo_to_edit)
    todos[index] = new_todo
    write_file(todos)


def delete_todo(todo):
    todo_to_complete = todo
    todos = read_file()
    todos.remove(todo_to_complete)
    write_file(todos)
