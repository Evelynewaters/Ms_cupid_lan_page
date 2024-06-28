# Ms_cupid_lan.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    # Add code to handle the email, like saving it to a database
    return jsonify({"message": "Thank you for signing up!"})

if __name__ == '__main__':
    app.run(debug=True)
