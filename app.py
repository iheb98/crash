from flask import Flask, request, render_template, jsonify
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

users = []
logged_in_users = []

@app.route('/')
def index():
    # Render the 'index.html' template
    return render_template('index.html')

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


@app.route('/signup', methods=['GET'])
def signup():
    email = request.args.get('email')
    username = request.args.get('username')
    password = request.args.get('password')

    # Add the user to the static array
    users.append({"email": email, "username": username, "password": password})

    return jsonify({"message": "User signed up successfully"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if user exists and password is correct
        for user in users:
            if user['username'] == username and user['password'] == password:
                logged_in_users.append(user)
                return jsonify({'message': 'Login successful'})
        
        return jsonify({'message': 'Invalid username or password'})
    
    return render_template('login.html')

@app.route('/users')
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)



