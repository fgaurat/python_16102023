import json

def main_write():
    # f= open("hello.txt",'w')
    with open("hello.txt", 'w') as f:
        for i in range(20):
            # f.write("")
            print(f"Ligne {i:02}", file=f)


def main_read():
    with open("hello.txt", 'r') as f:
        # read+splitlines
        # content = f.read()
        # lines =content.splitlines()
        # print(lines)
        # lines = [f.readlines()]

        # readlines
        # lines = [line.strip() for line in f.readlines()]
        # print(lines)

        for line in f:
            print(line.strip())


def main_write_json():
    todos = [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        },
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": False
        },
        {
            "userId": 1,
            "id": 3,
            "title": "fugiat veniam minus",
            "completed": False
        },
        {
            "userId": 1,
            "id": 4,
            "title": "et porro tempora",
            "completed": True
        },
        {
            "userId": 1,
            "id": 5,
            "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
            "completed": False
        }
    ]


    for todo in todos:
        print(f"{todo['title']} {todo['completed']}")

    with open("todos.json","w") as f:
        json.dump(todos,f,indent=4)


def main():
    with open("todos.json") as f: # lecture par défaut
        todos = json.load(f)
        print(todos[0])




if __name__ == '__main__':
    main()
