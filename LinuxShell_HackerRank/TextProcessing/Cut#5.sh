#!/usr/bin/env bash

cut -d $'\t' -f1-3 | while read line
do
  echo "$line"
done