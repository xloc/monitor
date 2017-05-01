from flask import Flask, jsonify, request
from flask.templating import render_template

from storage import table

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('play.html', toc=table.extract_toc())


@app.route('/get_vars', methods=['GET', 'POST'])
def get_vars():
    return jsonify(table.get_supervised())


@app.route('/set_var')
def set_var():
    name = request.args.get('name')
    value = request.args.get('value')
    result = table.set_controlled(name, value)
    return jsonify(dict(result=result))

if __name__ == '__main__':
    app.run()
