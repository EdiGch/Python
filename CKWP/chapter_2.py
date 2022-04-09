# Kod Pythoniczny

## Wyrażenia składowe i wyrażenia przypisania


def run_calculations(i: int) -> int:
    return i + 5


numbers = []
for i in range(10):
    numbers.append(run_calculations(i))

numbers = [run_calculations(i) for i in range(10)]


# Znaki podkreślenia w Pythonie
class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60


# Właściwości
class Coordinate:
    def __init__(self, lat: float, long: float) -> None:
        self._latitude = self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        """Próba przypisania właściwej wartości do atrybutu wywoła błąd"""
        if -90 <= lat_value <= 90:
            self._latitude = lat_value
        else:
            raise ValueError(f"{lat_value} is an invalid value for latitude")

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        """Próba przypisania właściwej wartości do atrybutu wywoła błąd"""
        if -180 <= long_value <= 180:
            self._longitude = long_value
        else:
            raise ValueError(f"{long_value} is an invalid value for longitude")


coordinate = Coordinate(52.3198094, 20.9650691)
latitude = coordinate.latitude
longitude = coordinate.longitude

# Umyśle wywołanie błedu.
coordinate.latitude = 180
coordinate.longitude = 360
