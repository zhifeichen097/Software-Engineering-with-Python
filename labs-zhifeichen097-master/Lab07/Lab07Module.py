#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18 >
#    Date:         <Feb.27,2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import math
class Rectangle:
    def __init__(self,lowerLeft, upperRight):
        self.lowerLeft =  lowerLeft
        self.upperRight = upperRight
        #print(lowerLeft,upperRight)

        if self.upperRight[0] <= self.lowerLeft[0] or self.upperRight[1] <= self.lowerLeft[1]:
            raise ValueError("The lower left or the upper right x and must be in the correct form")

    def isSquare (self):
        #print(self.upperRight[0] - self.lowerLeft[0])
        #print(self.upperRight[1] - self.lowerLeft[1])
        if abs((self.upperRight[0] - self.lowerLeft[0]) - (self.upperRight[1] - self.lowerLeft[1])) < 0.0001:
            return True
        else:
            return False

    #and rect.lowerLeft[0]
    def intersectsWith (self,rect):
        if (self.lowerLeft[0] < rect.lowerLeft[0]  < self.upperRight[0] and self.lowerLeft[1] < rect.lowerLeft[1]  < self.upperRight[1]) or (self.lowerLeft[0] < rect.upperRight[0]  < self.upperRight[0] and self.lowerLeft[1] < rect.upperRight[1]  < self.upperRight[1]):
            return True
        else:
            return False
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Input arugument is not an instance of the Rect class")
        selflength = abs(self.upperRight[1] - self.lowerLeft[1])
        selfwidth =  abs(self.upperRight[0] - self.lowerLeft[0])
        otherlength = abs(other.upperRight[1] - other.lowerLeft[1])
        otherwidth =  abs(other.upperRight[0] - other.lowerLeft[0])
        selfArea = selflength * selfwidth
        otherArea = otherlength * otherwidth
        # print(selfArea)
        # print(otherArea)
        # print(selfArea - otherArea)
        if selfArea - otherArea == 0:
            return True
        else:
            return False
class Circle:
    def __init__(self,center,radius):
    #print(type(args[1]))

             self.center = center
             self.radius = radius
             if self.radius < 0:
                    raise ValueError ("The radius of the circle must be greater than zero")

        # self.center = center
        # self.radius = radius
        # if self.radius < 0:
        #     raise ValueError ("The radius of the circle must be greater than zero")
        # if *args
        #super().__init__(self,lowerLeft, upperRight)
    def intersectsWith(self,other):
        if isinstance(other, Rectangle):
            other.__init__(other.lowerLeft,other.upperRight)


            radiuslowX1 = other.lowerLeft[0] - self.radius
            radiuslowX2 = other.lowerLeft[0] + self.radius

            radiusupperX1 = other.upperRight[0] - self.radius
            radiusupperX2 = other.upperRight[0] + self.radius

            radiuslowY1 = other.lowerLeft[1] - self.radius
            radiuslowY2 = other.lowerLeft[1] + self.radius

            radiusupperY1 = other.upperRight[1] - self.radius
            radiusupperY2 = other.upperRight[1] + self.radius

            if (radiuslowX1 < self.center[0] < radiuslowX2) or (radiusupperY1 < self.center[1] < radiusupperY2) or (radiuslowY1 < self.center[1] < radiuslowY2) or (radiusupperX1 < self.center[0] < radiusupperX2):
                return True
            else:
                return False

        else:
            centerDis = math.sqrt(math.pow(self.center[0] - other.center[0], 2) + math.pow(self.center[1] - other.center[1], 2))
            #print(centerDis)
            if centerDis < self.radius:
                return True
            else:
                return False



r1 = Rectangle((0.5, 1.923) ,(1.1, 2.8123))
r2 = Rectangle((0.5, 1.9), (1.1, 2.8123))
#print(type(r1))
c1 = Circle((1.0, 1.9), 1.1)
c2 = Circle((0.9, 1.9), 2.2)
print(r1.upperRight[1])
print(r1.isSquare())
print(1)
print(c1.intersectsWith(c2))
print(r1 == r2)
