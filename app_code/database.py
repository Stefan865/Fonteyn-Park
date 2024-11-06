import os
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

engine =  create_engine('sqlite:///guests.db')
Session = sessionmaker(bind = engine)
session = Session() 
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()



def set_password(password):
# Generate and set the hashed password
    hashed_pass = generate_password_hash(password)
    return hashed_pass

def check_password(hashed_pass,password):
    return check_password_hash(hashed_pass, password)
class Database:

    def GetSecretKey(self):
        secret_key = os.environ.get('SECRET_KEY')
        return secret_key
    
class Guest(Base, UserMixin):
    __tablename__ = 'Guest'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    arrival_date = Column(Date, nullable=False)
    departure_date = Column(Date, nullable=False)
    num_of_people = Column(Integer, nullable=False)
    room_1 = Column(Integer, nullable=False)
    room_2 = Column(Integer, nullable=False)
    password = Column(String(200), nullable=False)

#Base.metadata.create_all(engine)