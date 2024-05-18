from src.models import User
from src import db

def create_user(data):
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username:
        return {'message': 'username undefined'}
    if not email:
        return {'message': 'email undefined'}
    if not password:
        return {'message': 'password undefined'}

    if User.query.filter_by(username=username).first():
        return {'message': 'nombre de usuario en uso'}
    if User.query.filter_by(email=email).first():
        return {'message': 'correo en uso'}

    user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return {'message': 'OK'}

def login_by_username(data):
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user:
        return {'message': 'usuario sin registrar'}

    if user.password != password:
        return {'message': 'Contraseña incorrecta'}

    return True
