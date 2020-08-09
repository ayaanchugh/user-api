import json
from flask import Flask, jsonify
import sqlite3


app = Flask(__name__)


@app.route("/users")
def get_users():
    # con = sqlite3.connect('myusers.db')
    # # sql_table(con)
    #
    # cursorObj = con.cursor()
    # cursorObj.execute("SELECT * FROM users")
    # rows = cursorObj.fetchall()
    # users = []
    # for row in rows:
    #     users.append({'id': row[0], 'name':row[1]})
    #
    # return json.dumps(users)
    return jsonify(hello="world")


if __name__=="__main__":
    app.run(debug=True, host='127.0.0.1')
