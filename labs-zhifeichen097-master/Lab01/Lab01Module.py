#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18 >
#    Date:         <Jan.16,2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line

def findLongest():
   # result = 0
    lenList = []
    resultList = []
    for i in range (1, 1000000):
        resultList = []
        result = i
        while result > 1:
            if(result % 2 == 0):
                result /= 2
                resultList.append(result)
            else:
                result = 3* result + 1
                resultList.append(result)
        lenList.append(len(resultList))
    #print(lenList)
    ans = lenList.index(max(lenList))+1
    print(lenList.index(max(lenList))+1)
    return ans
def findSmallest():
    for i in range (1, 1000000):

        flag = 1
        num1 = str(i)
        for j in range (1,7):
            numx = str(j * i)
            if(len(num1) != len(numx)):
                flag = 0
                break
            sortedNum1 = sorted(num1)
            sortedNumx = sorted(numx)
            if(str(sortedNum1) != str(sortedNumx)):
                flag = 0
                break
        if(flag == 1):
            print(i)
            return i



if __name__ == "__main__":
    findLongest() # it will take about 40-50s to run
   # styr = str(42563)
   # print(sorted(styr))
    findSmallest()
    # result = 142857
    # for i in range (0, 7):
    #     print(i * result)


