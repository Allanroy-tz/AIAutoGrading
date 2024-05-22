from flask import Flask, jsonify
import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

from AI import AutoGrading
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'POST':
        a = request.get_data()
        student = json.loads(a)
        result = AutoGrading(student)
        return result
    else:
        return '<只接受post请求！'


if __name__ == '__main__':
    app.run(debug=True)
