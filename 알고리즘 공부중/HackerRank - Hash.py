#!/usr/bin/env python
# coding: utf-8

# In[17]:


s1 = "hello"
s2 = "world"


me2 = {v : i for i, v in enumerate(s2)}
check = 0


for i, v in enumerate(s1):
    if me2.get(v) != None:
        check += 1
    else:
        continue
        
if check != 0:
    print("Yes")
else:
    print("No")


# In[55]:


# Sherlock and Anagrams



s = "abba"
# number = {v : i for i, v in enumerate(s)}
numbercount = set(s)
number = dict()
count = 0
result = ""

for i, v in enumerate(numbercount):
    number[v] = s.count(v)

    
numberCheck = [False] * len(number)
for i, v in enumerate(s):
    if number.get(v) > 1:
        count += ((number.get(v) * number.get(v)) / 2)
        
        print(number['b'])
    


# In[66]:


s = "abba"
t = frozenset("abb")
t.


# In[114]:


# Count Triplets
r = 3
arr = [1, 3, 9, 9, 27, 81]
arrSize = set(arr)

# tep = [[0] * 2] * len(arrSize)
tep = []

print(tep)

for i in range(len(arrSize)):  
    tep.append([list(arrSize)[i], arr.count(list(arrSize)[i])])


print(dict(tep))
for i in reversed(arr):
    if i * r in tep

        

    


# In[83]:


arr = [1, 3, 9, 9, 27, 81]
arrSize = set(arr)
print(list(arrSize)[1])


# In[121]:


# Count Triplets
r = 5
arr = [1, 5, 5, 25, 125]

count = 0
dict = {}
dictPairs = {}

for i in reversed(arr):
    
        if i*r in dictPairs:
                count += dictPairs[i*r]
                print("d", dictPairs[i*r])
        if i*r in dict:
                dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]
        
        dict[i] = dict.get(i, 0) + 1
        print(dict, dictPairs)
print(count)


# In[227]:


# Count Triplets
r = 5
arr = [1, 5, 5, 25, 125]
arr2 = sorted(list(set(arr)))
print(arr2)
count = 0
result = {}
lastCount = arr[len(arr) - 1]
try:
    for i in range(len(arr)):
        for j in range(len(arr2)):       
            if arr[i] * r == arr[j]:
                count += 1         
                print(arr[i], arr[j])

except IndexError:
    check = 0
    
print(count)

# for i in arr:
#         if i*r in dictPairs:
#                 count += dictPairs[i*r]
#                 print("d", dictPairs[i*r])
#         if i*r in dict:
#                 dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]
        
#         dict[i] = dict.get(i, 0) + 1
#         print(dict, dictPairs)


# In[218]:


arr = [1, 2, 2, 4]
for i in range(len(arr)):
    print(i)
    
for i in range(len(arr) + 1):
    print(i)


# In[207]:


arr = [1, 3, 9, 9, 27, 81]
list(set(arr))


num = []
for i, v in enumerate(arr):
    num.append(int(v))
    
print(list(set(num)))
number = sorted(list(set(num)))
print(number)


# In[ ]:




