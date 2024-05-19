from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.Service.servive_post import craete_post

BP_post = Blueprint('post', __name__)

@BP_post.route('/post', methods=['POST'])
@jwt_required()
def CreatePost():
    
    if not request.is_json : return {'message': 'no json'}
    
    data = request.get_json()
    curret_user = get_jwt_identity()
    
    res = craete_post(data, curret_user)
    
    if res['message'] == 'OK': return jsonify(res), 201
    return jsonify(res), 409
    