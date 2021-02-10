#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 2D Array - DS
# arr = [[1, 1, 1, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 0],
#         [0, 0, 2, 4, 4, 0],
#         [0, 0, 0, 2, 0, 0],
#         [0, 0, 1, 2, 4, 0]]

arr = [[-1, -1, 0, -9, -2, -2],
[-2, -1, -6, -8, -2, -5],
[-1, -1, -1, -2, -3, -4],
[-1, -9, -2, -4, -4, -5],
[-7, -3, -3, -2, -9, -9],
[-1, -3, -1, -2, -4, -5]]


checkList = [[False for _ in range(6)] for _ in range(6)]


for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] >= 0:
            checkList[i][j] = True
        else:
            checkList[i][j] == False
            
        
result = -54 # -9가 6개라고 가정 
for i in range(len(arr) - 2):
    for j in range(len(arr) - 2):
#         if checkList[i][j] == True:
            maxSize = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]+
                       arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            if maxSize >= result:
                   result = maxSize

        
print(result)


# In[12]:


a = [1, 2, 3, 4, 5]
d = 4
result = a

# result = a

# for i in range(d):
    
    
#     tmp = result[0]7
    
    
    
#     for j in range(len(a)):
#         print(tmp)
#         if j == (len(a) - 1):
#             result[j] = tmp
#         else:
#             result[j] = result[j + 1]
#     print(result)


listCount = len(a) - d
for i in range(listCount):
    fristTmp = result[len(a) - 1]
    lastTmp = result[0]
    
    #     for j in range(len(a) - 1):
#         print(j)
#         if j == 0:
#             fristTmp = result[len(a) - 1]
#             lastTmp = result[j]
#             result[j] = fristTmp
#         else:
# #             result[j], result[j+1] = result[j+1], result[j]
#             result[j+1] = result[j]

print(result)


# In[27]:


t = 2

def minimumBribes(q):
    resultList = []
    result = 0
    for i in range(1, len(q)+1):
        resultList.append(i)
      
    checkList = [False] * len(q)
    check, count = 0, 0
    for i in range(len(q) - 1, -1, -1)
        if check != 2:
            resultList[i], resultList[i-1] = resultList[i-1], resultList[i]
            check += 1
            count += 1
        else:
            check = 0
            continue

    if resultList == q:
        print(count)
    else:
        print("Too chaotic")
        
    
# for t_itr in range(t):
#     n = int(input())
#     q = list(map(int, input().rstrip().split()))
#     minimumBribes(q)
    

# for i in range(len(q)):
        
        


# In[33]:


n = 5
# q = [1, 2, 3, 4, 5]
q = [2, 1, 5, 3, 4]    
resultList = []
result = 0 
checkList = [False] * len(q)
check, count = 0, 0
    
for i in range(1, len(q)+1):
    resultList.append(i)
    
for i in range(len(q) - 1, 0, -1):
    if check != 2:
        resultList[i], resultList[i-1] = resultList[i-1], resultList[i]
        check += 1
        count += 1
    else:
        check = 0
        continue

print(resultList, q)
        
if resultList == q:
    print(count)
else:
    print("Too chaotic")
        


# In[6]:


n = 5
q = [2, 1, 5, 3, 4]
# q = [1, 2, 5, 3, 7, 8, 6, 4] 
resultList = []
result = 0 
checkList = [False] * len(q)
check, count, chaotic = 0, 0, 0


for i in range(1, len(q)+1):
    resultList.append(i)
    
for i in range(len(q) - 1, 0, -1):
    print(q)
    if checkList[i] == False:
        if q[i] == resultList[i]:
            checkList[i] = True
            continue
        elif q[i - 1] == resultList[i]:
            check += 1
            checkList[i] = True
#             checkList[i], checkList[i-1] = True, True
        elif q[i - 2] == resultList[i]: 
            check += 2
            checkList[i] = True
#             checkList[i], checkList[i-1], checkList[i-2] = True, True, True        
        else:
#             if q[i] == resultList[i+1] or q[i] == resultList[i+2]:
#                 check += 1
#                 continue
#             else:
             chaotic += 1
    else:
        continue

if (chaotic * check) == 0:
    print(check)
else:
    print("Too chaotic")
        


# In[106]:


d = 3
a = [1, 2, 3, 4, 5]
result = [0] * len(a)
count = len(a) - d
def rotLeft(a, d): 
    for i in range(len(a)):
        print(i, i + count)
        if (i + count) > (len(a) - 1):
            result[(i + count) - len(a)] = a[i]
        else:
            result[i + count] = a[i]
#         print(a)
#         tmp = a[int(len(a) - 1)]
#         for j in range(len(a) - 1, 0, -1):
#             print(j)
#             if j == (len(a)):
#                 a[j] = tmp
#             else:
#                 a[j - 1], a[j] = a[j], a[j - 1]
    
    return result
print(rotLeft(a, d))


# In[20]:


arr = [4, 3, 1, 2]

count = 0
for i in range(len(arr)):
    if arr[i] != i+1:
        newNumber = i
        while(arr[newNumber] != i+1):
            newNumber += 1
        
        arr[i], arr[newNumber] = arr[newNumber], arr[i]
        count += 1
#         for j in range(i, len(arr)):
#             if arr[j] == i + 1:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 count += 1

                
print(count)
print(arr)


# In[80]:


arr = [4, 3, 1, 2]
sort = sorted(arr)
resultList = {v: i for i,v in enumerate(arr)}
count = 0

