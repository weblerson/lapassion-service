import datetime

from typing import Sequence, Any, Optional

from sqlalchemy import Row
from pydantic import BaseModel


class Location(BaseModel):
    location_id: int
    lat: int
    lon: int
    instant: datetime.datetime
    klass: int
    user_id: int

    @classmethod
    def from_row(cls, row: Row[Any] | None):
        # Raise Exception
        # Based
        if row is None:
            return

        return cls(
            location_id=row[0],
            lat=row[1],
            lon=row[2],
            instant=row[3],
            klass=row[4],
            user_id=row[5]
        )


# Based
class ListLocation(BaseModel):
    locations: list[Optional[Location]]

    @classmethod
    def from_rows(cls, rows: Sequence[Row]):
        _locations = [Location.from_row(row) for row in rows]

        return cls(locations=_locations)
