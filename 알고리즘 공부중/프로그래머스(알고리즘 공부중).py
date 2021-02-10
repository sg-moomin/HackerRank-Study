#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = input()
sum = 0

for i in range(len(n)):
    sum += int(n[i])
    
    
if int(n) % sum == 0:
    print(True)
else:
    print(False)



# In[23]:


number = [5, 0, 2, 7]
answer = [] * len(number)

number = sorted(number)

for i in range(len(number)):
    for j in range(i, len(number)):
        if i != j:
            print(number[i], number[j] , number[i] + number[j])
            answer.append(number[i] + number[j])
        
        
answer = list(set(answer))
# answer = list(answer)
# return(answer)


print(answer, answer[0] + answer[2])


# In[120]:


n = 10
result = [] * n
checkList = [False] * n
countList = [] * n



for i in range(2, n + 1):
    result.append(i)
    
print(result)
        
for i in range(len(result)):
    if result[i] == 2:
        print("result[i] : ", result[i])
        countList[i] = result[i]
        continue
    
    for j in range(i):
        print(i, j, result[i])
            
#         if int(result[i] % result[j]) != 0:
#             print(result[i])
#         else:
#             print(result[i], "t")



print(countList)


# In[103]:


3 % 1


# In[90]:


part = ["mislav", "stanko", "mislav", "ana"]
checkList = [False] * len(part)
answer = ''
# point = [1] * len(part)
point = 0:
com = ["stanko", "ana", "mislav"]

for i in range(len(com)):
    for j in range(len(part)):
        point = part.count(i)
        if point == 1:
            if com[i] in part[j]:
                checkList[j] = True
                continue
        else:
            

print(checkList, point)
for i in range(len(checkList)):
    if checkList[i] == False or point[i] == 1:
        answer += part[i]
        
print(answer)
            
            


# In[174]:


a = ["leo", "kiki", "eden"]
b = ["eden", "kiki"]
checkList = [False] * len(a)
result = []
for i in a:
    result.append(a.count(i))

a = sorted(a)
b = sorted(b)
print(a, b)
temp = ''


for i in range(len(b)):
    if a[i] is not b[i]:
        temp = a[i]
        
if temp is not '':
    print(temp)
else:
    print(a[len(a) - 1])
        

    
# a = list(enumerate(a))
# print(a)

# for i, v in enumerate(b):
#     for j in range(len(a)):
#         if v == a[j] and result[j] == 1:
#             checkList[j] = True
        
        
#         if result[j] > 1:
#             print(a[j]) 
#             continue
            
            


# In[1]:


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
   
def solution(participant, completion):    

    answer = ''
    temp = ''
    num = ""
    result = int(len(participant) - 1)

    participant.sort(reverse=False)
    completion.sort(reverse=False)
    
    for i in range(len(completion)):
        if completion[i] is not participant[i]:
            temp = str(participant[i])
                 
            
            
    if temp != num:
        answer = temp
    else:
        answer = participant[result]

    return answer




solution(participant, completion)


# In[60]:


# 기능개발 

from collections import deque
import math
math.ceil((100 - 5) / 3)
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
prog = deque(progresses)
speed = deque(speeds)
maxResult = []
numberSum = 100
tmp = 0
result = []


for i in range(len(progresses)):
    a = prog.popleft()
    b = speed.popleft()
    tmp = math.ceil(numberSum - a) / b
#     if int((numberSum - a) % b) == 0: 
#         tmp = int((numberSum - a) / b)
#     else:
#         tmp = int((numberSum - a) / b) + 1

    maxResult.append(tmp)
    

    
number = 1
# maxSize = maxResult[0]
for i in range(len(maxResult)):
    try:
        if maxResult[i] < maxResult[i + 1]:
            result.append(number)
            number = 1
        else:
            maxResult[i + 1] = maxResult[i]
            number += 1
            
    except IndexError:
        result.append(number)
        
