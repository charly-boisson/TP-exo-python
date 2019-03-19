import uuid

class Project:

    def __init__(self, id, name, start_date, end_date, description):
        self.id = str(uuid.uuid4())
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description

    def serialize:
        return {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'description': self.description,
        }
