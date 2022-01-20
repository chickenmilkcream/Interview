#!/bin/bash

echo 'YOYOYO what number would you like to sum up to? '
read num

if [[ -n ${num//[0-9]/} ]]; then
    echo "No letters or negative numbers please!"
    exit 1
fi

if [ -z "$num" ]
  then
    echo "No argument supplied"
    exit 1
fi

i=0
acc=0

while [ $i -ne $num ]
do
        i=$(($i+1))
        acc=$(($acc + $i))
done

echo  "The sum of numbers up to $num is $acc"