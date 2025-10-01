'''mermeid
classDiagram
class Presentation {
    <<layer>>
    +Service
    +API
}

class Business {
    <<layer>>
    +User
    +Place
    +Review
    +Amenty
}

class Persistence {
    <<layer>>
    +DataAccess
}

Presentation --> Business : Facade
Business --> Persistence : Data Access
'''