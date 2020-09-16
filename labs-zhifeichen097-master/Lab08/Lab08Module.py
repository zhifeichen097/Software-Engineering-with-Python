#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18 >
#    Date:         <Mar.06,2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line


class TimeSpan:
    def __init__(self, weeks, days, hours):
        self.weeks = weeks
        self.days = days
        self.hours = hours

        if self.weeks < 0 or self.days < 0 or self.hours < 0:
            raise ValueError("The arguments cannot be negative")
        if self.hours >= 24:
            self.hours = self.hours % 24
            self.days += hours // 24
        if self.days >= 7:
            self.days = self.days % 7
            self.weeks += days // 7
        # print(self.weeks)
        # print(self.days)
        # print(self.hours)
    def __str__(self):
        return '"'+"{:02d}W {:01d}D {:02d}H".format(self.weeks, self.days, self.hours)+'"'
    def getTotalHours(self):
        total = 0
        total = self.hours + self.weeks * (7 * 24) + self.days * 24
        return total
    def __add__(self, other):
        new = TimeSpan(0,0,0)
        if not isinstance(self, TimeSpan) or not isinstance(other, TimeSpan):
            raise TypeError("The input must be an instance of the TimeSpan class")
        new.weeks = self.weeks + other.weeks
        new.days = self.days + other.days
        new.hours = self.hours + other.hours

        new.__init__(new.weeks, new.days, new.hours)
        return new
    def __radd__(self, other):
        return self.__add__(other)
    def __mul__(self, other):
        new = TimeSpan(0,0,0)
        if not isinstance(other, int) and not isinstance(other, float):
            raise TypeError("The input must be an instance of the int class")
        if other < 0:
            raise ValueError("The input must be greater than zero")
        # new.weeks = round(self.weeks * other)
        # new.days = round(self.days * other)
        # new.hours = round(self.hours * other)
        newtotal = round(self.getTotalHours() * other)
        #print(newtotal)
        new.weeks = newtotal // 168
        newtotal = newtotal % 168
        #print(newtotal)
        new.days = newtotal // 24
        newtotal = newtotal %  24
        #print(newtotal)
        new.hours = newtotal
        new.__init__(new.weeks, new.days, new.hours)
        return new
    def __rmul__(self, other):
        # if not isinstance(other, int) :
        #     raise TypeError("The input must be an instance of the int class")
        return self.__mul__(other)

    def __gt__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("The input must be an instance of the TimeSpan class")
        if self.getTotalHours() > other.getTotalHours():
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("The input must be an instance of the TimeSpan class")
        if self.getTotalHours() > other.getTotalHours():
            return False
        else:
            return True
    def __eq__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("The input must be an instance of the TimeSpan class")
        if self.getTotalHours() == other.getTotalHours():
            return True
        else:
            return False

    def __ne__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("The input must be an instance of the TimeSpan class")
        if self.getTotalHours() != other.getTotalHours():
            return True
        else:
            return False

    def __ge__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("The input must be an instance of the TimeSpan class")
        if self.getTotalHours() >= other.getTotalHours():
            return True
        else:
            return False

    def __le__(self, other):
        if not isinstance(other, TimeSpan):
            raise TypeError("The input must be an instance of the TimeSpan class")
        if self.getTotalHours() <= other.getTotalHours():
            return True
        else:
            return False
t1 = TimeSpan(weeks = 3, days = 7, hours = 49)
t2 = TimeSpan(weeks = 2, days = 1, hours = 1)
print(t1)
print(t1.getTotalHours())
print(type(t1 + t2))
print(t2 *2)
print(2.5 * t2)
print(t1 != t2)