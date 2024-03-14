from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db_users = {
    "John": "Miami",
    "David": "Miami",
    "Jane": "London",
    "Gabriella": "Paris",
    "Tanaka": "Tokyo"
}

users = []
logged_in_users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    result = ''
    args = request.args
    name = args.get('name')
    location = args.get('location')

    if None not in (name, location):
        result = {key: value for key, value in db_users.items() if key == name and value == location}
    elif name is not None:
        result = {key: value for key, value in db_users.items() if key == name}
    elif location is not None:
        result = {key: value for key, value in db_users.items() if value == location}

    return jsonify(result)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    users.append({'email': email, 'username': username, 'password': password})
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    for user in users:
        if user['username'] == username and user['password'] == password:
            logged_in_users.append(user)
            return jsonify({'message': 'Login successful'})

    return jsonify({'message': 'Invalid username or password'})

@app.route('/users')
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
