from src.Models import User
from src import db

def create_user(data):
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not username : return {'message': 'username undefined'}
    if not email : return {'message': 'email undefinded'}
    if not password : return {'message': 'password undefined'}
    
    user = User.query.filter_by(username=username).first()
    if user : return {'message': 'nombre de usuario en uso'}
    user = User.query.filter_by(email=email).first()
    if user : return {'message': 'email en uso'}
    
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    
    return {'message': 'OK'}

def login_user(data):
    username = data.get('username')
    password = data.get('password')
    
    if not username : return {'message': 'username sin definir'}
    
    user = User.query.filter_by(username=username).first()
    
    if not user : return {'message': 'username no registrado'}

    user = User.query.filter_by(username=username).filter_by(password=password).first()
    
    if not user : return {'message': 'password invalid'}
    
    return True
    
    
    