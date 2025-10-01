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
