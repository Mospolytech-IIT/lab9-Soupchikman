from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='posts')

if __name__ == "__main__":
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)
