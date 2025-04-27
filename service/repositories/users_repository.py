from sqlalchemy import text

from extensions import db

class UsersRepository:
    def list(self):
        t = text('SELECT * FROM tb_users')
        users = db.session.execute(t)

        return users

    def create(self, name: str):
        t = (
            text('INSERT INTO tb_users(name) VALUES (:name)')
            .bindparams(name=name)
        )
        db.session.execute(t)
        db.session.commit()

        return
