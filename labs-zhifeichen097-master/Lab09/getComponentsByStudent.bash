#! /bin/bash

#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18>
#    Date:         <3/20/2019>
#######################################################

DataPath=~ee364/DataFolder/Lab09
projectfile=$DataPath"/maps/projects.dat"
studentfile=$DataPath"/maps/students.dat"
circuitdir=$DataPath"/circuits/"

ID=$(grep -E "$1" $studentfile | cut -f2 -d'|')
#echo $ID
circuitfile=$(ls $circuitdir)
for filename in $circuitfile

do
    if grep -q $ID "$circuitdir$filename"; then
         grep -o -P "[A-Z]+-[0-9]+" $circuitdir$filename

    fi
done | sort -u
