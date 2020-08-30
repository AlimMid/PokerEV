import math
import random
Str='23456789TJQKA'
M='hdcs'
CombStr=['карта','пара','допер','сет','стрейт','флаш','фулл хауз','каре','стрейт флаш']
Allcards=[Str[i%13]+M[i//13] for i in range(52)]

#все флеш комбинации без стрит флешей
Flush=[[k1,k2,k3,k4,k5] for k1 in range(4,13) for k2 in range(3,k1) for k3 in range(2,k2) for k4 in range(1,k3) for k5 in range(k4) if not ((k1==k2+1) and (k1==k3+2) and (k1==k4+3) and (k1==k5+4))] 

#все стрит флеши
SF=[[3,2,1,0,12]]+[[x,x-1,x-2,x-3,x-4] for x in range(4,13)]

#все каре
Quad=[[x,x,x,x,y] for x in range(0,13) for y in range(0,13) if not(x==y)]

#все фуллы
FH=[[x,x,x,y,y] for x in range(13) for y in range(13) if not(x==y)]

#сеты но не фуллы
Set=[[x,x,x,a,b] for x in range(13) for a in range(1,13) for b in range(a) if not(x==a)and not(x==b)]

#2 пары
Doper=[[x,x,y,y,k] for x in range(1,13) for y in range(x) for k in range(13) if (not(k==x))and(not(k==y))]

#пары
Pair=[[x,x,a,b,c] for x in range(13) for a in range(2,13) for b in range(1,a) for c in range(b) if not(a==x) and not(b==x) and not(c==x)]

#стриты
ST=SF

#старшие карты
High=Flush

#все комбинации
Allcomb=[High,Pair,Doper,Set,ST,Flush,FH,Quad,SF]

def HandStr(H):
    return [Allcards[x] for x in H]

def Cards(H):
    return [x%13 for x in H]

def SortHand(Hand):
    H=Hand[:]
    for i in range(len(H)):
        for j in range(i+1,len(H)):
            if (H[i]%13)<(H[j]%13):
                t=H[j]
                H[j]=H[i]
                H[i]=t
            elif (H[i]%13)==(H[j]%13)and(H[i]<H[j]):
                t=H[j]
                H[j]=H[i]
                H[i]=t
    return H

def SuiteCount(H):
    S=[0,0,0,0]
    C=[x//13 for x in H]
    for x in C: S[x]+=1
    return S

#Далее функции проверки типа комбинации,
#подразумевается, что аргумент - упорядоченный список карт
#после применения функции SortHand
#--------------------------------------
def isFlush(H): #проверка на флеш 
    res=[]
    M=SuiteCount(H)
    for i in range(4):
        if M[i]>4:
            res=[x for x in H if x//13==i]
            return res
    return res
#-------------------------------

def isST(H):  #проверка на стрит
    NoDubl=[H[0]]
    S=[H[0]%13]
    for i in range(1,len(H)):
        a=H[i]%13
        b=H[i-1]%13
        if a<b:
            NoDubl.append(H[i])
            S.append(a)
    res=[]
    for i in range(len(NoDubl)-4):
        if (S[i]==S[i+1]+1)and(S[i]==S[i+2]+2)and(S[i]==S[i+3]+3)and(S[i]==S[i+4]+4):
            res=NoDubl[i:i+5]
            return res
    if len(S)>4:
        if (S[0]==12)and(S[-4]==3)and(S[-3]==2)and(S[-2]==1)and(S[-1]==0):
            res=NoDubl[-4:]+NoDubl[:1]
    return res
#-------------------------------
def isSF(H):
    res=[]
    F=isFlush(H)
    if isFlush(H):
        res=isST(isFlush(H))
    return res
#------------------------------
def isQuad(H):
    res=[]
    C=Cards(H)
    for i in range(len(H)-3):
        if C[i]==C[i+1]==C[i+2]==C[i+3]:
            Kare=[H[i],H[i+1],H[i+2],H[i+3]]
            Kick=H[:i]+H[i+4:]
            res=Kare+Kick
    return res
#------------------------------
def isSet(H):
    res=[]
    C=Cards(H)  
    for i in range(len(H)-2):
        if C[i]==C[i+1]==C[i+2]:
            Trips=[H[i],H[i+1],H[i+2]]
            Kick=H[:i]+H[i+3:]
            res=Trips+Kick
            return res
    return res
#-----------------------------

def isFH(H):
    res=[]
    x=isSet(H)
    S=Cards(x)
    if x:
        for i in range(3,len(x)-1):
            if S[i]==S[i+1]:
                res=x[:3]+[x[i],x[i+1]]
                return res
    return res

#------------------------------
def isPair(H):
    res=[]
    C=Cards(H)
    for i in range(len(H)-1):
        if C[i]==C[i+1]:
            P1=[H[i],H[i+1]]
            Kick=H[:i]+H[i+2:]
            res=P1+Kick
            return res
    return res
#-----------------------------

def isDoper(H):
    res=[]
    x=isPair(H)
    S=Cards(x)
    if x:
        for i in range(2,len(x)-1):
            if S[i]==S[i+1]:
                P2=[x[i],x[i+1]]
                Kick=x[2:i]+x[i+2:]
                res=x[0:2]+P2+Kick
                return res
    return res
#---------------------------
def isHigh(H): return H[0:5]
#---------------------------
def myComb(Hand):  #возвращает тип комбинации и саму комбинацию
    H=SortHand(Hand)
    if isFlush(H):
        if isST(isFlush(H)):
            return [8,isST(isFlush(H))[:5]]
        return [5,isFlush(H)[:5]]
    elif isQuad(H):return [7,isQuad(H)[:5]]
    elif isST(H):return [4,isST(H)[:5]]
    elif isSet(H):
        x=isSet(H)
        for i in range(3,len(x)-1):
            if (x[i]%13==x[i+1]%13):
                return [6,x[:3]+[x[i],x[i+1]]]
        return [3,x[:5]]
    elif isPair(H):
        x=isPair(H)
        for i in range(2,len(x)-1):
            if x[i]%13==x[i+1]%13:
                res=x[0:2]+[x[i],x[i+1]]+x[2:i]+x[i+2:]
                return [2,res[:5]]
        return [1,x[:5]]
    else: return [0,H[:5]]

                    
            



'''

    if isSF(H): return [8,isSF(H)[:5]]
    elif isQuad(H): return [7,isQuad(H)[:5]]
    elif isFH(H): return [6,isFH(H)[:5]]
    elif isFlush(H): return [5,isFlush(H)[:5]]
    elif isST(H): return [4,isST(H)[:5]]
    elif isSet(H): return [3,isSet(H)[:5]]
    elif isDoper(H): return [2,isDoper(H)[:5]]
    elif isPair(H): return [1,isPair(H)[:5]]
    else: return [0,isHigh(H)[:5]]
'''
def Rank(r,Comb): #возвращает силу комбинации в зависимости от типа
    H=Cards(Comb)
    return Allcomb[r].index(H)
