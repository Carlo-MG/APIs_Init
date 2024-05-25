from flask import Blueprint, request, jsonify
from src.Service.Service_User import Create_user, Login_user
from src.Auth.create_token import create_token

BP_user = Blueprint('user', __name__)

@BP_user.route('/user', methods=['POST'])
def user_register():
    if not request.is_json : return jsonify(
        {'message': 'el formato no esta en json'}
    )
    data = request.get_json()
    res = Create_user(data)
    
    if res['message'] == 'OK' : return jsonify(res), 201
    return jsonify(res), 409

@BP_user.route('/user/login', methods=['POST'])
def login_user():
    if not request.is_json : {'message': 'formatodo no valido'}
    data = request.get_json()
    
    res = Login_user(data)
    
    if not res['message'] == 'OK': return jsonify(res), 409
    
    return create_token(data.get('username'))
    
    

