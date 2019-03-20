import Model

class Client(Model):

    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    name = Column(String(200), nullable=True)
    phone = Column(String(30), nullable=True)
    email = Column(String(200), nullable=True)
    positions = relationship("Position")
