from src import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(60), index=True, unique=False)
    
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self) -> str:
        return f'< User {self.username} >'
