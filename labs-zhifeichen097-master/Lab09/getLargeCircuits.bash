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
circuitfile=$(ls $circuitdir)

for filename in $circuitfile
do
    size=$(wc -c $circuitdir$filename | cut -f1 -d' ')
    if [[ $size -ge 200 ]]; then
        echo $filename | grep -o -P "[0-9]{2}-[0-9]-[0-9]{2}"
    fi
done
