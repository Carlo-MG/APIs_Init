from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False, unique=False)
    
    loans = db.relationship('Loan', back_populates='user', lazy=True)
    
    def __repr__(self) -> str:
        return f'<User {self.username}>'
