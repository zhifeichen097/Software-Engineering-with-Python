#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18 >
#    Date:         <Apr.10,2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line

import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
DataPath = os.path.expanduser('~ee364/DataFolder/Lab13')

from Lab10.measurement import calculateDistance
#sourceZip, destinationZip
def getCost(sourceZip, destinationZip):
    file = os.path.join(DataPath, 'coordinates.dat')
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
#
# def loadPackages():
#     file = os.path.join(DataPath, 'packages.dat')
#     with open(file,"r") as fpack:
#         next(fpack)
#         for line in fpack:
#             #print(line.split('"'))
#             package = Package(line.split('"')[1], line.split('"')[3],line.split('"')[5])
#             for pack in packageList:
#                # if
#
# loadPackages()

class Package:
    def __init__(self,company, source, destination):
        self.company = company
        self.source = source
        self.destination = destination
        self.cost = getCost(self.source, self.destination)
    def __str__(self):
        return f"{self.source} " + "=> " + f"{self.destination}" + ", " + "Cost = $" + f"{self.cost}"

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
    ################ function overload ###################
    def __add__(self, other):
        if not isinstance(self, Package):
            raise TypeError("Input must an instance of package class")
        if not isinstance(other, Package):
            raise TypeError("Input must an instance of package class")
        if self.company != other.company:
            raise ValueError("Input must belong to the same company")
        #packlist =[]
        #packlist.append(self)
        #cost = self.cost + other.cost
        new = PackageGroup(self.company,[self, other])
        return new
class PackageGroup:
    def __init__(self, company, packages):
        self.company = company
        self.packages = packages
        self.cost = 0
        for p in packages:
            self.cost += p.cost
    def __str__(self):
        return f"{self.company}, " + "{:03d} ".format(len(self.packages)) +"Shipments, " + "Cost = $" + f"{self.cost}"
    def __repr__(self):
        return self.__str__()

    def getByZip(self, zipcodes):
        if len(zipcodes) == 0:
            raise ValueError("The input zip codes could not be empty")
        packagelist = []
        for zipcode in zipcodes:
            for package in self.packages:
                if package.source == zipcode or package.destination == zipcode:
                    packagelist.append(package)
        return sorted(packagelist,reverse=True)


    def getByState(self,states):
        packagelist = []
        if len(states) == 0:
            raise ValueError("The input zip codes could not be empty")
        for state in states:
            for package in self.packages:
                if fromZiptoState(package.source) == state or fromZiptoState(package.destination) == state:
                    packagelist.append(package)
        return sorted(packagelist, reverse=True)

    def getByCity(self,cities):
        packagelist = []
        if len(cities) == 0:
            raise ValueError("The input zip codes could not be empty")
        for city in cities:
            for package in self.packages:
                if fromZiptoCity(package.source) == city or fromZiptoCity(package.destination) == city:
                    packagelist.append(package)
        return sorted(packagelist, reverse=True)
    def __contains__(self, item):
        if not isinstance(item, Package):
            raise TypeError("Item has to be Package class")
        for package in self.packages:
            if package.source == item.source and package.destination == item.destination and package.cost == item.cost :
                return True
            else:
                return False
    # def __add__(self, other):
    #     if not isinstance(self,PackageGroup):
    #         if not isinstance(other, PackageGroup):
    #             if not isinstance(self, Package) or not isinstance(other, Package):
    #                 raise ValueError("Wrong class input")
    #             else:
    #                 return Package.__add__(self, other)
    #
    #
    #     if not isinstance(other,PackageGroup):
    #         if not isinstance(self, PackageGroup):
    #             if not isinstance(self, Package) or not isinstance(other, Package):
    #                 raise ValueError("Wrong class input")
    #             else:
    #                 return Package.__add__(self, other)
    #     if self.company != other.company:
    #         raise ValueError("Name does not match")
    # 
    #     self.packages.add(other)
    #     return self
    #
    # def __radd__(self, other):
    #     return self.__add__(other)

def fromZiptoState(zip):
    file = os.path.join(DataPath, 'coordinates.dat')
    with open(file, 'r') as fcoord:
        next(fcoord)
        for line in fcoord:
            output = re.search('\"(?P<zip>[0-9A-Z]{5})\"', line)
            #print((output["zip"]))
            # print(type(sourceZip))
            if output["zip"] == zip:
                #print(1)
                #print(line.split('"'))
                return line.split('"')[3]
def fromZiptoCity(zip):
    file = os.path.join(DataPath, 'coordinates.dat')
    with open(file, 'r') as fcoord:
        next(fcoord)
        for line in fcoord:
            output = re.search('\"(?P<zip>[0-9A-Z]{5})\"', line)
            #print((output["zip"]))
            # print(type(sourceZip))
            if output["zip"] == zip:
                #print(1)
                #print(line.split('"')[9])
                return line.split('"')[9]

fromZiptoCity("35004")


#
# p1 = Package("123","99337", "35115")
# p2 = Package("123","99337", "35115")
# p3 = Package("123","99337", "35139")
# P = PackageGroup("123",[p1,p2]).getByZip({"35115"})
# print(p3+p2)
# print(p3 in P)
# print(P + p3)
# print(P)