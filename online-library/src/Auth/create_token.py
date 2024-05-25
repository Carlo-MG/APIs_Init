from flask_jwt_extended import create_access_token
from flask import jsonify

def create_token(username):
    token = create_access_token(identity=username)
    return jsonify(token=token)