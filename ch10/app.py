from flask import Flask,render_template
from Todo import Todo
from TodoDAO import TodoDAO

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/ugly")
def index_ugly():
    dao = TodoDAO("todos_db.db")
    html = ""

    for todo in dao.find_all():
        html += f"""
<tr>
<td>{todo.id}</td>
<td>{todo.userId}</td>
<td>{todo.title}</td>
<td>{todo.completed}</td>
</tr>"""
    html = "<table>"+html+"</table>"

    return html

@app.route("/")
def index():
    dao = TodoDAO("todos_db.db")
    todos = list(dao.find_all())
    return render_template("list_todos.html",the_todos=todos)
