from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(30), index=True, unique=False)
    
    def __repr__(self) -> str:
        return f'< User {self.username} >'
    
    def to_dict(self):
        return {'id': self.id, 'username': self.username, 'email': self.email}