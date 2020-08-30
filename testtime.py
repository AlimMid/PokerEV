import time
import random
import Cards
import numpy as nm
h=nm.random.choice(52,7,replace=False)
p=h.astype(int)
print(h,p)

S=[0,0,0,0]
def SuiteL(H):
    C=[x//13 for x in H]
    for x in C: S[x]+=1
    return S

S1=[0,0,0,0]
def SuiteT(H):
    C=(x//13 for x in H)
    for x in C: S1[x]+=1
    return S1

def Suite(H):
    s=nm.zeros(4,int)
    c=H//13
    for x in c: s[x]+=1
    return s

start = time.clock()
for i in range(1000000):
    x=Suite(h)
t=time.clock()-start
print('массив чисел numpy 1000000 итераций (сек)',t)

start = time.clock()
for i in range(1000000):
    x=Suite(p)
t=time.clock()-start
print('массив чисел numpy 1000000 итераций (сек)',t)




'''
for i in range(1000000):
    x=SuiteL(h)
t=time.clock()-start
print('список чисел 1000000 итераций (сек)',t)

start = time.clock()
for i in range(1000000):
    x=SuiteT(p)
t=time.clock()-start
print('кортеж чисел 1000000 итераций (сек)',t)
'''

