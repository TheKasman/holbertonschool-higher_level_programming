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


@app.route("/")
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())


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


#  Any user
@app.route("/protected")
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user)


#  Admin
@app.route("/admin")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"msg": "Admins only"}), 403
    return jsonify({"msg": f"Welcome, {current_user['username']}!"})


if __name__ == "__main__":
    app.run()
