"""

We are starting with Web Apps on Day 19

"""

import streamlit as st
import functions as fn

todos = fn.read_file()

st.title("To do App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        fn.delete_todo(todo)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", key="new_todo",
              on_change=fn.add_todo)
