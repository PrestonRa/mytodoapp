"""run it in the terminal (streamlit run web.py)
stop it in the terminal with (ctrl c)
create requirement file (pip freeze > requirements.txt"""
import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] +'\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title("Let's Make a List")
st.subheader("This Will Help You!")
st.write("Enter what you need to do in the box below.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()

st.text_input(label="My List", placeholder="Add an item to the list...",
              on_change=add_todo, key='new_todo')
