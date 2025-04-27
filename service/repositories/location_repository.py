from sqlalchemy import text
from extensions import db


class LocationRepository:
    def list(self):
        t = text('SELECT * FROM tb_location;')

        return db.session.execute(t)

    def create(
            self,
            lat: int,
            lon: int,
            klass: int,
            user_id: int
    ):
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