for i in range(len(arr)):
    countList = sort[i]
    if countList != resultList[i]:
        to_swap_ix = resultList[countList]
        arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix]
        resultList[i] = to_swap_ix
        resultList[countList] = i
        swaps += 1
    print(sort[i], v, to_swap_ix, index_dict[v], index_dict[sort[i]])
#     print(resultList)
    
print(swaps)


# In[192]:


arr = [3, 7, 6, 9, 1, 8, 10, 4, 2, 5]
sort = sorted(arr)
resultList = {j : i for i, j in enumerate(arr)}
count = 0
for i, j in enumerate(arr):
    countList = sort[i]
    if countList != j:
        tmpList = resultList[countList]
        arr[tmpList], arr[i] = arr[i], arr[tmpList]
        resultList[j] = tmpList
        resultList[countList] = i
        count += 1
        
print(count, arr)
        


# for i in range(arr):
#     resultList[i] = arr[i]
    
# for i in range(len(arr)):
#     countList = sort[i]
#     if countList != resultList[i]:
#         temp = resultList[countList]
        
        


# In[197]:


arr = [4, 3, 1, 2]
count = 0

for i in range(len(arr)):
    if arr[i] == (i+1):
        continue
    
    arr[i], arr[arr[i] - 1] = arr[arr[i] - 1] ,arr[i]
    count += 1
    
print(count)


# In[179]:


arr = [4, 3, 1, 2]
c = {j : i for i, j in enumerate(arr)}

print(c, c[index[0]])
    


# In[5]:


n = 5
arr = [2, 3, 4, 1, 5]


print(set())


# In[11]:


# Sparse Arrays
strings = ['aba', 'baba', 'aba','xzxb']
queries = ['aba', 'xzxb', 'ab']
result = []
print(result)
for i in range(len(queries)):
    count  = 0
    for j in range(len(strings)):
        if queries[i] == strings[j]:
            count += 1
        else:
            continue
            
            
    result.append(count)
    
print(result)
    


# In[3]:


strings = ['aba', 'baba', 'aba','xzxb']
queries = ['aba', 'xzxb', 'ab']

count = 0
for i in range(len(strings)):
    if "aba" == strings[i]:
        count += 1
        

print(count)
        


# In[50]:


# Hash Tables: Ransom Note
magazine = ["two", "times", "three", "is", "not", "four"]
note = ["two", "times", "two", "is", "four"]
noteCheck = [False] * len(note)
magazineCheck = [False] * len(magazine)

# mResult = dict()
# nResult = dict()

for i in range(len(note)):
    for j in range(len(magazine)):
        if magazineCheck[j] == False:
            if magazine[j] == note[i]:
                noteCheck[i] = True
                magazineCheck[j] = True
            else:
                continue
        else:
            continue

# for i in range(len(noteCheck)):
if False in noteCheck:
    print("NO")
else:
    print("YES")


# In[117]:


magazine = ["ive", "got", "a", "lovely", "bunch", "of", "coconuts"]
note = ["ive", "got", "some", "coconuts"]
noteCheck = [False] * len(note)
magazineCheck = [False] * len(magazine)

mMaga = {i : v for i, v in enumerate(magazine)}
mNote = {i : v for i, v in enumerate(note)}


for i in range(len(note)):
    
    if mNote[i] in mMaga.values() and magazineCheck[int(mMaga.get(mNote[i]))] == False:
        print(mNote[i] , int(mMaga.get(mNote[i])))
        noteCheck[i] = True
        magazineCheck[int(mMaga.get(mNote[i]))] = True
    else:
        continue
 

 

print(magazineCheck, noteCheck)
            
if False in noteCheck:
    print("NO")
else:
    print("YES")
    
    


# In[130]:


magazine = ["two", "got", "two", "lovely", "two", "of", "two"]
note = ["two"]

mMaga = {i : v for i, v in enumerate(magazine)}
mNote = {i : v for i, v in enumerate(note)}

print(mMaga, mNote)

print(mMaga.get("two"))

del(mMaga[mMaga.get("two")])
    
print(mNote.get("two"))
print(mMaga[mNote.get("two")])

if "two" in mMaga.values():
    print(mMaga.keys())


# In[139]:


magazine = ["ive", "got", "a", "lovely", "bunch", "of", "coconuts"]
note = ["ive", "got", "some", "coconuts"]
noteCheck = [False] * len(note)
magazineCheck = [False] * len(magazine)

mMaga = {j : k for j, k in enumerate(magazine)}
print(mMaga)

for i, v in enumerate(note):
    if note[i] in mMaga.values() and magazineCheck[int(mMaga.get(v))] == False:
        print(mNote[i] , int(mMaga.get(v)))
        noteCheck[i] = True
        magazineCheck[int(mMaga.get(v))] = True
    else:
        continue
 

 

print(magazineCheck, noteCheck)
            
if False in noteCheck:
    print("NO")
else:
    print("YES")
    
    


# In[178]:


magazine = ["ive", "got", "a", "lovely", "bunch", "of", "coconuts"]
note = ["ive", "got", "some", "coconuts"]
noteCheck = [False] * len(note)
magazineCheck = [False] * len(magazine)

mMaga = {j : k for j, k in enumerate(magazine)}
mno = {j : k for j, k in enumerate(note)}

dddict = list(mno.items())
# dddict.



# for i, (key, element) in enumerate(mno.items()):
#     if mno[i] in mMaga.values():
    
#     print(i, key, element)
#     print(mMaga[i])


# In[ ]:




