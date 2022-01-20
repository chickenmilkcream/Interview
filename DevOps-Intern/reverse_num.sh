#!/bin/bash

echo 'YOYOYO what number would you like to reverse? '
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

digit=0
reverse_num=0

while [ $num -gt 0 ]
do
    digit=$(( $num % 10 ))                         # get rightmost digit
    reverse_num=$(( $reverse_num * 10 + $digit  )) # store the rightmost digit in reverse_num
    num=$(( $num / 10 ))                           # divide by 10 to get to the next digit
done

echo  "Reverse order is $reverse_num"