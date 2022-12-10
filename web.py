from flask import Flask, render_template, abort, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    BASE_DIR = './static/ss'

    abs_path = os.path.join(BASE_DIR)

    if not os.path.exists(abs_path):
        return abort(404)

    if os.path.isfile(abs_path):
        return send_file(abs_path)

    files = os.listdir(abs_path)
    print(files)
    return render_template('index.html', files=files)


if __name__ == '__main__':
    app.run(debug = True)
