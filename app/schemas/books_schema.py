from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    title: str
    description: str
    author_id: int
    author: str
    year: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    # class ConfigDict:
    #     from_attributes = True  # when pydamic version < 2.0
    #     # orm_mode = True # when pydantic version >= 2.0
