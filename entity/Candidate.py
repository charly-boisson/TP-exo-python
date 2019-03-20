import uuid

class Candidate():

    def __init__(self, first_name, last_name, experience):
        self.id = str(uuid.uuid1())
        self.first_name = first_name
        self.last_name = last_name
        self.experience = experience

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "experience": [exp.serialize() for exp in self.experience]
        }
