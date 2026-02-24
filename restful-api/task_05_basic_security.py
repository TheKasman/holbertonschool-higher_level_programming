#!/usr/bin/python3
"""The most basic of security"""
from flask import jsonify, request, Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)
#  why aren't we learning the secure way to do this?
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

auth = HTTPBasicAuth()

# Mock user database
users = {
    "admin": {
        "password": generate_password_hash("adminpass"),
        "role": "admin"
    },
    "user": {
        "password": generate_password_hash("userpass"),
        "role": "user"
    }
}


#  Basic auth
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username),
                                                 password):
        return username
    return None


# Basic af
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted"), 200


#  JWT time
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username in users and check_password_hash(users[username]["password"],
                                                 password):
        access_token = create_access_token(
            identity={"username": username, "role": users[username]["role"]})
        return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad credentials"}), 401


# JWT-protected route for any user
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted"), 200


#  Admin
@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200


if __name__ == "__main__":
    app.run()
