#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18 >
#    Date:         <Feb.20,2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
def extractArguments(commandline):
    match = re.findall(r'[+\\]([a-z])\s+([^+\\\s]\S*)',commandline)
    print(match)
    return sorted(match)





def extractNumerics(sentence):
    match = re.findall(r'([+-]?[\d]*[\.]?[\d]+[Ee+-]*[\d]*)', sentence)
    print(type(match[1]))
    print(match)
    return match



if __name__ == "__main__":
    extractArguments('myScript.bash +v  \i 2  +p  /local/bin/somefolder')
    extractNumerics("With the electron's charge being -1.6022e-19, some choices you have are -110, .5 and +55. Assume that pi equeals 3.1415, 'e' equals 2.7 and Na is +6.0221E+023.")
