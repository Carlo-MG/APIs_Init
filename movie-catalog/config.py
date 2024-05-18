
class Config():
    SECRET_KEY = 'hola'
    JWT_SECRET_KEY = 'hola'
    DEBUG = True
    PORT = 4040
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/movile'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
