#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Counting Valleys : https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    upDown = 0
    result = 0

    for i in range(steps):
        if path[i] == "U":
            upDown = upDown + 1
        else:
            upDown = upDown - 1
        
        if upDown == 0:
            if path[i] == "U":
                result += 1
    
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

