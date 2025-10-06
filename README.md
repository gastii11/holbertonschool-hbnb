# HBnB Documentation


# Introduction to HBnB
This document was created to help understand and implement the HBnB project, a simplified version of AirBnB developed as part of a learning process. Its goal is to clearly explain how the system works, what components it consists of, and how to get it up and running step by step.

HBnB allows the management of data such as users, places to stay, reviews, and more, all through a well-organized structure designed to scale. Throughout this document, you will find information about the tools used, how they connect with each other, and what is needed for everything to work correctly.

The idea is that this guide serves as support both for those working directly on the project and for those who need to understand or maintain it in the future.

## What is a Three-Tier Architecture?

Three-tier architecture is a software design pattern that organizes an application into three independent layers, each with clearly defined responsibilities. This approach separates the presentation logic, business logic, and data access logic, promoting better code organization, greater maintainability, and system scalability.

## The three layers of the architecture are:

### Presentation Layer
This is the top layer that users interact with directly. Its function is to display information and collect input from the user. It acts as the user interface of the application, rendering web pages and handling user requests.

### Business Logic Layer
This middle layer acts as the "brain" of the application, processing requests from the presentation layer and applying core business rules. It manages key application logic such as user authentication, data validation, and business workflows. It processes information from the presentation layer and interacts with the data layer.

### Persistence Layer
This is the back-end layer that stores and manages the application's data. It is only accessed by the application layer, never directly by the presentation layer. It handles data storage, retrieval, and manipulation, ensuring persistence across user sessions.

<img width="681" height="1561" alt="Diagrama sin fondo y flechas negras drawio" src="https://github.com/user-attachments/assets/6c21753e-840e-43e3-9719-212b4137bdad" />

## Use of the Facade Pattern in a Three-Tier Architecture
### What is the Facade Pattern?

The Facade pattern provides a single, simplified interface to a complex system, acting as a front-facing layer that hides the intricacies of underlying components and their interactions. It improves code readability and usability by reducing dependencies and offering a clearer entry point for clients to interact with a subsystem without needing to understand its internal complexity.

## Where is the Facade Pattern applied in HBnB?

In the three-tier architecture, the Facade pattern is applied in the Core layer, serving as a unified gateway between the API and the business logic.

Without Facade: The API would need to directly access all the Core classes (User, Place, Review, Amenity) and understand how to interact with each of them, leading to tight coupling.

With Facade: The API interacts only with a central class or module (a "facade"), which internally coordinates all necessary operations. This simplifies communication and improves modularity.

## Database Operations in a Three-Tier Architecture

Database operations refer to the fundamental actions of creating, reading, updating, and deleting (CRUD) data within the application's back-end database.

The purpose of the Data Access Layer is to isolate data access from the rest of the application. This way, the upper layers (like the business logic or API) don’t need to know how the database operations are implemented or worry about SQL statements, database connections, or transaction handling.

By encapsulating these concerns in a dedicated layer, the system becomes more modular, testable, and easier to maintain.



# Detailed Class Diagram for Business Logic Layer

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
# Detailed Class Diagram for Business Logic Layer
## Introduction

This document describes the class model designed for the application. The goal is to model the system’s main entities, their attributes, operations, and the relationships between them, ensuring a clear structure for future implementation.

The system is based on an HBnB-style model, where users can register places, manage amenities, and write reviews.

## General Description

The class diagram represents the main entities of the application and their relationships. It consists of five key classes: BaseModel, User, Place, Amenity, and Review.

The BaseModel class acts as a superclass that provides common attributes, such as a unique identifier and timestamps, ensuring consistency across all entities. The User class represents the individuals registered in the system, while the Place class models the properties that users can list or rent. The Amenity class describes additional services or features that a place can offer, such as Wi-Fi or parking. Finally, the Review class allows users to provide feedback through comments and ratings on listed places.

All classes inherit from BaseModel, ensuring that they share a unified structure for identification and time management. The relationships between classes are also clearly defined: a Place is linked to a single User as its owner, may contain multiple Amenities, and can receive multiple Reviews. Additionally, users are directly associated with the reviews they create.

This structure establishes a solid foundation for representing the application’s domain and provides a clear blueprint for implementation in code.

## Class Documentation
## Class BaseModel

**Type:** Superclass

**Purpose:** Provides basic attributes common to all system entities.

### Attributes:

**uuid:** Universal unique identifier.

**creation_date:** Creation date.

**last_update:** Last modification date.

## Class User

**Type:** Model

**Purpose:** Represents the users registered in the system.

### Attributes:

**first_name:** User’s first name.

**last_name:** User’s last name.

**email:** User’s email address.

**password:** Encrypted password.

**is_admin:** Indicates whether the user has admin privileges.

### Methods:

**register():** Creates a new user.

**update():** Updates user information.

**delete():** Deletes a user.

## Class Place

**Type:** Model

**Purpose:** Represents a place available for hosting or rental.

### Attributes:

**owner:** The user who owns the place.

**title:** Place title or name.

**description:** Place description.

**price:** Price per stay.

**latitude:** Latitude coordinate.

**longitude:** Longitude coordinate.

**amenities:** List of amenities associated with the place.

### Methods:

**create():** Creates a new place.

**update():** Updates place information.

**delete():** Deletes a place.

**list():** Returns the available places.

## Class Amenity

**Type:** Model

**Purpose:** Defines additional services that a place may offer (e.g., Wi-Fi, pool, parking).

### Attributes:

**name:** Amenity name.

**description:** Short description.

### Methods:

**create():** Creates an amenity.

**update():** Updates amenity information.

**delete():** Deletes an amenity.

