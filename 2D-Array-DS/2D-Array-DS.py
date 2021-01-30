#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    checkList = [[False for _ in range(6)] for _ in range(6)]


    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != 0:
                checkList[i][j] = True
            
    result = -54
    maxSize = 0
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            # if checkList[i][j] == True:
                maxSize = (arr[i][j] + arr[i][j+1] +
                           arr[i][j+2] + arr[i+1][j+1]+
                           arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
                if maxSize >= result:
                    result = maxSize
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

