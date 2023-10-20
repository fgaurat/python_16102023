import os
import sys
from Todo import Todo
from TodoDAO import TodoDAO

def main():
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
