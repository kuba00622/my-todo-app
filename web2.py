import streamlit as st
import functions

todos = functions.get_todos()
def add_new():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''

st.title("My todo App")
st.subheader('This is my todo APP')
st.write("Hello")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f'{index}{todo}')
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f'{index}{todo}']
        st.experimental_rerun()


a = st.text_input(label="", placeholder="Add new todo",
              on_change=add_new, key='new_todo')


st.session_state
