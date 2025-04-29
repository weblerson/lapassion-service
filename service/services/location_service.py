from repositories import LocationRepository
from dtos import ListLocation, Location


class LocationService:
    def __init__(self, location_repository: LocationRepository):
        self.__location_repository = location_repository

    def list(self) -> ListLocation:
        return self.__location_repository.list()

    def create(
            self,
            lat: int,
            lon: int,
            klass: int,
            user_id: int
    ) -> Location:
        return self.__location_repository.create(
            lat, lon, klass, user_id,
        )
