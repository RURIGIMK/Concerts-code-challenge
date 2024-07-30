class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

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
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if not hasattr(self, '_hometown'):
            if isinstance(value, str) and value:
                self._hometown = value
            else:
                raise ValueError("Hometown must be a non-empty string")

    def concerts(self):
        from concert import Concert
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        return list(set(concert.venue for concert in self.concerts()))

    def play_in_venue(self, venue, date):
        from concert import Concert
        return Concert(date, self, venue)

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]
