from app.models.base import BaseModel

class Place(BaseModel):
    def __init__(self, title, price, latitude, longitude, owner, description=None):
        super().__init__()
        self.owner = owner  # relación con User (composición)
        self.title = title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.description = description or ""
        self.owner = owner
        self.amenities = []  # relación con Amenity

        owner.places.append(self) # agregamos el lugar al usuario dueño


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or len(value) > 100:
            raise ValueError("Title is required and must be <= 100 characters.")
        self._title = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive.")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not -90.0 <= value <= 90.0:
            raise ValueError("Latitude out of bounds.")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not -180.0 <= value <= 180.0:
            raise ValueError("Longitude out of bounds.")
        self._longitude = value

    def add_review(self, review):
        """
        Agrega una Review al Place.
        - Valida que sea instancia de Review.
        - Evita duplicados.
        - Asigna este Place como lugar de la Review.
        """
    if not isinstance(review, Review):
        raise TypeError("Debe ser una instancia de Review")
    if review not in self.reviews:
        self.reviews.append(review)

def add_amenity(self, amenity):
     """
        Agrega un Amenity al Place.
        - Valida que sea instancia de Amenity.
        - Evita duplicados.
        - Mantiene relación doble: agrega el Place a Amenity.places
        """
    if not isinstance(amenity, Amenity):
        raise TypeError("Debe ser una instancia de Amenity")
    if amenity not in self.amenities:
        self.amenities.append(amenity)
        if self not in amenity.places:
            amenity.places.append(self)  # relación doble
