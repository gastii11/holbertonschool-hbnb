from app.models.basemodel import BaseModel


class User(BaseModel):
    def __init__(self, first_name: str, last_name: str, email: str, is_admin: bool = False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []  # lista de lugares que posee


    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value or len(value) > 50:
            raise ValueError("First name is required and cannot exceed 50 characters")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value or len(value) > 50:
            raise ValueError("Last name is required and cannot exceed 50 characters")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        try:
            email_validation = validate_email(value, check_deliverability=False)
            self._email = email_validation.normalized
        except EmailNotValidError:
            raise ValueError("Invalid email format")

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
