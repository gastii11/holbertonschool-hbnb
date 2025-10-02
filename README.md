```mermaid
classDiagram
class Presentation {
    <<layer>>
    +Services
    +API
}
class Business {
    <<layer>>
    +User
    +Place
    +Review
    +Amenity
}
class Persistence {
    <<layer>>
    +DataAccess
}
Presentation --> Business : Facade
Business --> Persistence : Data Access
```
<img width="681" height="1562" alt="Diagrama sin título drawio" src="https://github.com/user-attachments/assets/fcf29c2e-42fc-4061-ac7e-094296da252f" />


```mermaid
classDiagram

    class BaseModel {
    <<super class>>
    +UUID uuid
    +Date creation_date
    +Date last_update
    }

    class User {
    <<model>>
    +String first_name
    +String last_name
    +String email
    +String password
    +Bool is_admin
    +register()
    +update()
    +delete()
    }

    class Place {
    <<model>>
    +User owner
    +String title
    +String description
    +Number price
    +Number latitude
    +Number longitude
    +List (Amenity) amenities
    +create()
    +update()
    +delete()
    +list()
    }

    class Amenity {
    <<model>>
    +String name
    +String description
    +create()
    +update()
    +delete()
    +list()
    }

    class Review {
    <<model>>
    +String comment
    +Number rating
    +create()
    +update()
    +delete()
    +list()
    }

    User --|> BaseModel : Inheritance
    Place --|> BaseModel : Inheritance
    Amenity --|> BaseModel  : Inheritance
    Review --|> BaseModel : Inheritance

    Place o-- User : Composition
    Place o-- Amenity : Composition
    Place o-- Review : Composition

    User --> Review : Association
```
