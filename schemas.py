from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    description: str
    author: str
    year: int

class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class ConfigDict:
        from_attributes = True  # when pydamic version < 2.0
        # orm_mode = True # when pydantic version >= 2.0