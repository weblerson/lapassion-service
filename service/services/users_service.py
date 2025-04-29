from repositories import UsersRepository
from dtos import ListUserDto, UserDto


class UsersService:
    def __init__(self, users_repository: UsersRepository):
        self.__users_repository = users_repository

    def list(self) -> ListUserDto:
        return self.__users_repository.list()

    def create(self, name) -> UserDto:
        return self.__users_repository.create(name)
