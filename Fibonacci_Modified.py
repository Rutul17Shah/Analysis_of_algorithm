# Link - https://www.hackerrank.com/challenges/fibonacci-modified/problem
#!/bin/python3

import math
import os
import random
import re
import sys
a, b, n = [int(x) for x in input().split(" ")]

if n == 0:
    print(a)
if n == 1:
    print(b)

for _ in range(n-2):
    a, b = b, b*b + a
    
print(b)
