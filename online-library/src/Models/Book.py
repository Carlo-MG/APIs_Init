from src import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60), nullable=False, unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    loans = db.relationship('Loan', backref='book', lazy=True)
    
    def __repr__(self):
        return f'< Book {self.title}>'
    
    