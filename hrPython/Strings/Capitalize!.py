#!/bin/python3

import math
import os
import random
import re
import sys
import string


def solve(s):
    return " ".join(map(str.capitalize, s.split(" ")))


if __name__ == "__main__":
    s = input()
    result = solve(s)
    print(result)
