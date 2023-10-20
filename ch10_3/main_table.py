import sys
import sqlite3
from tkinter import *
from tkinter import ttk
from TodoDAO import TodoDAO
from Todo import Todo

def main():
    dao = TodoDAO("todos_db.db")
    todos = dao.find_all()

    ws = Tk()
    ws.title('TodoList')
    ws.geometry('800x600')
    ws['bg']='#fb0'

    tv = ttk.Treeview(ws,show="headings")
    tv['columns']=('Id', 'Title', 'Completed')
    
    tv.column('Id',  anchor=CENTER,stretch=NO)
    tv.column('Title', anchor=CENTER, width=80)
    tv.column('Completed', anchor=CENTER, width=80)

    tv.heading('Id', text='Id', anchor=CENTER)
    tv.heading('Title', text='Title', anchor=CENTER)
    tv.heading('Completed', text='Completed', anchor=CENTER)
    
    for todo in todos:
        tv.insert(parent='', index=todo.id, iid=todo.id, text='', values=(todo.id,todo.title,todo.completed))
    
    tv.pack(fill=BOTH,expand=True)

    ws.mainloop()

if __name__=='__main__':
    main()