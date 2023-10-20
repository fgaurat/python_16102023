import sqlite3
from dataclasses import astuple
from Todo import Todo

class TodoDAO:


    def __init__(self,db_file) -> None:
        self.__con = sqlite3.connect(db_file)

    def find_all(self):# list de Todo
        todos = []
        cur = self.__con.cursor()
        res = cur.execute("SELECT id,userId,title,completed FROM todos_tbl")
        for result in res.fetchall():
            t = Todo(*result)
            todos.append(t)
        return todos

    def find_by_id(self,id):
        cur = self.__con.cursor()
        res = cur.execute("SELECT id,userId,title,completed FROM todos_tbl WHERE id=?",(id,))
        t = res.fetchone()
        todo = Todo(*t)
        return todo

    def save(self,todo:Todo):
        cur = self.__con.cursor()
        
        sql = "INSERT INTO todos_tbl(userId,title,completed) VALUES(?,?,?)"
        # t = (todo.userId,todo.title,todo.completed)
        # cur.execute(sql,t)
        cur.execute(sql,astuple(todo)[1:])
        self.__con.commit()

    def __del__(self):
        self.__con.close()
