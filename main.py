import Cards
import PF
import numpy as n
import Cards_old2
import time
import random
reps = 100000
repslist = range(reps)
RC=n.arange(52)
R=n.random.choice(52,4,replace=False)
a=[R[0],R[1]]
b=[R[2],R[3]]
A=PF.HandStr(a)
B=PF.HandStr(b)
Rcards=n.delete(RC,R,None)
print(A,B)
start = time.clock()
E=PF.eq(a,b)
print('эквити ',A,'против',B,'равен')
print(E)
t=time.clock()-start
print('время вычисления еквити (сек) - ',t)
input()
print(A,B)


