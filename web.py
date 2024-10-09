import streamlit as st
import function01

todos = function01.get_todos()

st.set_page_config(layout= "wide")

def add_todo():
    todo = st.session_state['new_todo'] +"\n"
    todos.append(todo)
    function01.write_todos(todos)


st.title("My Todo <b>App</b>")
st.subheader("This is my todo app")
st.write("This app is to increase your Productivity")

st.text_input(label="Enter the Todo:",placeholder= "Add new todo...",
              on_change= add_todo,key="new_todo")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key =todo)
    if  checkbox:
        todos.pop(index)
        function01.write_todos(todos)
        del st.session_state[todo]
        st.rerun()




print("Hello")

st.session_state

