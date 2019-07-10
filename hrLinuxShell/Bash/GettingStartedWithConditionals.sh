#!/usr/bin/env bash

read -n 1 letter

if [[ $letter == 'y' || $letter == 'Y' ]]; then
	echo YES
fi
if [[ $letter == 'n' || $letter == 'N' ]]; then
	echo NO
fi