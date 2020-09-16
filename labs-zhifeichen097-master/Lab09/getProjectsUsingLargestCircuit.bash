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

circuitfile=$(ls -S $circuitdir | head -n 1 | grep -o -P "[0-9]{2}-[0-9]-[0-9]{2}")
grep $circuitfile $projectfile | cut -f15 -d' ' | sort -u
