from repositories import UsersRepository


class UsersService:
    def __init__(self, users_repository: UsersRepository):
        self.__users_repository = users_repository

    def list(self):
        return self.__users_repository.list()

    def create(self, name):
        return self.__users_repository.create(name)
