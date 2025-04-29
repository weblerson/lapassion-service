from sqlalchemy import text

from extensions import db
from dtos import ListLocation, Location


class LocationRepository:
    def list(self) -> ListLocation:
        t = text('SELECT * FROM tb_location;')
        results = db.session.execute(t)

        return ListLocation.from_rows(results.fetchall())

    def create(
            self,
            lat: int,
            lon: int,
            klass: int,
            user_id: int
    ) -> Location:
        query = """
        INSERT INTO
            tb_location(lat, lon, class, user_id)
        VALUES
            (:lat, :lon, :klass, :user_id);
        """

        t = (
            text(query)
            .bindparams(
                lat=lat,
                lon=lon,
                klass=klass,
                user_id=user_id,
            )
        )

        db.session.execute(t)
        db.session.commit()

        query = """
        SELECT
            *
        FROM
            tb_location
        ORDER BY
            location_id DESC
        LIMIT 1;
        """
        t = text(query)

        result = db.session.execute(t)

        return Location.from_row(result.fetchone())
