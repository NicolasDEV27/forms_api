from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class User(Base):

    __tablename__ = "Users"

    DNI = Column(Integer, primary_key=True)
    Name = Column(String)
    Last_names = Column(String)
    Age = Column(Integer)
    Height = Column(Float)
    Birthday = Column (String)
    email = Column(String, unique=True)
    password = Column(String)
    