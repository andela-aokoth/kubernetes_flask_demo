from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!"


@app.route('/update', methods=['GET'])
def update():
    return "Just Rolled An Update"


@app.route('/another', methods=['GET'])
def another():
    return "This is another update"


if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')
