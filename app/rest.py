import pymysql
from app import app
from db import mysql
from flask import jsonify, request


@app.route('/')
def welcome():
    return jsonify({"result": "Welcome"})


@app.route('/tasks')
def get_tasks():
    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM task")

    rows = cursor.fetchall()

    response = jsonify({"result": rows})

    return response, 200


@app.route('/tasks', methods=['POST'])
def add_tasks():
    body = request.get_json()
    value = body["name"]

    command = "INSERT INTO `task` (`name`) VALUES ('" + value + "')"

    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(command)
    conn.commit()

    cursor.execute("SELECT * FROM task ORDER BY id DESC LIMIT 1")

    rows = cursor.fetchall()
    response = jsonify({"result": rows[0]})

    return response, 201


@app.route('/tasks/<task_id>', methods=['PUT'])
def update_tasks(task_id):
    body = request.get_json()
    value = body["name"]
    status_value = body["status"]

    command = "UPDATE `task` SET `name` = '" + value + "', `status` = '" + str(status_value) + "' WHERE `id` = '" + str(
        task_id) + "'"

    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(command)
    conn.commit()

    command_response = "SELECT * FROM task WHERE `id` = '" + str(task_id) + "'"
    cursor.execute(command_response)

    rows = cursor.fetchall()

    response = jsonify(rows[0])

    return response, 200


@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_tasks(task_id):
    command = "DELETE FROM task WHERE `id` = '" + str(task_id) + "'"

    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(command)
    conn.commit()

    return '', 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
