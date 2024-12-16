from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base

class TM(Base):
    __tablename__ = 'Tms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(Integer, unique= True, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, unique= True, nullable=False)
    


Students = relationship("Students",back_populates = 'Tms')

def __repr__(self):
    return f'<TM(id={self.id}, name={self.name}, age={self.age}, phone={self.phone}, address={self.address}, email={self.email})>'


class Students(Base):
    __tablename__ = 'Students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(Integer, unique= True, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    tm_id = Column(Integer, ForeignKey('Tms.id'))

