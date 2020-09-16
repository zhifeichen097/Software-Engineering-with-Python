#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18 >
#    Date:         <Feb.13,2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line



DataPath = os.path.expanduser('~ee364/DataFolder/Lab05')

def getPinFor(name,date):
    file1 = os.path.join(DataPath, 'people.dat')
    file2 = os.path.join(DataPath, 'pins.dat')
    dateList = []
    peopleList = []
    peopleToID = dict()
    dateToIndex = dict()
    c=0
    with open (file1,"r") as fpeople:
        next(fpeople)
        next(fpeople)
        for line in fpeople:
            peopleList.append(line.split()[0]+' '+line.split()[1])
            peopleToID[line.split()[0]+' '+line.split()[1]] = line.split()[3]
    #print(peopleToID)
    with open (file2,"r") as fpins:
        next(fpins)
        line1 = fpins.readline()
        print(line1.split())
        if date not in line1.split():
            raise ValueError("Date is not in the file")
        for i in range(0, 21):
            dateToIndex[line1.split()[i]] = c
            c+=1
   # print(dateList)
    if name not in peopleList:
        raise ValueError("Name is not in the file")

    #print(dateToIndex)

    with open (file2,"r") as fpins:
            next(fpins)
            next(fpins)
            for line3 in fpins:
                if peopleToID[name]== line3.split()[0]:
                    print(line3.split()[dateToIndex[date]])
    return (str(line3.split()[dateToIndex[date]]))



def getUserOf(pin,date):
    file1 = os.path.join(DataPath, 'people.dat')
    file2 = os.path.join(DataPath, 'pins.dat')
    dateList = []
    peopleList = []
    IDtoPeople = dict()
    dateToIndex = dict()
    c = 0
    error = 1
    with open(file1, "r") as fpeople:
        next(fpeople)
        next(fpeople)
        for line in fpeople:
            peopleList.append(line.split()[0] + ' ' + line.split()[1])
            IDtoPeople[line.split()[3]]= line.split()[0] + ' ' + line.split()[1]
    # print(peopleToID)
    with open(file2, "r") as fpins:
        next(fpins)
        line1 = fpins.readline()
        print(line1.split())
        if date not in line1.split():
            raise ValueError("Date is not in the file")
        for i in range(0, len(line1.split())):
            dateToIndex[line1.split()[i]] = c
            c += 1
    #print(dateToIndex)
    with open(file2, "r") as fpin1:
        next(fpin1)
        next(fpin1)
        next(fpin1)
        for line3 in fpin1:
            if pin in line3.split():
                error = 0

    if error ==1:
        raise ValueError("Pin is not in the file")
    with open(file2, "r") as fpin1:
        next(fpin1)
        next(fpin1)
        next(fpin1)
        for line3 in fpin1:

           # print(line3.split()[dateToIndex[date]])
            if(line3.split()[dateToIndex[date]] == pin):
                print(IDtoPeople[line3.split()[0]])
    return str(IDtoPeople[line3.split()[0]])

# def getUserOn(date):
#     file1 = os.path.join(DataPath, 'people.dat')
#     file2 = os.path.join(DataPath, 'pins.dat')
#     file3 = os.path.join(DataPath, 'log.dat')
#     dateList = []
#     peopleList = []
#     IDtoPeople = dict()
#     dateToIndex = dict()
#     peopleSet= set()
#     facility = dict()
#     facilityList = []
#     c = 0
#     error = 1
#     with open(file1, "r") as fpeople:
#         next(fpeople)
#         next(fpeople)
#         for line in fpeople:
#             peopleList.append(line.split()[0] + ' ' + line.split()[1])
#             IDtoPeople[line.split()[3]]= line.split()[0] + ' ' + line.split()[1]
#     # print(peopleToID)
#     with open(file2, "r") as fpins:
#         next(fpins)
#         line1 = fpins.readline()
#         print(line1.split())
#         if date not in line1.split():
#             raise ValueError("Date is not in the file")
#     with open(file2, "r") as fpins:
#         next(fpins)
#         line1 = fpins.readline()
#         print(line1.split())
#         if date not in line1.split():
#             raise ValueError("Date is not in the file")
#         for i in range(0, len(line1.split())):
#             dateToIndex[line1.split()[i]] = c
#             c += 1
#     with open(file3, "r") as flog:
#         next(flog)
#         next(flog)
#         next(flog)
#         for line in flog:
#             facilityList = line.split()[3]
#             facility[line.split()[0]+line.split()[1]]= line.split()[3]
#     with open(file2, "r") as fpins:
#         next(fpins)
#         next(fpins)
#         next(fpins)
#         for line in fpins:
#             #print(line.split()[dateToIndex[date]] )
#             if(facility[line.split()[dateToIndex[date]]] :
#                 peopleSet.add(IDtoPeople[line.split()[0]])
#     print(peopleSet)
def getDifference(slot1, slot2):
    file1 = os.path.join(DataPath, 'slots.dat')

    TimetoID = dict()
    c= 0
    result=0
    with open(file1, "r") as fslot:
        next(fslot)
        line1 = fslot.readline()
        for i in range(0, 5):
                TimetoID[line1.split()[i]] = c
                c += 1
    print(TimetoID)
    with open(file1, "r") as fslot:
        next(fslot)
        next(fslot)
        next(fslot)
        for line2 in fslot:
                if line2.split()[TimetoID[slot1]] == '1' and line2.split()[TimetoID[slot2]] == '0':
                    result += 1
    print(result)
    return result
def getCommon(slot1, slot2):
    file1 = os.path.join(DataPath, 'slots.dat')

    TimetoID = dict()
    c= 0
    result= 0
    with open(file1, "r") as fslot:
        next(fslot)
        line1 = fslot.readline()
        for i in range(0, 5):
                TimetoID[line1.split()[i]] = c
                c += 1
    print(TimetoID)
    with open(file1, "r") as fslot:
        next(fslot)
        next(fslot)
        next(fslot)
        for line2 in fslot:
                if (line2.split()[TimetoID[slot1]]) == '1' and (line2.split()[TimetoID[slot2]] =='1'):
                    result += 1
    print(result)
    return result
def getMissing(slots):
    file1 = os.path.join(DataPath, 'slots.dat')

    TimetoID = dict()
    c= 0
    result= 0
    with open(file1, "r") as fslot:
        next(fslot)
        line1 = fslot.readline()
        for i in range(0, 5):
                TimetoID[line1.split()[i]] = c
                c += 1
    print(TimetoID)

    with open(file1, "r") as fslot:
            next(fslot)
            next(fslot)
            next(fslot)
            for line2 in fslot:
                error = 0
                for element in slots:
                    if line2.split()[TimetoID[element]] == '1':
                        error = 1
                if error == 0:
                    result +=1


    print(result)
    return result

if __name__ == "__main__":
    # getPinFor('Bailey, Catherine', '03/18')
    # getUserOf('60006','01/17')
    #getUserOn('04/15')
    getDifference('11:30AM-01:20PM','01:30PM-03:20PM')
    getCommon('11:30AM-01:20PM', '03:30PM-05:20PM')
    getMissing({'11:30AM-01:20PM', '03:30PM-05:20PM'})