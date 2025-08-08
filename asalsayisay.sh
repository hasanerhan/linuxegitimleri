#!/usr/bin/env bash
##Desc: 100'e Asal Sayilari sayar
i=0
j=0
for i in $(seq 2 8)
do
	for j in $(seq 2 8)
	do
	a=$(echo $i % $j| bc)
	if  [[ $a -eq 0 ]];
	then
		
			 echo "$i bir asal sayidir"
	fi
	done	
sleep 1
done
