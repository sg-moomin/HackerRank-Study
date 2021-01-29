#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count, result = 0, 0
    sCount = int(n / len(s))
    mCount = n % len(s)
    checkPoint = "a"

    for i in range(len(s)):
        if checkPoint == s[i]:
            count += 1

        
    count = count * sCount
    result = count
    for i in s[:mCount]:
        if checkPoint == i:
            result += 1
        
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

