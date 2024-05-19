from flask import Blueprint, request, jsonify
from src.Service.service_user import create_user, login_user
from src.Auth.Token import generar_token

blueP = Blueprint('user', __name__)

@blueP.route('/registre', methods=['POST'])
def registrer():
    
    if not request.is_json : return jsonify({'message': 'data not json'})
    
    data = request.get_json()
    
    res = create_user(data)
    
    if res['message'] == 'OK': return jsonify(res), 201
    return jsonify(res), 409

@blueP.route('/login', methods=['POST'])
def login():
    
    if not request.is_json : return jsonify({'message':'no json'})
    
    data = request.get_json()
    res = login_user(data)
    
    if res != True: return jsonify(res),401
    
    return generar_token(data.get('username')), 200