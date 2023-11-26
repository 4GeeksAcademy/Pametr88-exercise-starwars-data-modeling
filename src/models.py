import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    gender = Column(String(100))
    height = Column(String(100))
    mass = Column(String(100))
    skin_color = Column(String(100))
    hair_color = Column(String(100))
    eye_color = Column(String(100))
    
class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    diameter = Column(String(100))
    climate = Column(String(100))
    terrain = Column(String(100))
    population = Column(String(100))
    rotation_period = Column(String(100))
    orbital_period = Column(String(100))

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    director = Column(String(100))
    producer = Column(String(100))
    release_date = Column(String(100))
    created = Column(String(100))
    
class Species(Base):
    __tablename__ = 'species'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    classification = Column(String(100))
    designation = Column(String(100))
    language = Column(String(100))
    skin_colors = Column(String(100))
    hair_colors = Column(String(100))
    eye_colors = Column(String(100))

class Favorities(Base):
    __tablename__ = 'favorities'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    chararcter_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    films_id = Column(Integer, ForeignKey('films.id'))
    films = relationship(Films)
    species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship(Species)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
