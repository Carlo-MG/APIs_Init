
class Config():
    DEBUG = True
    PORT = 4040
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/movile'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'hola'
