#! /bin/bash

#######################################################
#    Author:      <ZhiFei Chen>
#    email:       <chen2281@purdue.edu>
#    ID:           <ee364g18>
#    Date:         <3/20/2019>
#######################################################

DataPath=~ee364/DataFolder/Lab10

file=$DataPath"/facilities.txt"
facidir=$DataPath"/facilities"
#address=$(grep -Eo "[0-9]{9}" $file)
#echo $address
address=$(grep -E "$1" $file | grep -Eo "[0-9]{9}")
#echo $address
for item in $address
do
    grep -Elr $item $facidir
done | grep -Eo "[0-9]{5}" | sort -u