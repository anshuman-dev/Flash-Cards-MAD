#load value from main Flask config
#Database URI describing the databse connections
class appConfig():
    SQLALCHEMY_DATABASE_URI = "sqlite:///data/database.sqlite3"
    DEBUG = True