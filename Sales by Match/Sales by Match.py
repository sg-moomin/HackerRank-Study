#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('jupyter nbconvert --to script Sales by Match.ipynb')


# In[ ]:


#Sales by Match : https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]


def sockMerchant(n, ar):
    checkList =  [0] * n
    visite =  [False] * n
    result = 0
    
    for i in range(n):
        if visite[i] == False:
            checkList[i] += 1
            visite[i] = True
            minSize = ar[i]
            for j in range(i, n):
                if minSize == ar[j]:
                    if visite[j] == False:
                        visite[j] = True
                        checkList[i] += 1

            result += int(checkList[i] / 2)

    return result
    
print(sockMerchant(n, ar))

