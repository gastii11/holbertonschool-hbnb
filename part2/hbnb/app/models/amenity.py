from app.models.basemodel import BaseModel
from app.models.place import Place

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

    def add_place(self, place):
        """
        Agrega un Place al Amenity.
        - Valida tipo.
        - Evita duplicados.
        - Mantiene relación doble: agrega el Amenity al Place.amenity
        """
        if not isinstance(place, Place):
            raise TypeError("Debe ser una instancia de Place")
        if place not in self.places:
            self.places.append(place)
            if self not in place.amenity:
                place.amenity.append(self)
