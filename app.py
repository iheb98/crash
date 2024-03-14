from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


db_users = {
    "John" : "Miami",
    "David" : "Miami",
    "Jane" : "London",
    "Gabriella" : "Paris",
    "Tanaka" : "Tokyo"
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/search', methods=['GET'])
def search():
    result = ''
    args = request.args
    name = args.get('name')
    location = args.get('location')

    # result = db_users
    if None not in (name, location):
        result = {key: value for key, value in db_users.items() if key == name and value == location}
    elif name is not None:
        result = {key: value for key, value in db_users.items() if key == name}
    elif location is not None:
        result = {key: value for key, value in db_users.items() if value == location}

    return result

if __name__ == '__main__':
    app.run(debug=True)



