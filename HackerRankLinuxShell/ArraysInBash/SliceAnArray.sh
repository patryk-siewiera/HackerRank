#!/usr/bin/env bash

while read n
do
    unix=("${unix[@]}" $n)
done

echo ${unix[@]:3:5}
