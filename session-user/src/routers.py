from src.controller import create_user, login_by_username
from flask import Blueprint, request, jsonify

endpointers = Blueprint('routers', __name__)

@endpointers.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    res = create_user(data)
    
    if res['message'] == 'OK':
        return jsonify(res), 201
    return jsonify(res), 409

@endpointers.route('/login/username', methods=['POST'])
def loginByUsername():
    data = request.get_json()
    
    res = login_by_username(data)
    
    if res['message'] == 'OK': return jsonify(res), 200
    return jsonify(res), 409

