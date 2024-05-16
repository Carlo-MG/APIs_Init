from src.controller import create_user
from flask import Blueprint, request, jsonify

endpointers = Blueprint('routers', __name__)

@endpointers.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    res = create_user(data)
    
    if res['message'] == 'OK':
        return jsonify(res), 201
    return jsonify(res), 409