**list():** Lists all available amenities.

## Class Review

**Type:** Model

**Purpose:** Stores reviews written by users about places.

### Attributes:

**comment:** Review text.

**rating:** Numeric rating.

### Methods:

**create():** Creates a review.

**update():** Updates a review.

**delete():** Deletes a review.

**list():** Lists existing reviews


## Relationships Between Classes

**Inheritance:**

All classes (User, Place, Amenity, Review) inherit from BaseModel, sharing identity and time-related attributes.

**Composition:**

Place composes User: each place belongs to one owner.

Place composes Amenity: a place can include multiple amenities.

Place composes Review: a place can contain multiple reviews.

**Association:**

User associated Review: A user can create multiple reviews.


# Sequence Diagrams for API Calls

# User Registration sequence

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

## General Description

The Register User use case allows a new user to create an account in the system.
The process involves four main components: User, API, Business Logic Layer, and Database.
The flow considers both successful scenarios and errors (incorrect data, existing user, failed validations).

## Components

**User:** Interacts with the system interface to submit registration data.

**API:** Receives requests from the user and forwards the information to the business logic layer.

**BusinessLogic:** Validates the information, checks for existing users, and applies business rules.

**Database:** Stores the new user information persistently and returns confirmations or errors.

## Process Flow
### Main Flow (Successful Registration)

1. The User submits the registration data to the API.

2. The API forwards the request to BusinessLogic for validation.

3. BusinessLogic validates the data and checks that the user does not already exist.

4. If everything is correct, a request is sent to the Database to create the new user.

5. The Database confirms the creation.

6. BusinessLogic receives the confirmation and returns success to the API.

7. The API sends the User a registration success message (HTTP 201).

## Alternative Flows (Errors)

### Incorrect Data

If the data submitted by the user is invalid, BusinessLogic returns a validation error.

The API responds with HTTP 400 and message: Wrong Data Error Message.

### Failed Validation

If the data does not meet the business rules (e.g., weak password), BusinessLogic returns an error.

The API responds with HTTP 401 and message: Registration Failed Message.

### User Already Exists

If the user’s email is already registered, BusinessLogic detects the existing account and returns an error.

The API responds with HTTP 401 and message: Registration Failed Message.

# Place Creation sequence

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
## General Description

The Place Creation use case allows a user to create a new Place within the system.
The process covers the entire flow — from when the user submits the place data until the system validates and stores it in the database.
This flow includes both successful and error scenarios such as invalid data, validation failure, or an already existing place.

## Components

User: Interacts with the system interface to create a new place.

API: Receives the user’s request, performs initial checks, and forwards it to the business logic layer.

BusinessLogic: Applies business rules, verifies if the place already exists, and handles the creation process.

Database: Stores the new place information and returns confirmation or error messages.

## Process Flow
### Main Flow (Successful Registration)


1. The User sends a request to the API to create a new place.

2. The API receives the request and forwards it to the BusinessLogic layer.

3. BusinessLogic validates the received data.

4. It checks the Database to verify if the place already exists.

5. If the place does not exist, BusinessLogic requests the Database to create a new record.

6. The Database confirms that the place was successfully created.

7. BusinessLogic sends a success message back to the API.

8. The API responds to the User with a successful creation message (HTTP 201).

## Alternative Flows (Errors)
### Invalid Data

If the data sent by the user is invalid (missing fields, wrong format, etc.), the API returns:

HTTP Code: 400

Message: Wrong Data Error Message.

### Validation Failed

If the BusinessLogic detects that the data does not meet business rules (e.g., too short name, invalid location):

HTTP Code: 401

Message: Place Creation Failed Error Message.

### Place Already Exists

If the place already exists in the database, BusinessLogic returns an error:

HTTP Code: 401

Message: Place Creation Failed Error Message

## Review Submission sequence

```mermaid
sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant DataBase

    User ->> API : Review Submission (API Call)
    API -->> API : Wrong Data
    API -->> User : Wrong Data Error Message (code 400)

    API ->> BusinessLogic : Validate and Process Request
    BusinessLogic -->> BusinessLogic : Validation Failed
    BusinessLogic -->> API : Return Error
    API -->> User : Review Submission Failed Error Message (code 401)

    BusinessLogic ->> DataBase : Create Review
    DataBase -->> BusinessLogic : Review Creation Succesfull
    BusinessLogic -->> API : Return Success
    API -->> User : Successfully Review Submission Message (code 201)
```

## Fetching a List of Places sequence

```mermaid
sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant DataBase

    User ->> API : Fetching a List of Places (API Call)
    API -->> API : Wrong Data
    API -->> User : Wrong Data Error Message (code 400)

    API ->> BusinessLogic : Validate and Process Request
    BusinessLogic -->> BusinessLogic : Validation Failed
    BusinessLogic -->> API : Return Error
    API -->> User : Fetching a List of Places <br> Failed Error Message (code 401)

    BusinessLogic ->> DataBase : Check Places List Existense
    DataBase -->> DataBase : Places List Not Available
    DataBase -->> BusinessLogic: Return Error
    BusinessLogic -->> API : Return Error
    API -->> User : No Places To Show Message (code 401)

    BusinessLogic ->> DataBase : Get Places List
    DataBase -->> BusinessLogic : Return Places List
    BusinessLogic -->> API : Return Success
    API -->> User : Show Places List (code 200)
```

## HTTP Response Codes Explanation

**200:** OK - Successful request (no new resource created)
**201:** Created - New resource successfully created
**400:** Bad Request - Invalid or missing input data
**401:** Unauthorized / Validation Failed - Business rule violation or existing record


