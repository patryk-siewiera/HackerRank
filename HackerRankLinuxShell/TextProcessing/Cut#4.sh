#!/usr/bin/env bash

while read n
do
	echo "$n" | cut -d :
done
