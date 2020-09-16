#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18 >
#    Date:         <Feb.6,2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line



DataPath = os.path.expanduser('~ee364/DataFolder/Lab04')

def getDifference(provider1, provider2):
    file1 = os.path.join(DataPath, 'providers/')
    provider1 = str(provider1+'.dat')
    provider2 = str(provider2+'.dat')
    #file2 = os.path.join(DataPath, 'providers')
    filenameList = []
    provider1set = set()
    provider2set = set()
    for filename in os.listdir(file1):
        filenameList.append(filename)
    #print(filenameList)
    if provider1 not in filenameList:
        raise ValueError ("The provider is not in directory")
    elif provider2 not in filenameList:
        raise ValueError("The provider is not in directory")
    else:
        with open (file1 + provider1) as fprovider1:
            next(fprovider1)
            next(fprovider1)
            next(fprovider1)
            for line in fprovider1:
                provider1set.add(line.split()[0]+' '+line.split()[1])
        with open (file1 + provider2) as fprovider2:
            next(fprovider2)
            next(fprovider2)
            next(fprovider2)
            for line in fprovider2:
                provider2set.add(line.split()[0]+' '+line.split()[1])
        #print(provider1set)
        #print(provider2set)
        #print(provider1set - provider2set)
        return provider1set - provider2set
def getPriceOf(sbc, provider):
    file1 = os.path.join(DataPath, 'providers/')
    # file2 = os.path.join(DataPath, 'providers')
    provider = str(provider+'.dat')
    filenameList = []
    providerset = {}

    for filename in os.listdir(file1):
        filenameList.append(filename)
    if provider not in filenameList:
        raise ValueError("The provider is not in directory")
    else:
        with open(file1 + provider) as fprovider:
            next(fprovider)
            next(fprovider)
            next(fprovider)
            for line in fprovider:
                providerset[(line.split()[0] + ' ' + line.split()[1])] = line.split()[3]
            if sbc not in providerset:
                raise ValueError("The sbc is not in this provider")
            else:
                price = providerset[sbc].replace('$','')
                return price

def checkALlPrices(sbcSet):
    file1 = os.path.join(DataPath, 'providers/')
    providerset = {}
    minprice = {}
    #print(str(sbcSet))
    priceSet = {}
    resultSet = {}
    for element in sbcSet:
        price = 0
        for filename in os.listdir(file1):
            with open (file1 + filename, "r") as fprovider:
                next(fprovider)
                next(fprovider)
                next(fprovider)
                for line in fprovider:
                    if element == (line.split()[0] + ' ' + line.split()[1]):
                        priceSet[float(line.split()[3].replace('$',''))] = filename
        #print(priceSet)
        #print(min(priceSet))
        priceMin= min(priceSet)
        resultSet[element] = (min(priceSet)) ,(priceSet[priceMin].replace('.dat',''))
    print(resultSet)
    return resultSet

def getFilter():
    file1 = os.path.join(DataPath, 'phones.dat')
    splitList = []

    with open (file1,"r") as fphone:
        next(fphone)
        for line in fphone:
            print(line.split(',')[1].strip())
            useline = line.split(',')[1].strip()
            flag = 1
            splitList = []
            for i in range (0, len(useline)-2):
                if(useline[i] != '(' and useline[i] != ')' and useline[i] != '-' and useline[i] != ' '):
                    split = useline[i]+useline[i+1]+useline[i+2]
                    for element in split:
                        if(element == '(' or element == ')' or element == '-'):
                            flag = 0
                            break
                    if(flag == 1):
                        splitList.append(split)
            print(splitList)













if __name__ == "__main__":
    #getDifference("provider1", "provider3")
    #getPriceOf("Rasp. Pi-4702MQ","provider2")
    checkALlPrices({"Rasp. Pi-4702MQ","Rasp. Pi-4702HQ"})
    getFilter()