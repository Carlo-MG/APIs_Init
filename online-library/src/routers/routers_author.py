from flask import Blueprint, request, jsonify
from src.Service.Service_author import create_autor, get_author_by_name

BP_Author = Blueprint('author', __name__)


@BP_Author.route('/author', methods=['POST'])
def register_author():
    if not request.is_json : {'message': 'formato no valido'}

    data = request.get_json()
    res = create_autor(data)
    
    if res['message'] == 'OK' : return jsonify(res), 201
    return jsonify(res), 409

@BP_Author.route('/author/<name>', methods=['GET'])
def get_author(name):
    res = get_author_by_name(name)
    
    if res['error'] == 'OK' : return jsonify(res), 409
    return jsonify(res), 200

