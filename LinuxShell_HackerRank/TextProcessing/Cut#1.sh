#!/usr/bin/env bash

while read n
do
    echo "$n" | cut -c 3
done
