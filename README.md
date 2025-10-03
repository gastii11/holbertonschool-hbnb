# HBnB Documentation


# Introduction to HBnB
This document was created to help understand and implement the HBnB project, a simplified version of AirBnB developed as part of a learning process. Its goal is to clearly explain how the system works, what components it consists of, and how to get it up and running step by step.

HBnB allows the management of data such as users, places to stay, reviews, and more, all through a well-organized structure designed to scale. Throughout this document, you will find information about the tools used, how they connect with each other, and what is needed for everything to work correctly.

The idea is that this guide serves as support both for those working directly on the project and for those who need to understand or maintain it in the future.

<img width="681" height="1562" alt="Diagrama sin título drawio" src="https://github.com/user-attachments/assets/fcf29c2e-42fc-4061-ac7e-094296da252f" />


```mermaid
classDiagram

    class BaseModel {
    <<super class>>
    +UUID
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
    +Int price
    +Int latitude
    +Int longitude
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
    +Int rating
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
    Place o-- Review : Composition

    Place <-- Amenity : Association
    User --> Review : Association
```
# Sequence Diagrams for API Calls

## User Registration sequence

```mermaid
sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant Database

    User ->> API : Register User (API Call)
    API -->> API : Wrong Data
    API -->> User : Wrong Data Error Message (code 400)

    API ->> BusinessLogic : Validate and Process Request
    BusinessLogic -->> BusinessLogic : Validation Failed
    BusinessLogic -->> API : Return Error
    API -->> User : Registration Failed Message (code 401)

    BusinessLogic ->> Database : Check User Existense
    Database -->> Database : User Already Exist
    Database -->> BusinessLogic : Return Error
    BusinessLogic -->> API : Return Error
    API -->> User : Registration Failed Message (code 401)

    BusinessLogic ->> Database : Create User
    Database -->> BusinessLogic : Return Success
    BusinessLogic -->> API : Return Success
    API -->> User : Registration Successfully Message (code 201)
```
## Place Creation sequence

```mermaid
sequenceDiagram
  participant User
  participant API
  participant BusinessLogic
  participant DataBase
  
    User ->> API : Place Creation (API Call)
    API -->> API : Wrong Data
    API -->> User : Wrong Data Error Message (code 400)

    API ->> BusinessLogic : Validate and Process Request
    BusinessLogic -->> BusinessLogic : Validation Failed
    BusinessLogic -->> API : Return Error
    API -->> User : Place Creation Failed Error Message (code 401)

    BusinessLogic ->> DataBase : Check Place Existense
    DataBase -->> DataBase : Place Already Exist
    DataBase -->> BusinessLogic: Return Error
    BusinessLogic -->> API : Return Error
    API -->> User : Place Creation Failed Error Message (code 401)

    BusinessLogic ->> DataBase : Create Place
    DataBase -->> BusinessLogic : Place Creation Succesfull
    BusinessLogic -->> API : Return Success
    API -->> User : Successfully Place Creation Message (code 201)
```
