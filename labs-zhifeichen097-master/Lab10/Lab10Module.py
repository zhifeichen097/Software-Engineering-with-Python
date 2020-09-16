#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu >
#    ID:           <ee364g18>
#    Date:         <Mar 27, 2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
DataPath = os.path.expanduser('~ee364/DataFolder/Lab10')
file = os.path.join(DataPath, 'coordinates.dat')
from Lab10.measurement import calculateDistance
#sourceZip, destinationZip
def getCost(sourceZip, destinationZip):
    with open (file,'r') as fcoord:
        next(fcoord)
        for line in fcoord:
            output = re.search('\"(?P<zip>[0-9A-Z]{5})\"', line)
            #print((output["zip"]))
            #print(type(sourceZip))
            if output["zip"] == sourceZip:
                #print(line)
                #print(output)
                sourcelang = re.search('\"\s?(?P<lang>[0-9]{2}\.[0-9]{6})', line)
                sourcelat = re.search('\"\s?(?P<lat>[-][0-9]{2,}\.[0-9]{5})\"', line)
               # print(sourcelang["lang"])
                #print(sourcelat["lat"])
                source1 = tuple((float(sourcelang["lang"]),float(sourcelat["lat"])))
            #else: source1 = (0,0)
            if output["zip"] == destinationZip:
                #print(line)
                destlang = re.search('\"\s?(?P<lang>[0-9]{2}\.[0-9]{6})', line)
                destlat = re.search('\"\s?(?P<lat>[-][0-9]{2,}\.[0-9]{5})\"', line)
                dest = tuple((float(destlang["lang"]), float(destlat["lat"])))

        #print(calculateDistance(source, dest))
        #print(sourcelang)
       # if dest != None or source1 != None:
    result = calculateDistance(source1, dest) * 0.01
    print(round(result,2))
    if dest == None or source1 == None:
        return 0
    return round(result,2)
getCost("99337","35115")


class Package:

    def __init__(self,source, destination):
        self.source = source
        self.destination = destination
        self.cost = getCost(self.source, self.destination)
    def __str__(self):
        return f"{self.source} " + "=>" + f"{ self.destination, }"

    def __gt__(self, other):
        if not isinstance(other, Package):
            raise TypeError("Input item is not a instance of packet class")
        if self.cost > other.cost:
            return True
        else:
            return False
    def __lt__(self, other):
        if not isinstance(other, Package):
            raise TypeError("Input item is not a instance of packet class")
        if self.cost < other.cost:
            return True
        else:
            return False
    def __eq__(self, other):
        if not isinstance(other, Package):
            raise TypeError("Input item is not a instance of packet class")
        if self.cost == other.cost:
            return True
        else:
            return False
    def __ge__(self, other):
        if not isinstance(other, Package):
            raise TypeError("Input item is not a instance of packet class")
        if self.cost >= other.cost:
            return True
        else:
            return False
    def __le__(self, other):
        if not isinstance(other, Package):
            raise TypeError("Input item is not a instance of packet class")
        if self.cost <= other.cost:
            return True
        else:
            return False
    def __ne_(self, other):
        if not isinstance(other, Package):
            raise TypeError("Input item is not a instance of packet class")
        if self.cost != other.cost:
            return True
        else:
            return False

def getNumberPattern():
    pattern = r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
    m = re.search(pattern, "The IP is 215.68.0.94")
    print(m[0])
getNumberPattern()
p1 = Package("35035", "53936")
print(p1)