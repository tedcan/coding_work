#!/bin/bash

export SJAR=/usr/lib/hadoop/contrib/streaming/hadoop-streaming-0.20.2+737.jar

hadoop fs -copyFromLocal $1 medwiki

hadoop jar $SJAR -file $(pwd)/mapper1.py -mapper $(pwd)/mapper1.py -file $(pwd)/reducer1.py -reducer $(pwd)/reducer1.py -input medwiki -output mw1

if [ "$#" = "2" ]; 
then
hadoop jar $SJAR -file $(pwd)/mapper2.py -mapper $(pwd)/mapper2.py -file $(pwd)/reducer2.py -reducer $(pwd)/reducer2.py -input mw1 -output mw2_1 -numReduceTasks $2
else
hadoop jar $SJAR -file $(pwd)/mapper2.py -mapper $(pwd)/mapper2.py -file $(pwd)/reducer2.py -reducer $(pwd)/reducer2.py -input mw1 -output mw2_1 
fi 

for i in `seq 2 30`
do
	ind=$(($i-1))
	input=$(printf "mw2_%s" "$ind")
	output=$(printf "mw2_%s" "$i")

if [ "$#" = "2" ]; 
then
	hadoop jar $SJAR -file $(pwd)/mapper2.py -mapper $(pwd)/mapper2.py -file $(pwd)/reducer2.py -reducer $(pwd)/reducer2.py -input $input -output $output -numReduceTasks $2
else
	hadoop jar $SJAR -file $(pwd)/mapper2.py -mapper $(pwd)/mapper2.py -file $(pwd)/reducer2.py -reducer $(pwd)/reducer2.py -input $input -output $output 
fi

done

hadoop jar $SJAR -file $(pwd)/mapper3.py -mapper $(pwd)/mapper3.py -file $(pwd)/reducer3.py -reducer $(pwd)/reducer3.py -input mw2_30 -output mw3

hadoop fs -copyToLocal mw3 output

hadoop fs -rmr medwiki
hadoop fs -rmr mw1

for i in `seq 1 30`
do
	hadoop fs -rmr $(printf "mw2_%s" "$i")
done

hadoop fs -rmr mw3
