from app.models.basemodel import BaseModel
from app.models.place import Place
from app.models.review import Review
from email_validator import validate_email, EmailNotValidError
from app.extensions import bcrypt, db
import uuid

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, first_name: str, last_name: str, email: str, password, is_admin=False):
        if not first_name or len(first_name) > 50:
            raise ValueError("First name is required and cannot exceed 50 characters")
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name is required and cannot exceed 50 characters")
        try:
            from email_validator import validate_email, EmailNotValidError
            email_validation = validate_email(email, check_deliverability=False)
            email = email_validation.normalized
        except EmailNotValidError:
            raise ValueError("Invalid email format")

        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.places = []  # lista de lugares que posee

    def add_place(self, place):
        """
        Agrega un Place al usuario.
        - Valida que sea instancia de Place.
        - Evita duplicados.
        - Asigna este usuario como owner del Place.
        """
        if not isinstance(place, Place):
            raise TypeError("Debe ser una instancia de Place")
        if place not in self.places:
            self.places.append(place)
            place.owner = self

    def add_review(self, review):
        """
        Agrega una Review al usuario.
        - Valida que sea instancia de Review.
        - Evita duplicados.
        - Asigna este usuario como autor de la Review.
        """
        if not isinstance(review, Review):
            raise TypeError("Debe ser una instancia de Review")
        if review not in self.reviews:
            self.reviews.append(review)
            review.user = self

    @property
    def password(self):
        return self.password_hash
    
    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)