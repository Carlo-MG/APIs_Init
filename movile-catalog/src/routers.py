from flask import Blueprint, jsonify, request
from src.controllers import add_movile, list_Movile, movile_by_name, update_by_desc, update_by_name, delete_by_id, delete_by_name

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

@routers.route('/movile/<name>')
def by_name(name):
    return jsonify(movile_by_name(name)), 200


@routers.route('/movile/desc', methods=['PUT'])
def update_desc():
    data = request.get_json()
    
    res = update_by_desc(data)
    
    if res['message'] == 'OK':
        return jsonify(res), 201
    return jsonify(res), 409

@routers.route('/movile/name', methods=['PUT'])
def update_name():
    data = request.get_json()
    
    res = update_by_name(data)
    
    if res['message'] == 'OK': return jsonify(res), 201
    return jsonify(res), 409

@routers.route('/movile/id/<id>', methods=['DELETE'])
def delete_movile(id):
    res = delete_by_id(id)
    
    if res['message'] == 'OK': return jsonify({'message': 'peliculta eliminada'}), 200
    return jsonify(res),409

@routers.route('/movile/name/<name>', methods=['DELETE'])
def delete_name(name):
    res = delete_by_name(name)
    
    if res['message'] == 'OK': return jsonify(res), 200
    return jsonify(res), 409