from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250), nullable=True)


class Team(Base):
    __tablename__ = 'team'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
           'user_id'      : self.user_id
       }
 
class Player(Base):
    __tablename__ = 'player'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    height = Column(Integer)
    weight = Column(Integer)
    team_id = Column(Integer,ForeignKey('team.id'))
    team = relationship(Team)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'height'         : self.height,
           'weight'         : self.weight,
       }



engine = create_engine('sqlite:///teamplayer.db')
 

Base.metadata.create_all(engine)
