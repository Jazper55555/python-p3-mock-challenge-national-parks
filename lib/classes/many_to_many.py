from collections import Counter

class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            raise Exception('Name cannot change after national park has been instantiated')
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception('Name must be a string with 3 or more characters')
        
    def trips(self):
        return [trips for trips in Trip.all if trips.national_park == self]
    
    def visitors(self):
        return list(set([trips.visitor for trips in Trip.all if trips.national_park == self]))
    
    def total_visits(self):
        count = 0
        for trips in Trip.all:
            if trips.national_park == self:
                count += 1
        return count   
    
    def best_visitor(self):
        visitors_count = Counter(trips.visitor for trips in Trip.all if trips.national_park == self)
        if visitors_count:
            best_visitor = visitors_count.most_common(1)
            return best_visitor[0][0]
        else:
            return None
        
    @classmethod
    def most_visited(cls):
        park_visits = [trips.national_park for trips in Trip.all]
        for park in park_visits:
            park_counter = [park.total_visits()]
            if max(park_counter):
                return park
            else:
                return None




class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise Exception('Start date must be a string with at least 7 characters in the format of Month Day')
        
    @property
    def end_date(self):
        return self._end_date
        
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        else:
            raise Exception('End date must be a string with at least 7 characters in the format of Month Day')

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception('visitor must be an instance of Visitor')
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception('national_park must be an instance of NationalPark')

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception('Name must be a string between 1 & 15 characters long')
        
    def trips(self):
        return [trips for trips in Trip.all if trips.visitor == self]
    
    def national_parks(self):
        return list(set([trips.national_park for trips in Trip.all if trips.visitor == self]))
    
    def total_visits_at_park(self, park):
        count = 0
        for trips in Trip.all:
            if trips.national_park == park:
                count += 1
        return count