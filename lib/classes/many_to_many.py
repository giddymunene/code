
class Band:
    def __init__(self, name, hometown):
        self.name = name
        self._hometown = hometown

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError('name must a non-empty string.')

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        raise AttributeError('hometown is immutable')

    def concerts(self):
        return [concert for concert in Concert.all if concert.band is self]

    def venues(self):
        return list(set([concert.venue for concert in self.concerts()]))

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts() if concert.introduction()]


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError('date must be non-empty string')

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError('Band must be an instance of band class')

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError('venue must be an instance of venue class')

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f'Was sup {self.venue.city}! We are {self.band.name} from {self.band.hometown}'

    @date.setter
    def date(self, value):
        self._date = value


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError('name must be a non-empty string')

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError('city must be a non-empty string')

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue is self]

    def bands(self):
        return list({concert.band for concert in self.concerts()})

