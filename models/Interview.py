import Model

class Interview(Model):

    __tablename__ = 'interviews'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    date = Column(Date, nullable=True)
    feedback = Column(String(200), nullable=True)
    position = Column(String(200), nullable=True)
    recruiter = relationship("Recruiter")
    candidate = relationship("Candidate")
