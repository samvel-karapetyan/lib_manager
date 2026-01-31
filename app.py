import streamlit as st
from src.manager import LibraryManager

manager = LibraryManager()

st.title("Library Manager")
command = st.radio("Հրամանի անուն", ["add", "search", "remove"])

if command == "add":
    title = st.text_input("Title")
    
    col1, col2, col3 = st.columns(3)

    publication_year = col1.number_input("Publication Year", value=2025, step=1)
    author = col2.text_input("Author")
    genre = col3.text_input("Genre")

    pressed_add = st.button("Add")

    if pressed_add:
        manager.add(title=title, publication_year=publication_year, author=author, genre=genre)
        manager.exit() # exit -> save
elif command == "remove":
    pass