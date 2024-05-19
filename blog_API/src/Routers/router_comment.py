from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.Service.service_comment import addComment

BP_comment = Blueprint('comment', __name__)


@BP_comment.route('/comment/<int:post_id>', methods=['POST'])
@jwt_required()
def add_comment(post_id):
    
    if not request.is_json : return {'message': 'not json'}
    
    data = request.get_json()
    current_name = get_jwt_identity()
    
    res = addComment(data, post_id, current_name)
    
    if res['message'] == 'OK' : return jsonify(res), 201
    return jsonify(res), 409
