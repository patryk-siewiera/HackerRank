#!/usr/bin/env bash

while read val1
do
echo $val1 > text.txt
done

cat text.txt

