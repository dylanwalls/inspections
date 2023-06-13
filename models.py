from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean

db = SQLAlchemy()

class Inspection(db.Model):
    __tablename__ = "inspection"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
    consent = Column(Boolean)
    comments = Column(String)
    image = Column(String)
    signature = Column(String)