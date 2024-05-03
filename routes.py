from flask import Flask, jsonify
app = Flask(__name__)

@app.routes("/users", methods=["GET"])
def get_users():
    users = seasssion.query(User).all()
    return jsonify([user.name for user in users])