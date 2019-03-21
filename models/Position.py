from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Models.Model import Model

class Position(Model):

    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    name = Column(String(200), nullable=True)
    description = Column(String(200), nullable=True)
    tech_skills = Column(String(200), nullable=True)
    feedback = Column(String(200), nullable=True)
    years_of_experience = Column(Integer, nullable=True)
    salary = Column(Integer, nullable=True)
    clients = Column(Integer, ForeignKey('clients.id'))
    recruters = Column(Integer, ForeignKey('recruters.id'))
    interviews = relationship("Interview")
