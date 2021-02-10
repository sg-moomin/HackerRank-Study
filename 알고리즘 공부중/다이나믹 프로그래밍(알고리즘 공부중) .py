#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 탑다운(하향식) 보텀업(상향식)
# 다이나믹 프로그래밍 - 동적 계획법 (프로그램이 실행되는 도중에 실행)
# 메모이제이션 : 한번 계싼한 결과를 메모리 공간에 메모하는 기법 -> 다시 호출 시 그대로 가져옴 
 


# In[3]:


# 탑다운 피보나치

d_list = [0] * 100

def fib(x):
    if x == 1 or x == 2:
        return 1
    if d_list[x] != 0:
        return d_list[x]
    else:
        d_list[x] = fib(x - 1) + fib(x - 2)
        return d_list[x]
    
print(fib(99))


# In[5]:


# 보텀업 피보나치

d_list [0] * 100
d_list[1] = 1
d_list[2] = 1
n = 99

for i in range(n):
    d_list[i] = d_list[i - 1] + d_list[i - 2]
print(d_list[n])


# In[6]:


# c++의 경우 long long을 하더라도 오버플로우가 발생 


# In[1]:


# 개미 전사 문제 
N = int(input())
result = 0
array = list(map(int, input().split()))
antList = [0] * 100


antList[0] = array[0]
antList[1] = max(array[0], array[1])

for i in range(2, N):
    antList[i] = max(antList[i-1], antList[i-2] + array[i])

print(antList[N - 1])


# In[7]:


# 1로 만들기 문제 
x = int(input())
result = x

count = [0] * 30001

for i in range(2, x + 1):
    count[i] = count[i - 1] + 1
    print(str("count :  "), count[i])
    if i % 2 == 0:
        count[i] = min(count[i], count[i // 2] + 1) 
    if i % 3 == 0:
        count[i] = min(count[i], count[i // 3] + 1) 
    if i % 5 == 0:
        count[i] = min(count[i], count[i // 5] + 1) 
    
    
print(count[x])



# In[4]:


if 50 / 5:
    print("11")
else:
    print("22")


# In[12]:


# 효율적인 화폐 구성 
n, m = map(int, input().split())
coin =[0] * 100


for i in range(n):
    coin[i] = int(input())

for i in range(1, n):
    if m % int(coin[i]) == 0:
        result = min(result, m / int(coin[i]))
    elif m % int(coin[i - 1]) == 0:
        result = min(result, m / int(coin[i - 1]))
    else:
        result = min(result, -1)
        
print(result)
    


# In[15]:


n, m = map(int, input().split())
coin =[]
INF = 10001
checkList = [INF] * (m + 1)


for i in range(n):
    coin.append(int(input()))

checkList[0] = 0
for i in range(n):
    for j in range(coin[i], m+1):
        if checkList[j - coin[i]] != int(INF):
            checkList[j] = min(checkList[j], checkList[j - coin[i]] + 1)
    
if checkList[m] == int(INF):
    print(-1)
else:
    print(checkList[m])


# In[8]:


# 금광 
testCase = int(input())
caseDp = []
result = 0
results = []
for i in range(testCase):
    n, m = map(int, input().split())
    case = list(map(int, input().split()))
    
    index = 0
    for i in range(n):
        caseDp.append(case[index : index + m])
        index += m
    
    for i in range(1, m): 
        for j in range(n):
            if j == 0:
                left_up = 0
            else:
                left_up = caseDp[j - 1][i - 1]
                
            if j ==  n - 1:
                left_down = 0
            else:
                left_down = caseDp[j + 1][i - 1]
            
            left = caseDp[j][i - 1]
            caseDp[j][i] = caseDp[j][i] + max(left_up, left_down, left)
   
    result = 0 
    for i in range(n):
        result = max(result, caseDp[i][m-1])
    print(result)


# In[16]:


n, m, k = map(int, input().split())

clean = []

index = 0
for i in range(n):
    text = input().split()
    clean.append(text[index : index + m])

clean = list(set(clean))


# In[ ]:


# *@.@
# ##..
# @@@#

