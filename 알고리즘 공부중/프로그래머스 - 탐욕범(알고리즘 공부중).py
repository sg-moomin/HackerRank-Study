#!/usr/bin/env python
# coding: utf-8

# In[38]:


ord('J') - ord('A')


# In[35]:


a1 = ord('J') - ord('A')
a2 = ord('E') - ord('A')
a3 = ord('R') - ord('A')
a4 = ord('O') - ord('A')
a5 = ord('E') - ord('A')
a6 = ord('N') - ord('A')

result = a1 + a2 + a3 + a4 + a5 + a6 - 5

print(a1, a2, a3, a4, a5, a6, result)


# In[8]:


a1 = ord('J') - ord('A')
a2 = ord('A') - ord('A')
a3 = ord('N') - ord('A')
result = a1 + a2 + a3

print(result)


# In[9]:


a1 = ord('J') - ord('A')
a2 = ord('A') - ord('A')
a3 = ord('Z') - ord('A')
result = a1 + a2 + a3

print(result)


# In[27]:


ord('Z') - ord('A') - 26


# In[80]:


import math

checkNumber = math.ceil((ord('Z') - ord('A')) / 2)
checks = 26
name = "JEROEN"
count = 0


for i in range(len(name)):
    number = min(ord(name[i]) - ord('A') , (ord('Z') - ord(name[i]) + 1))
    if number == 0:
        continue
#     leftMove = 1
#     rightMove = 1
        
#     while name[i - leftMove] == ord('A'):
#         leftMove += 1
#     while name[i + rightMove] == ord('A'):
#         rightMove += 1
    
#     count += number
#     count = min(leftMove, rightMove)
    
    
print(count)


# In[48]:


name = "AAABAABB"
name = list(name)
moveCheck = 0 
leftMove = 1
rightMove = 1


while True:
    
    
    
    

for i in range(len(name)):
    if name[i] == "A":
        
        
        
    else:
        rightMove += 1
        movecheck = rightMove
    
    

    
while()


# In[106]:


name = "AAABAABB"
left = 1
right = 1

startPoint = 0
endPoint = len(name)


name = list(name)
               
for i in range(len(name)):
    if name[i] == "A":
        continue
    else:
        startPoint
        
        for j in range(i, len(name)):
            
    
    


# In[96]:


name = "ABCDEFG"
name[-1]


# In[ ]:




