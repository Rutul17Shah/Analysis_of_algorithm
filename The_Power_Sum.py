# Link - https://www.hackerrank.com/challenges/the-power-sum/problem 
#!/bin/python3

import math
import os
import random
import re
import sys
X = int(input())
N = int(input())

def rec(X,N,start):
    count = 0 
    for i in range(start,X):
        ans = X-i**N
        if ans == 0:
            count += 1
        if ans> 0 :
            count += rec(ans,N,i+1)
        if ans<0:
            continue   
    return count
    
print(rec(X,N,1))
 