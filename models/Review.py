import Model

class Review(Model):

    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    review_date = Column(Date, nullable=True)
    content = Column(String(200), nullable=True)
    reviewer = Column(String(200), nullable=True)
    candidate = relationship("Candidate")
