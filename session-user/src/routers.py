from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.controller import create_user, login_by_username
from src.auth import generarToken

endpoints = Blueprint('endpoints', __name__)

@endpoints.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    res = create_user(data)
    
    if res['message'] == 'OK':
        return jsonify(res), 201
    return jsonify(res), 409

@endpoints.route('/login/username', methods=['POST'])
def login_by_username_route():
    if not request.is_json:
        return jsonify({'message': 'no json'}), 400

    data = request.get_json()
    res = login_by_username(data)
    
    if res != True:
        return jsonify(res), 409

    return generarToken(data.get('username')), 200

# Ejemplo de una ruta protegida con JWT
@endpoints.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200