import Model

class Recruiter(Model):

    __tablename__ = 'recruiters'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    phone = Column(String(30), nullable=True)
    interviews = relationship("Interview")
    positions = relationship("Position")
