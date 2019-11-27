from flask import Flask, jsonify
from flask_cors import CORS

all_all_all_one = {
    'pm':60,
    'jf':34,
    'lh':45,
    'wt':50,
    'zt':43
}

app = Flask(__name__)


@app.route('/getdata')
def hello_world():
    return jsonify({'data': '3234'})


if (__name__) == '__main__':
    CORS(app, supports_credentials=True)
    app.run(debug=True)
