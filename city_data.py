# city_data.py
# A class for storing a city's population data
# Starter Code from CSC 210
# Modified by: [Jackie Arteaga]

class CityData:
    def _init_ (self, name, start_year, end_year, data):
    # private variables
        self._name = name
        self._start_year = start_year
        slef._end_year = end_year
        self._data + data 
        # population # by year
   

    @property
    def name(self):
        return self._name

    @property
    def start_year(self):
        return self._start_year

    @property
    def end_year(self):
        return self._end_year

    def __getitem__(self, year):
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year < self._start_year or year > self._end_year:
            raise IndexError("Year out of range")
        return self._data[year - self._start_year]

    @property
    def min_year(self):
        min_index = self._data.index(min(self._data))
        return self._start_year + min_index
        # what is the lowest population

    @property
    def max_year(self):
        max_index = self._data.index(max(self.data))
        return self._start_year + max_index
        # what is the highest population
    # help from chatgpt to find years with max and min population

    def population_growth(self, year1, year2):
        pop1 = self[year1]
        pop2 = self[year2]
        return pop2 - pop1
        # returns the difference between year2 and year1
        # help from chatgpt to figure out how to return the difference
    
