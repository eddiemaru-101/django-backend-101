
class TaskCreateRequestDTO:
    def __init__(self,data):
        self.title = data.get('title')
        self.description = data.get('description')
        self.completed = data.get('completed',False)

class TaskResponseDTO:
    def __init__(self):
        self.id = task.id
        self.title = task.title
        self.description = task.description
        self.completed = task.completed

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

    