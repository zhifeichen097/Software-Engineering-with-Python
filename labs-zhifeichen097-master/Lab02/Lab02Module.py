#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18 >
#    Date:         <Jan.23,2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line

DataPath = os.path.expanduser('~ee364/DataFolder/Lab02')

def getCodeFor(stateName):
    file = os.path.join(DataPath, 'zip.dat')
    zipList = []
    with open(file, 'r') as fin:
        next(fin)
        next(fin)
        for line in fin:
           # print(line.split())
            if(line.split()[0] == stateName):
                zipList.append((line.split()[2]))
       # print(len(zipList))
        print(sorted(zipList))
            #if(line.split(" "))

def getMinLatitude(stateName):
    file = os.path.join(DataPath, 'zip.dat')
    file1 = os.path.join(DataPath, 'coordinates.dat')
    zipList = []
    latList = []
    with open(file, 'r') as fin:
        next(fin)
        next(fin)
        for line in fin:
            # print(line.split())
            if (line.split()[0] == stateName):
                zipList.append(line.split()[2])
    with open(file1,'r') as fin1:
        next(fin1)
        next(fin1)
        for line in fin1:
            # print(line.split())
            if line.split()[2] in zipList:
                latList.append(line.split()[0])
        print(min(latList))

def getMaxLongitude(stateName):
    file = os.path.join(DataPath, 'zip.dat')
    file1 = os.path.join(DataPath, 'coordinates.dat')
    zipList = []
    longList = []
    with open(file, 'r') as fin:
        next(fin)
        next(fin)
        for line in fin:
            # print(line.split())
            if (line.split()[0] == stateName):
                zipList.append(line.split()[2])
    with open(file1, 'r') as fin1:
        next(fin1)
        next(fin1)
        for line in fin1:
            # print(line.split())
            if line.split()[2] in zipList:
                longList.append(float(line.split()[1]))
        print(max(longList))


def getSubMatrixSum(startRowIndex, endRowIndex, startColumnIndex, endColumnIndex):
    file = os.path.join(DataPath, 'matrix.dat')
    matrix = []
    result = 0
    with open(file, 'r') as fin:
        for line in fin:
            matrix.append(line)
        for i in range (startRowIndex, endRowIndex+1):
            for j in range (startColumnIndex, endColumnIndex+1):
                result += int(matrix[i].split(" ")[j])
    print(result)





if __name__ == "__main__":
    getCodeFor("Indiana")
    getMinLatitude("Florida")
    getMaxLongitude("Florida")
    getSubMatrixSum(0, 99, 0, 99)