from flask import Flask
from flask.templating import render_template

from storage import table

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_vars', methods=['POST'])
def get_vars():
    return table.extract()

if __name__ == '__main__':
    app.run()
