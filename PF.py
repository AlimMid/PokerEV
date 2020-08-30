import math
import random
import numpy as n
Str='23456789TJQKA'
M='hdcs'
CombStr=['карта','пара','допер','сет','стрейт','флаш','фулл хауз','каре','стрейт флаш']
Allcards=[Str[i%13]+M[i//13] for i in range(52)]


def HandStr(H):
    return [Allcards[x] for x in H]

def Cards(H):
    return H%13

def SuiteCount(H):
    k=len(H)
    s=n.zeros(4,int)
    c=H//13
    for i in range(k):
        s[c[i]]+=1
    return s


#Далее функции проверки типа комбинации,
#подразумевается, что аргумент - упорядоченный список карт
#--------------------------------------
def isFlush(H): #проверка на флеш 
    M=SuiteCount(H)
    k=n.argmax(M)
    if M[k]>=5:
        res=n.array([x%13 for x in H if x//13==k],dtype=int)
        return sorted(res,reverse=True)
    return []
#--------------------------------------
def isSF(H):  #проверка на стрит-флеш (H-упорядоченная флеш комбинация, без повторений)
    for i in range(len(H)-4):
        if (H[i]==H[i+1]+1)and(H[i]==H[i+2]+2)and(H[i]==H[i+3]+3)and(H[i]==H[i+4]+4):
            return n.array([H[i]],dtype=int)
    if (H[0]==12)and(H[-4]==3)and(H[-3]==2)and(H[-2]==1)and(H[-1]==0):
        return n.array([3],dtype=int)
    return []    

#-------------------------------

def isST(C):  #проверка на стрит
    N=[C[0]]
    nd=n.unique(C)[::-1]
    if len(nd)>=5:
        for i in range(len(nd)-4):
            if (nd[i]==nd[i+1]+1)and(nd[i]==nd[i+2]+2)and(nd[i]==nd[i+3]+3)and(nd[i]==nd[i+4]+4):
                return n.array([nd[i]],dtype=int)
        if (nd[0]==12)and(nd[-4]==3)and(nd[-3]==2)and(nd[-2]==1)and(nd[-1]==0):
            return n.array([3],dtype=int)
    return []

#------------------------------
def isQuad(C):
    for i in range(len(C)-3):
        if C[i]==C[i+1]==C[i+2]==C[i+3]:
            Kick=C[:i]+C[i+4:]
            return n.array([C[i],Kick[0]],dtype=int)
    return []
#------------------------------

def isSet(C):
    for i in range(len(C)-2):
        if C[i]==C[i+1]==C[i+2]:
            Kick=C[:i]+C[i+3:]
            return n.array([C[i]]+Kick,dtype=int)
    return []
#-----------------------------

def isPair(C):
    for i in range(len(C)-1):
        if C[i]==C[i+1]:
            Kick=n.append(C[:i],C[i+2:])
            return n.append([C[i]],Kick)
    return []

#---------------------------


def getComb(H):  #возвращает тип комбинации и саму комбинацию
    C=sorted(Cards(H),reverse=True)    
    if isFlush(H)!=[]:
        x=isSF(isFlush(H))
        if x!=[]:return [8,x]
        return [5,isFlush(H)[:5]]
    elif isQuad(C)!=[]:return [7,isQuad(C)]
    elif isST(C)!=[]:return [4,isST(C)]
    elif isSet(C)!=[]:
        x=isSet(C)
        for i in range(1,len(x)-1):
            if x[i]==x[i+1]:
                return [6,n.array([x[0],x[i]],dtype=int)]
        return [3,n.array([x[0],x[1],x[2]],dtype=int)]
    elif isPair(C)!=[]:
        x=isPair(C)
        for i in range(1,len(x)-1):
            if x[i]==x[i+1]:
                Kick=n.append(x[1:i],x[i+2:])
                return [2,n.array([x[0],x[i],Kick[0]],dtype=int)]
        return [1,n.array(x[:4],dtype=int)]
    else: return [0,n.array(C[:5],dtype=int)]
#---------------------------

'''
for i in range(30):
    RC=n.random.choice(52,7,replace=False)


#    RCards=Cards(RC)
#    k=isFlush(RC)
#    print(RCards,isST(RCards))
#    if k:
#        print(k)
#        x=isSF(k)
#        if x: print(RC,SuiteCount(RC),'=>',x)
#    print(RC,'=>',RCards,'=>',SuiteCount(RC),'=>',isFlush(RC))
    g=getComb(RC)[0]
    comb=getComb(RC)[1]
    print(HandStr(RC),end=' ')
    print(CombStr[g],end=' ')
    print(comb,end=' ')
    input()
'''           


#---------------------------------------        
def win(H1,H2): #определяет выигрышную комбинацию из двух
    r1,c1=getComb(H1)
    r2,c2=getComb(H2)
    if r1>r2: i=0
    elif r1<r2: i=2
    elif r1==r2:
        i=1
        for k in range(len(c1)):
            if c1[k]>c2[k]:
                i=0
                break
            elif c1[k]<c2[k]:
                i=2
                break
    return i
#---------------------------------------  
def boardcomb(a,b,c,d):
    H=n.delete(n.arange(52),[a,b,c,d],None)
    s=len(H)
    bcomb=n.array([[H[k1],H[k2],H[k3],H[k4],H[k5]] for k1 in range(s-4) for k2 in range(k1+1,s-3) for k3 in range(k2+1,s-2) for k4 in range(k3+1,s-1) for k5 in range(k4+1,s)],dtype=int)
    return bcomb
#---------------------------------------  
def eq(A,B):
    boards=boardcomb(A[0],A[1],B[0],B[1])
    e=n.zeros(3)
    for x in boards:
        e[win(n.append(A,x),n.append(B,x))]+=1
    k=2*47*46*9*44
    return [x/k for x in e]
