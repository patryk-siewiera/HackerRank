#!/usr/bin/env bash

while read n
do
    unix=("${unix[@]}" $n)
done

echo ${unix[@]}
