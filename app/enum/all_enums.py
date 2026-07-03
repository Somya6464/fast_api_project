import enum as Enum

class UserRole(str, Enum):
    AUTHOR = "author"
    USER = "user"