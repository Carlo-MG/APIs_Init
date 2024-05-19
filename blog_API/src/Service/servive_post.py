from src.Models import Post, User
from src import db

def craete_post(data, username):
    user = User.query.filter_by(username=username).first()
    
    if not user : return {'message': 'user not found'}
    
    title = data.get('title')
    context = data.get('context')
    
    new_post = Post(title=title, context=context, author=user)
    
    db.session.add(new_post)
    db.session.commit()
    
    return {'message': 'OK'}