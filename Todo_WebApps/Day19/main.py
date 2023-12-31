"""

We are starting with Web Apps on Day 19

"""

import streamlit as st
import functions

todos = functions.read_file()


def add_todo():
    new_todo = st.session_state["todo"] + "\n"
    if len(new_todo.strip("\n")) > 0:
        todos.append(new_todo)
        functions.write_file(todos)


def delete_todo(del_todo):
    todo_to_complete = del_todo
    todos.remove(todo_to_complete)
    functions.write_file(todos)


st.title("To do App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        delete_todo(todo)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", key="todo",
              on_change=add_todo)
