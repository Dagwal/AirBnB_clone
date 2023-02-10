from datetime import datetime
import uuid
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
    def __str__(self):
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
    def save(self):
        self.updated_at = datetime.now().isoformat()
    def to_dict(self):
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

