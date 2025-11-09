from app.models.basemodel import BaseModel
from app.extensions import db
import uuid
from app.models.place import place_amenity


class Amenity(db.Model, BaseModel):
    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    _name = db.Column("name", db.String(50), nullable=False, unique=True)

    places = db.relationship(
        'Place',
        secondary=place_amenity,
        back_populates='amenities'
    )

    def __init__(self, name):
        if not name or len(name) > 50:
            raise ValueError("Amenity name is required and must not exceed 50 characters")
        super().__init__()
        self._name = name
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
        from app.models.place import Place
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
