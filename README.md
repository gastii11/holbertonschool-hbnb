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
