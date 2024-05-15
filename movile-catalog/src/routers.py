from flask import Blueprint, jsonify, request
from src.controllers import add_movile, list_Movile

routers = Blueprint('routers', __name__)

@routers.route('/movile', methods=['POST'])
def createMovile():
    data = request.get_json()
    
    res = add_movile(data)
    
    if res['message'] == 'OK':
        return jsonify(res), 201
    return jsonify(res), 409

@routers.route('/movile', methods=['GET'])
def listMovile():
    return jsonify(list_Movile()), 200