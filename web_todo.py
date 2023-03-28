import streamlit as st
import function

todos = function.get_todos()
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("this app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo", placeholder="Add todo...")
