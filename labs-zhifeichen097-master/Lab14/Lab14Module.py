#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18 >
#    Date:         <Apr.17,2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line

import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
DataPath = os.path.expanduser('~ee364/DataFolder/Lab14')
from Lab10.measurement import calculateDistance
from enum import Enum

class Direction(Enum):
    Incoming = 0
    Outgoing = 1
    Both = 2
class Leg:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.sourceZip = re.search(r'[ ][0-9A-Z]{5}', self.source)
        self.destZip = re.search(r'[ ][0-9A-Z]{5}', self.destination)
        #self.distance = calculateDistance(self.sourceZip[0].replace(" ", ""), self.destZip[0].replace(" ", ""))
        self.szip = self.sourceZip[0].replace(" ", "")
        self.dzip = self.destZip[0].replace(" ", "")
    def __str__(self):
        return f"{self.szip}" + " => " f"{self.dzip}"
    def __repr__(self):
        return self.__str__()
    def calculateLength(self, locationMap):
        return round(calculateDistance(locationMap[self.szip], locationMap[self.dzip]),2)
class Trip:
    def __init__(self, person, legs):
        self.person = person
        self.legs = legs
    def calculateLength(self, locationMap):
        totalDis = 0
        for leg in self.legs:
            totalDis += calculateDistance(locationMap[leg.szip], locationMap[leg.dzip])
        return round(totalDis,2)
    def getLegsByZip(self, zipcode, level):
        self.level = level.name
        result = []
        if self.level == "Incoming":
            for leg in self.legs:
                if leg.dzip == zipcode:
                    result.append(leg)
        elif self.level == "Outgoing":
            for leg in self.legs:
                if leg.szip == zipcode:
                    result.append(leg)
        elif self.level == "Both":
            for leg in self.legs:
                if leg.szip == zipcode or leg.dzip == zipcode:
                    result.append(leg)
        if result == None:
            return []
        else:
            return result

    def getLegsByState(self, state, level):
        self.level = level.name
        result = []
        if self.level == "Incoming":
            for leg in self.legs:
                self.sourceState = re.search(r'[ ][A-Z]{2}[ ]', leg.source)
                self.destState = re.search(r'[ ][A-Z]{2}[ ]', leg.destination)
                self.sState = self.sourceState[0].replace(" ", "")
                self.dState = self.destState[0].replace(" ", "")
                if self.sState == state:
                    result.append(leg)
        elif self.level == "Outgoing":
            for leg in self.legs:
                self.sourceState = re.search(r'[ ][A-Z]{2}[ ]', leg.source)
                self.destState = re.search(r'[ ][A-Z]{2}[ ]', leg.destination)
                self.sState = self.sourceState[0].replace(" ", "")
                self.dState = self.destState[0].replace(" ", "")
                if self.sState == state:
                    result.append(leg)
        elif self.level == "Both":
            for leg in self.legs:
                self.sourceState = re.search(r'[ ][A-Z]{2}[ ]', leg.source)
                self.destState = re.search(r'[ ][A-Z]{2}[ ]', leg.destination)
                self.sState = self.sourceState[0].replace(" ", "")
                self.dState = self.destState[0].replace(" ", "")
                if self.dState == state or self.sState == state:
                    result.append(leg)

        if result == None:
            return []
        else:
            return result
    def __add__(self, other):
        if not isinstance(self, Trip):
            raise TypeError("Input has to be a correct type")
        if not isinstance(other, Trip):
            raise TypeError("Input has to be a correct type")
        if self.person != other.person:
            raise ValueError("must be same person")

        newTrip = Trip(self.person, self.legs)
        newTrip.legs.append(other)
        return newTrip
    def __radd__(self, other):
        return self.__add__(other)

class RoundTrip(Trip):
    def __init__(self):
        super.__init__(self.person, self.legs)

def mapziptolat():
    file = os.path.join(DataPath, 'locations.dat')
    map = {}
    with open(file, 'r') as floc:
        next(floc)
        for line in floc:
            output = re.search('\"(?P<zip>[0-9A-Z]{5})\"', line)
            sourcelang = re.search('\"\s?(?P<lang>[0-9]{2}\.[0-9]{6})', line)
            sourcelat = re.search('\"\s?(?P<lat>[-][0-9]{2,}\.[0-9]{5})\"', line)
            source1 = tuple((float(sourcelang["lang"]), float(sourcelat["lat"])))
            map[output["zip"]] = source1
    return map
def getShortestTrip(source, destination, stops):

    tripList = []
    tlist = {}
    asdlist = []
    # sourcez = re.search(r'[ ][0-9A-Z]{5}', source)
    # szip = sourcez[0].replace(" ", "")
    # destz = re.search(r'[ ][0-9A-Z]{5}', destination)
    # dzip = sourcez[0].replace(" ", "")
    for stop in stops:
        l1 = Leg(source, stop)
        l2 = Leg(stop, destination)

        tripList.append(l1)
        tripList.append(l2)
        Trip1 = Trip(" ", tripList)

        asdlist.append(Trip1.calculateLength(mapziptolat()))
        tlist[(Trip1.calculateLength(mapziptolat()))] = Trip1
    return tlist[min(asdlist)]


# def getTotalDistanceFor(person):
#     file = os.path.join(DataPath, 'trips.dat')
#     with open(file, 'r') as floc:
#         next(floc)
#         for line in floc:
#             zz = line.split('"')[1]
#             if person == zz:
#
#                     zips = re.findall(r'[ ][0-9A-Z]{5}', line)
#                     print(zips)
#                     for zip in zips:
#                         #print(enumerate(zip))
#
#
#
#                     #zipcode = zip[0].replace(" ", "")






        # totaldis = 0
        # zip = re.search(r'[ ][0-9A-Z]{5}', stop)
        # zipcode = zip[0].replace(" ", "")
        #
        # totaldis = calculateDistance(mapziptolat(szip),mapziptolat(zipcode)) + calculateDistance(mapziptolat(zipcode),mapziptolat(zipcode))






if __name__ == "__main__":
    p1 = Leg("Packwood, WA 98361", "Naples, FL 34108")
    p2 = Leg("Packwood, WA 34108", "Naples, FL 32046")
    p3 = Leg("Packwood, WA 34208", "Naples, FL 32046")
    L1 = Trip("Taylor", [p1,p2])
    L2 = L1 + L1
    print(L2.legs)
    #print(L1.legs)
    #print(mapziptolat())
    #getTotalDistanceFor(123)
    #getTotalDistanceFor("Garcia, Martha")
    #print(L1.getLegsByZip("32046", Direction.Incoming))
   # print(L1.getLegsByState("WA", Direction.Incoming))
    #print(L1.calculateLength({"98361":(36.427702, -92.11109), "34108":(39.427702, -72.11109)}))
  #  print(p1)
    #print(p1.calculateLength({"98361":(36.427702, -92.11109), "34108":(39.427702, -72.11109) }))
