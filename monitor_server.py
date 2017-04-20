from flask import Flask, jsonify
from flask.templating import render_template

from storage import table

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_vars', methods=['GET', 'POST'])
def get_vars():
    print 'called'
    return jsonify(table.extract())

if __name__ == '__main__':
    app.run()
