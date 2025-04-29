from sqlalchemy import text

from extensions import db
from dtos import ListUserDto, UserDto

class UsersRepository:
    def list(self) -> ListUserDto:
        t = text('SELECT * FROM tb_users')
        users = db.session.execute(t)

        return ListUserDto.from_rows(users.fetchall())

    def create(self, name: str) -> UserDto:
        t = (
            text('INSERT INTO tb_users(name) VALUES (:name)')
            .bindparams(name=name)
        )
        db.session.execute(t)
        db.session.commit()

        t = (
            text('SELECT * FROM tb_users ORDER BY user_id DESC LIMIT 1;')
        )
        result = db.session.execute(t)

        return UserDto.from_row(result.fetchone())
