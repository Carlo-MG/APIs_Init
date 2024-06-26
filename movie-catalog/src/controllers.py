from flask import jsonify
from src.models import Movile
from src import db

def add_movile(data):
    name = data.get('name')
    desc = data.get('desc')
    
    if not name and not desc: return {'message': 'Error'}
    
    movile = Movile(name=name, description=desc)
    
    db.session.add(movile)
    db.session.commit()
    
    return {'message': 'OK'}


def list_Movile():
    data = Movile.query.all()
    
    return [item.to_dict() for item in data]

