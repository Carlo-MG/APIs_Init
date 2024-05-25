from src.Models import User
from src import db

def Create_user(data):
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    if user : return {'message': 'Nombre de usuario en uso', 'error':True}
    
    user = User(username=username, password=password)
    
    db.session.add(user)
    db.session.commit()
    return {'message': 'OK'}


