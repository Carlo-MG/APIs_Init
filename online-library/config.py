class Config():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask_library'
    SQLALCHEMY_TRACK_MODIFICATIONS = False