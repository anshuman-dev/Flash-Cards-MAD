#Importing the dataitems for SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

#pool of connections available for use whenever application needs to talk to database? Look for it.
engine = None

#construct base class for declarative class definitions
base = declarative_base()
db = SQLAlchemy()