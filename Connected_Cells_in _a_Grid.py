# Link - https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
#!/bin/python3

import math
import os
import random
import re
import sys


n=int(input())
m=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
def check(i,j):
    if i<0 or j<0 or i>=n or j>=m or l[i][j]==-1 or l[i][j]==0:
        return 0
    else:
        l[i][j]=-1
        return 1+(check(i,j+1)+check(i,j-1)+check(i+1,j)+check(i-1,j+1)+check(i-1,j-1)+check(i,j+1)+check(i+1,j-1)+check(i+1,j+1))

res= -1
for i in range(n):
    for j in range(m):
        if l[i][j]==1:
            res=max(res,check(i,j))
print(res)
