from src.Models import User, Post, Comment
from src import db

def addComment(data, id_post, username):
    
    user = User.query.filter_by(username=username).first()
    
    if not user : return {'message': 'user not found'}
    
    post = Post.query.get(id_post)
    
    if not post : return {'message': 'post not found'}
    
    title = data.get('title')
    context = data.get('context')
    
    new_comment = Comment(title=title, context=context, post_id=post.id, user_id=user.id)

    db.session.add(new_comment)
    db.session.commit()
    
    return {'message': 'OK'}
    