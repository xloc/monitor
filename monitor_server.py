from flask import Flask, jsonify
from flask.templating import render_template

from storage import table

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('play.html', toc=table.extract_toc())


@app.route('/get_vars', methods=['GET', 'POST'])
def get_vars():
    return jsonify(table.exchange_data())

if __name__ == '__main__':
    app.run()
