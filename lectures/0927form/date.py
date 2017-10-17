#!/usr/local/bin/python3.5

#Date object example

class Date:

    # the constructor
    def __init__(self, month=1, day=1, year=1970):
        self._month, self._day, self._year = month, day, year

    # getters
    def get_month(self):
        return self._month

    def get_day(self):
        return self._day

    def get_year(self):
        return self._year

    # setters
    def set_date(self, month, day, year):
        self._month, self._day, self._year = month, day, year

    # overload str function
    def __str__(self):
        return str(self._month) + '/'  \
               + str(self._day) + '/'  \
               + str(self._year)

    # check for leapyear
    def is_leapyear(self):    
        return self._year % 4 == 0 \
               and self._year % 100 != 0 \
               or self._year % 400 == 0

    #compare two dates
    def __lt__(self, rhs):
        if self.get_year() < rhs.get_year():
            return True
        if self.get_year() > rhs.get_year():
            return False
        # the years are equal at this point
        if self.get_month() < rhs.get_month():
            return True
        if self.get_month() > rhs.get_month():
            return False
        # the months are equal at this point
        if self.get_day() < rhs.get_day():
            return True
        return False
        
        

# test the code
if __name__ == '__main__':
    d = Date(10,11,2017)
    print (str(d))

    d.set_date(d.get_month(), d.get_day(), d.get_year() - 1)
    print (str(d))

    for year in [1900, 1901, 1800, 2100]:
        d.set_date(d.get_month(), d.get_day(), year)
        if d.is_leapyear():
            print (str(year) + " isn't a leapyear, there was an error")

    for year in [1904, 2000, 2016, 2104]:
        d.set_date(d.get_month(), d.get_day(), year)
        if not d.is_leapyear():
            print (str(year) + " is a leapyear, there was an error")

    today = Date(9,20,2017)
    tomorrow = Date(9,21,2017)

    if today < tomorrow:
       print ("less than works (1 of 2)")
    if not today < today:
       print ("less than works (2 of 2)")

