#!/usr/bin/env bash
read var1
read var2
if (( "var1" > "var2" )); then
    echo 'X is greater than Y'
elif (("var1" < "var2")); then
    echo 'X is less than Y'
elif (( "var1" == "var2")); then
    echo 'X is equal to Y '
fi