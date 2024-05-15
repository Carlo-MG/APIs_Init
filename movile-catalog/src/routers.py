from flask import Blueprint, jsonify, request
from src.controllers import add_movile

routers = Blueprint('routers', __name__)

@routers.route('/movile', methods=['POST'])
def createMovile():
    data = request.get_json()
    
    res = add_movile(data)
    
    if res['message'] == 'OK':
        return jsonify(res), 201
    return jsonify(res), 409
