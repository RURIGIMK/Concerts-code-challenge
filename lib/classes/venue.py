class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and value:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string")

    def concerts(self):
        from concert import Concert
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        return list(set(concert.band for concert in self.concerts()))
