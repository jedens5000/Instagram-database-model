import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'Person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'Address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship('Person')

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_id = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')

class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True)
    likes = Column(String(250), nullable=False)
    favorites = Column(String(250), nullable=False)
    image = Column(String(250), nullable=False)
    comments = Column(String(250), nullable=False)
    # image_id = Column(Integer, ForeignKey('image.id'))
    # image = relationship(Post)
    comments_id = Column(Integer, ForeignKey('comments.id'))
    comments = relationship('Comments')
    # likes_id = Column(Integer, ForeignKey('likes.id'))
    # likes = relationship(Likes)

class Comment(Base):
    __tablename__ = "Comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')

class Follower(Base):
    __tablename__ = "Follower"
    id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e