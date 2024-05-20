from src import db

class Author(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    books = db.relationship('Book', backref='author', lazy=True)
    
    def __repr__(self):
        return f'<Author {self.name}>'    
    