import os
import sys

from flask import Flask, request, jsonify

import data.conn as db

app = Flask(__name__)

@app.route('/posts', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        conn = db.get_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        data = []
        for row in posts:
            data.append(dict(row))

        return jsonify(list(data))

    if request.method == 'POST':
        body = request.get_json()

        print(body)

        conn = db.get_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                        (body['title'], body['content']))
        conn.commit()
        
        post = conn.execute('SELECT * FROM posts ORDER BY id DESC LIMIT 1').fetchone()

        conn.close()
        return jsonify(dict(post))

if __name__ == "__main__":
    current_module = os.path.dirname(os.path.curdir)
    sys.path.append(current_module)

    os.environ['FLASK_APP'] = 'app.py'
    os.environ['FLASK_ENV'] = 'development'

    app.run()