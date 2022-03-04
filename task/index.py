from flask import Flask, jsonify, request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'demo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

# TODO: organize code
# TODO: take care of exceptions
# TODO: add comments


@app.route('/')
def get_index():
    return jsonify({"result": "Welcome"})


@app.route('/tasks')
def get_tasks():
    cursor.execute("SELECT * FROM task")
    columns = cursor.description
    data = cursor.fetchall()

    fields = [f[0] for f in columns]
    results = []

    for t in data:
        dictionary = {}

        for i in range(len(columns)):
            dictionary[fields[i]] = t[i]

        results.append(dictionary)

    return jsonify({"result": results})


@app.route('/tasks', methods=['POST'])
def add_tasks():
    body = request.get_json()
    value = body["name"]

    command = "INSERT INTO `task` (`name`) VALUES ('" + value + "')"
    cursor.execute(command)
    conn.commit()

    cursor.execute("SELECT * FROM task ORDER BY id DESC LIMIT 1")
    columns = cursor.description
    data = cursor.fetchall()
    fields = [f[0] for f in columns]

    dictionary = {}

    for t in data:
        for i in range(len(columns)):
            dictionary[fields[i]] = t[i]

    return jsonify({"result": dictionary}), 201


@app.route('/tasks/<task_id>', methods=['PUT'])
def update_tasks(task_id):
    body = request.get_json()
    value = body["name"]
    status_value = body["status"]

    command = "UPDATE `task` SET `name` = '" + value + "', `status` = '" + str(status_value) + "' WHERE `id` = '" + str(
        task_id) + "'"
    cursor.execute(command)
    conn.commit()

    command_response = "SELECT * FROM task WHERE `id` = '" + str(task_id) + "'"
    cursor.execute(command_response)
    columns = cursor.description
    data = cursor.fetchall()
    fields = [f[0] for f in columns]

    dictionary = {}

    for t in data:
        for i in range(len(columns)):
            dictionary[fields[i]] = t[i]

    return jsonify(dictionary), 200


@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_tasks(task_id):
    command = "DELETE FROM task WHERE `id` = '" + str(task_id) + "'"
    cursor.execute(command)
    conn.commit()

    return '', 200
