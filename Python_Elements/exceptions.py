class Coordinate:
    """
    Klasa odpowiedzialna za wartości współrzędnych, sprawdza przypisane wartości, manipuluje,
    waliduje.
    """

    def __init__(self, lat: float, long: float) -> None:
        self._latitude = self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        """Próba przypisania niewłaściwej wartości do atrybutu wywoła błąd.
           Gdy użytkownik zechce zmodyfikować wartości dowolnej z tych właściwości to
           zostanie automatycznie(i przezroczyście wywołana metoda walidacji zadeklarowana za
           pomocą dekoratora @latitude.setter)
        """
        if -90 <= lat_value <= 90:
            self._latitude = lat_value
        else:
            raise ValueError(f"{lat_value} is an invalid value for latitude", 1)

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        """Próba przypisania niewłaściwej wartości do atrybutu wywoła błąd.
           Gdy użytkownik zechce zmodyfikować wartości dowolnej z tych właściwości to
           zostanie automatycznie(i przezroczyście wywołana metoda walidacji zadeklarowana za
           pomocą dekoratora @longitude.setter)
        """
        if -180 <= long_value <= 180:
            self._longitude = long_value
        else:
            raise ValueError(f"{long_value} is an invalid value for longitude", 1)


class ServiceGeneratingMap:
    """Klasa odbiera/otrzymuje dane które opisują współrzendne np: z andpointu przekształca je
     na objekt Coordinate
     1. Klasa nawiązuje połaczenie z 3 serwisem odpowiedzialnym za wygenerowaniem linku go google
     maps na podstawie Coordinate.
     """

    def execute(self, lat: float, long: float):
        return self._get_link_to_map(self._create_object_coordinate(lat, long))

    @staticmethod
    def _create_object_coordinate(lat: float, long: float) -> Coordinate:
        return Coordinate(lat, long)

    @staticmethod
    def _get_link_to_map(co_ordinates: Coordinate) -> str:
        return f'https://www.google.com/maps/place/@{co_ordinates.latitude},' \
               f'{co_ordinates.longitude}/17z/hl=pl'


class Endpoint:
    def __init__(self):
        self.service_generating_map = ServiceGeneratingMap()

    def get_link_to_map(self, lat: float, long: float):
        try:
            return {
                "message": "success",
                "code": 200,
                "link": self.service_generating_map.execute(lat, long)
            }
        except BaseException as e:
            return {
                "message": e,
                "code": 400,
                "link": None
            }


endpoint = Endpoint()
print(endpoint.get_link_to_map(52.3197577, 20.9650879))
print(endpoint.get_link_to_map(190.3197577, 20.9650879))
