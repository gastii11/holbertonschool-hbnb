from app.models.base import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.places = []  # lugares que usan este amenity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or len(value) > 50:
            raise ValueError("Amenity name is required and must not exceed 50 characters")
        self._name = value