print(result)    
    
# number = 1
# maxSize = maxResult[0]
# for i in range(1, len(maxResult)):
#     print("maxsize  : ",  maxSize, maxResult[i])
#     if maxSize > maxResult[i]:
#         number += 1
#         maxSize = maxSize - maxResult[i]
#     else:
#         result.append(number)
#         number = 1
           
#     if i == (len(maxResult) - 1):
#         result.append(number)   
        
# print(result)    


# In[24]:


progresses = [93, 30, 55]
speeds = [1, 30, 5]
prog = deque(progresses)
speed = deque(speeds)

maxsize = prog.popleft()
if maxsize > prog.popleft():
    print(11)
else:
    print(22)


# print(prog, speed)


# In[51]:



progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def aaa(progresses, speeds):  
    from collections import deque

    return progresses


aaa(progresses, speeds)


# In[70]:


# K번째수 

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []


for i, j, k in commands:
    result = array[i-1:j]
    result.sort()
    answer.append(result[k - 1])

print(answer)
    


# In[4]:


# 가장 큰 수

number = [3, 30, 34, 5, 9]
result = []

for i in number:
    result.append(str(i))
    
print(result[0][0])    

result.sort(key=lambda x : x*3, reverse=True)
# for i in range(len(result)):
#     try:
#         if result[i][0] == result[i + 1][0]:
#             if(result[i][0] > result[i][1]):
#                 result[i], result[i + 1] = result[i + 1], result[i]
    
#     except IndexError:
#         continue
        
        
# print(result)

print(''.join(result))


# In[133]:


# 가장 큰 수

number = [3, 30, 34, 5, 9]
result = list(map(str, number))
print(result)
result.sort(key=lambda x : x*3, reverse = True)    

print(int(''.join(result)))   


# In[78]:


# 모의고사 
import math 
math1 = [1, 2, 3, 4, 5]
math2 = [2, 1, 2, 3, 2, 4, 2, 5]
math3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
answer = [1,3,2,4,2]
check = [0] * 3
result = []

math1 = math1 * math.ceil(len(answer) / len(math1))
math2 = math2 * math.ceil(len(answer) / len(math2))
math3 = math3 * math.ceil(len(answer) / len(math3))

    


for i in range(len(answer)):

    if answer[i] == math1[i]:
        check[0] += 1
        maxSize = False
    
    if answer[i] == math2[i]:
        check[1] += 1
        maxSize = False

    if answer[i] == math3[i]:
        check[2] += 1
        maxSize = False

    if check[0] == check[1] and check[1] == check[2]:
        maxSize = True
    
    
maxSum = 0 
for i in range(len(check)):
    try:
        if maxSize == True:
            result = [1, 2, 3]
            break
        
        if check[i] < check[i+1]:
            maxSum = i
        
    except IndexError:
        continue
        
if len(result) == 0:
    result.append(maxSum + 1)    
    
# maxSize = check[0]
# for i in range(1, len(check)):
#     if check[i] != 0 
#         if maxSize == check[i] and maxSize == check[i + 1]:
        
        
        
print(result)


# In[7]:


5 % 2


# In[84]:


from itertools import cycle

math1 = [1, 2, 3, 4, 5]
math2 = [2, 1, 2, 3, 2, 4, 2, 5]
math3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
answer = [1,3,2,4,2]
check = [0] * 3
result = []


for number1, number2, number3, answer in zip(cycle(math1),cycle(math2),cycle(math3), answer):
    if number1 == answer:
        check[0] += 1
    
    if number2 == answer:
        check[1] += 1

    if number3 == answer:
        check[2] += 1

maxSize = max(check)
# for i in range(len(check)):
#     if check[i] == maxSize:
#         print(check[i])
#         result.append(i+1)
# check = dict(check)
# if check.count(maxSize) != 0:
    

# else:
#     result.append(check.index(maxSize) + 1)
# print(check)
# print(check.index(maxSize))

