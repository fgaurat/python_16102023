import os
import sys
from pprint import pprint
from Todo import Todo
from TodoDAO import TodoDAO
import requests

def main():
    dao = TodoDAO("todos_db.db")

    # resp = requests.get('https://jsonplaceholder.typicode.com/todos')
    # todos = resp.json()
    # pprint(todos)
    # print(todos[0]['title'])
    # for todo in todos:
    #     t = Todo(**todo)
    #     dao.save(t)
    # todos = dao.find_all() # list de Todo
    todos = dao.find_all()
    for todo in todos:
        print(todo.id,todo.title) # "Faire encore du Python"    

def main_01():
    print(os.cpu_count())
    print(os.getcwd())
    # t = Todo(1,1,"Faire du Python")
    # print(t)
    # sys.exit(1)
    
    dao = TodoDAO("./ch10/todos_db.db")
    todos = dao.find_all() # list de Todo

    for todo in todos:
        print(todo.id,todo.title)

    t = Todo(userId=12,title="Faire encore du Python",completed=False)
    dao.save(t)

    todos = dao.find_all() # list de Todo
    for todo in todos:
        print(todo.id,todo.title) # "Faire encore du Python"

    t = dao.find_by_id(3)
    print(t)

if __name__ == '__main__':
    main()
