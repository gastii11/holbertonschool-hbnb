from app.models.basemodel import BaseModel
from app.extensions import db
import uuid

place_amenity = db.Table(
    'place_amenity',
    db.Column('place_id', db.String(36), db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String(36), db.ForeignKey('amenities.id'), primary_key=True)
)

class Place(db.Model, BaseModel):
    __tablename__ = 'places'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    _title = db.Column("title", db.String(100), nullable=False)
    _price = db.Column("price", db.Float, nullable=False)
    _latitude = db.Column("latitude", db.Float, nullable=False)
    _longitude = db.Column("longitude", db.Float, nullable=False)
    description = db.Column(db.Text, default="")
    owner_id = db.Column(db.String(36), nullable=False)

    amenities = db.relationship(
        'Amenity',
        secondary=place_amenity,
        back_populates='places'
    )

    reviews = db.relationship(
        "Review",
        back_populates="place",
        cascade="all, delete-orphan"
    )

    def __init__(self, title, price, latitude, longitude, owner_id, description=None):
        super().__init__()
        self.owner_id = owner_id
        self.title = title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.description = description or ""

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
        from app.models.review import Review
        if not isinstance(review, Review):
            raise TypeError("Debe ser una instancia de Review")
        if review not in self.reviews:
            self.reviews.append(review)

    def add_amenity(self, amenity):
        from app.models.amenity import Amenity
        if not isinstance(amenity, Amenity):
            raise TypeError("Debe ser una instancia de Amenity")
        if amenity not in self.amenities:
            self.amenities.append(amenity)
        if self not in amenity.places:
            amenity.places.append(self)
