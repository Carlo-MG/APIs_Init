from src import db 

class Movile (db.Model):
    id_movile = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(60), index=True, unique=True)
    description = db.Column(db.String(200), index=True, unique=False)
    
    def __repr__(self):
        return f'< Movile {self.name} >'
