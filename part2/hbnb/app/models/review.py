from app.models.basemodel import BaseModel


class Review(BaseModel):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.user_id = user_id # asociación con User (asociasion)
        self.place_id = place_id # asociación con Place (asociasion)
        self.text = text
        self.rating = rating

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not value:
            raise ValueError("Review text is required.")
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self._rating = value

    def set_user(self, user):
        from app.models.user import User
        """
        Asigna un User como autor de la Review.
        - Valida tipo.
        - Evita duplicados en user.reviews.
        """
        if not isinstance(user, User):
            raise TypeError("Debe ser una instancia de User")
        self.user = user
        if self not in user.reviews:
            user.reviews.append(self)

    def set_place(self, place):
        from app.models.place import Place
        """
        Asigna un Place a la Review.
        - Valida tipo.
        - Evita duplicados en place.reviews.
        """
        if not isinstance(place, Place):
            raise TypeError("Debe ser una instancia de Place")
        self.place = place
        if self not in place.reviews:
            place.reviews.append(self)
