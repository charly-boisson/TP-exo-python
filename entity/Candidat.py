import uuid

class Candidat:

    def __init__(self, id, first_name, last_name, experience):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.experience = experience

    def serialize:
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'experience': self.experience,
        }
