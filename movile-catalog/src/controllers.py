from src.models import Movile
from src import db

def add_movile(data):
    name = data.get('name')
    desc = data.get('desc')
    
    if not name and not desc: return {'message': 'Error'}
    
    movile = Movile.query.filter_by(name=name).all()
    
    if movile : return {'message': 'Nombre no disponible'}
    
    movile = Movile(name=name, description=desc)
    
    db.session.add(movile)
    db.session.commit()
    
    return {'message': 'OK'}


def list_Movile():
    data = Movile.query.all()
    
    return [item.to_dict() for item in data]

def movile_by_name(name):
    movile = Movile.query.filter_by(name=name).all()
    if not movile : return {'message': 'Pelicula no encontrada'}
    
    return [ mov.to_dict() for mov in movile]


def update_by_desc(data):
    id = data.get('id')
    desc = data.get('desc')
    movile = Movile.query.get(id)
    
    if not movile : return {'message': 'undefined'}
    
    movile.description = desc
    
    db.session.commit()
    
    return {'message': 'OK'}

def update_by_name(data):
    id = data.get('id')
    name = data.get('name')
    
    movile = Movile.query.get(id)
    
    if not movile : return {'message': 'undefined'}
    
    movile.name = name
    
    db.session.commit()
    return {'message': 'OK'}

def delete_by_id(id):
    movile = Movile.query.get(id)
    
    if not movile : return {'message': 'undefined'}
    db.session.delete(movile)
    db.session.commit()
    return {'message': 'OK'}
    
def delete_by_name(name):
    movile = Movile.query.filter_by(name=name).all()
    
    if not movile: return {'message': 'undefined'}
    
    db.session.delete(movile[0])
    
    db.session.commit()
    
    return {'message': 'OK'}