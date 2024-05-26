from src.Models import Author
from src import db

def create_autor(data):
    name = data.get('name')
    
    author = Author.query.filter_by(name=name).first()
    
    if author : return {'message': 'Nombre en uso', 'error': 'OK'}
    
    author = Author(name=name)
    
    db.session.add(author)
    db.session.commit()
    
    return {'message': 'OK'}

def get_author_by_name(name):
    author = Author.query.filter_by(name=name).first()
    
    if not author : {'message': 'Author undefined', 'error': 'OK'}
    
    return {'name':author.get_obj(), 'error': 'NO'}
    