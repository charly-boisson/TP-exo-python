from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Models.Model import Model

class Interview(Model):

    __tablename__ = 'interviews'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    date = Column(Date, nullable=True)
    feedback = Column(String(200), nullable=True)
    position = Column(Integer, ForeignKey('positions.id'))
    recruiter = Column(Integer, ForeignKey('recruiters.id'))
    candidate = Column(Integer, ForeignKey('candidates.id'))