print(result)


# In[73]:


import math 
math.ceil(12 / 5)


# In[102]:


# 체육복
# from ceil import math
n = 5
lost = [2, 4]
reserve = [3]
nLost = set(lost) - set(reserve)
nRes = set(reserve) - set(lost)

print(new_lost)
reserveCheck = [False] * len(reserve)
# print(reserveCheck)
ready = n - len(lost)
Bready = 0

for i in lost:
    for j in range(len(reserve)):
        print(i, j)
        if reserveCheck[j] == False:
#             print(reserve[j] + 1, reserve[j] - 1)
            if (reserve[j] + 1) == i or (reserve[j] - 1) == i:
                reserveCheck[j] = True
                Bready += 1
                break
        else:
            continue
                
print(ready, Bready)



# In[120]:


# 체육복
# from ceil import math
n = 5
lost = [2, 4]
reserve = [3]
nLost = set(lost) - set(reserve)
nRes = set(reserve) - set(lost)
# nRes = list(nRes)

reserveCheck = [False] * len(reserve)
# print(reserveCheck)
ready = n - len(lost)
Bready = 0

for i in nLost:
    Frist = i - 1
    Last = i + 1
    
    if Frist in nRes:
        nRes.remove(Frist)
    elif Last in nRes:
        nRes.remove(Last)
    else:
        n = n - 1
        
print(n)
    


# In[26]:


#  타겟 넘버
number = [1,1,1,1,1]
checkList = [False] * len(number)
# checkList = [[False for i in range(number)] for j in range(number)]
target = 3
count = 0

for i in range(len(number)):
    numbers = sum(number) - target
    for j in range(len(number)):
        if checkList[j] == False:
            numbers = numbers - number[j]
            if numbers == 0:
                checkList[j - 1] == True
                count += 1

                
print(count)
                
            


# In[31]:


#  타겟 넘버
number = [1,1,1,1,1]
checkList = [False] * len(number)
target = 3

def so(number, target):
    if number == []:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return so(number[1:], target+number[0]) + so(number[1:], target-number[0])

so(number, target)                
            


# In[30]:


number = [1,1,1,1,1]
number[1:]


# In[36]:


# N으로 표현 
import math
n = 5
number = 31168


count = 0
if n > 9 or number % n != 0:
    print(-1)
    
count = 0
numberSum = number * n
numberSumCheck = [False] * len(str(numberSum))

# for i in range(len(numberSum))




result = 0


while(result != number):
#     result = numberSum / n
#     print(count)
    if int(str(n) + str(n)) + n == numberSum:
        count = count + 3
    
    if number != result:
        result = numberSum / n
        count += 1


print(count)


# In[12]:


# N으로 표현 
import math
n = 5
number = 12


count = 0
if n > 9 :
    print(-1)
    
count = 0
numberSum = number * n
numberSumStr = str(numberSum)
numberSumCount = 0
numberSumCheck = False

for i in range(len(numberSumStr)):
    if numberSumStr[i] == str(n):
        numberSumCount += 1
        numberSumCheck = True
    else:
        numberSumCheck = False
        break


resultsum = 0
result = numberSum
while(result != number):
    print(result, resultsum)
    if numberSumCheck == True:
        count = numberSumCount + 1
        break
    
    if (result + n) / n == number and str(result) == str(n) * len(str(result)):
        result = int(result / n)
        count = len(str(result)) + 1
        break
        
    else:
        result = result - n
        resultsum += 1
    
    
    if resultsum > 8:
        count = -1
        break
    
    
if count > 8:
    print(-1)
else:
    print(count)


# In[46]:


for i in range(20):
    print(5 ** i)


# In[57]:


len(str(54))


# In[5]:


if str(55) == 5 * len(str(55)):
    print(True)
else:
    print(False, 5 * len(str(55)))


# In[8]:


str(5) * 6


# In[ ]:




