import streamlit as st
from TodoDAO import TodoDAO

def main():
    st.set_page_config(layout="wide")
    dao = TodoDAO("todos_db.db")
    st.write("# Hello")
    title = st.text_input('Movie title', 'Life of Brian')
    
    todos = dao.find_all() # generator
    
    if st.button('Submit'):
        st.write('Why hello there')    
        st.write('The current movie title is', title)


    st.table(data=todos)
    


if __name__ == '__main__':
    main()
