from pydantic import BaseModel


class UserDto(BaseModel):
    id: int
    name: str

    @classmethod
    def from_row(cls, row):
        return cls(id=row[0], name=row[1])


class ListUserDto(BaseModel):
    users: list[UserDto]

    @classmethod
    def from_rows(cls, rows):
        results = []
        for row in rows:
            results.append(UserDto(id=row[0], name=row[1]))

        return cls(users=results)
