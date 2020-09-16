#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18 >
#    Date:         <Feb.8,2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line



DataPath = os.path.expanduser('~ee364/DataFolder/Lab03')

def getStateByCounty(county):
    file = os.path.join(DataPath, 'counties.dat')
    file1 = os.path.join(DataPath, 'coordinates.dat')
    file2 = os.path.join(DataPath, 'zip.dat')
    coordToCounty = {}
    CoordToZip = {}
    ZipToState = {}
    resultSet = set()
    with open (file, "r") as fcounties:
        next(fcounties)
        next(fcounties)
        for line in fcounties:
            if(len(line.split())> 3):
                coordToCounty[line.split()[0] + line.split()[1]] = line.split()[2] + ' ' + line.split()[3]
            else:
                coordToCounty[line.split()[0]+line.split()[1]] = line.split()[2]
    with open (file1, "r") as fcoord:
        next(fcoord)
        next(fcoord)
        for line in fcoord:
            CoordToZip[line.split()[0]+line.split()[1]] = line.split()[2]
   # print(CoordToZip)
    with open (file2,"r") as fzip:
        next(fzip)
        next(fzip)
        for line in fzip:
            if(len(line.split()) > 3):
                ZipToState[line.split()[3]] = line.split()[0]+' '+line.split()[1]
                #print(line.split()[0]+' '+line.split()[1])
            else:
                ZipToState[line.split()[2]] = line.split()[0]
                #print(line.split()[0])
    for element in coordToCounty:
        if(coordToCounty[element] == county):
            resultSet.add(ZipToState[CoordToZip[element]])
    if len(resultSet) == 0:
       resultSet = {}

   # print(resultSet)

    #print(coordToCounty)
    return resultSet
    #resultSet.add(coordToCounty[])
def getCount(state):
    file = os.path.join(DataPath, 'counties.dat')
    file1 = os.path.join(DataPath, 'coordinates.dat')
    file2 = os.path.join(DataPath, 'zip.dat')
    coordToCounty = {}
    ZipToCoord = {}
    ZipToState = {}
    State = set()
    result = set()
    c=0
    with open (file, "r") as fcounties:
        next(fcounties)
        next(fcounties)
        for line in fcounties:
            if(len(line.split())> 3):
                coordToCounty[line.split()[0] + line.split()[1]] = line.split()[2] + ' ' + line.split()[3]
            else:
                coordToCounty[line.split()[0]+line.split()[1]] = line.split()[2]
    with open (file1, "r") as fcoord:
        next(fcoord)
        next(fcoord)
        for line in fcoord:

            ZipToCoord[line.split()[2]] = line.split()[0]+line.split()[1]
    #print(CoordToZip)
    with open (file2,"r") as fzip:
        next(fzip)
        next(fzip)
        for line in fzip:
            if(line.split()[0] =='New'):
                ZipToState[line.split()[3]] = line.split()[0]+' '+line.split()[1]
                #print(line.split()[0]+' '+line.split()[1])
            else:
                ZipToState[line.split()[2]] = line.split()[0]
    with open (file2,"r") as fzip:
        next(fzip)
        next(fzip)
        for line in fzip:
            if(line.split()[0] =='New'):
                State.add(line.split()[0]+' '+line.split()[1])
                #print(line.split()[0]+' '+line.split()[1])
            else:
                State.add(line.split()[0])
    if state not in State:
        raise ValueError ("Invalid State Name")
    else:
        for element in ZipToState:
            c+=1
            if(ZipToState[element] == state):
                result.add(coordToCounty[ZipToCoord[element]])
  #  print(len(result))
    return (len(result))

def getReport():
    file = os.path.join(DataPath, 'students.dat')
    file1 = os.path.join(DataPath, 'calls.dat')
    nameToPhone = {}
    count = 0
    result = {}
    totalTime =0
    with open (file, "r") as fstudents:
        next(fstudents)
        next(fstudents)
        for line in fstudents:
            nameToPhone[line.split()[0]+' '+line.split()[1]] = line.split()[3]
    with open (file1,"r") as fcall:
        next(fcall)
        next(fcall)
        for element in nameToPhone:
            for line1 in fcall:
                if 'x'+(line1.split()[0]).split('-')[2] == nameToPhone[element]:
                    count+=1
                    totalTime += (line1.split()[2]).time
            result[element] = (count, totalTime)
    print(result)




    #print(len(ZipToCoord))
if __name__ == "__main__":
    getStateByCounty('St. Clair')
    getCount('New York')
    #getReport()
