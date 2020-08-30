import math
import random
Str='23456789TJQKA'
M='hdcs'
CombStr=['карта','пара','допер','сет','стрейт','флаш','фулл хауз','каре','стрейт флаш']
Allcards=[Str[i%13]+M[i//13] for i in range(52)]


def HandStr(H):
    return [Allcards[x] for x in H]

def Cards(H):
    return [x%13 for x in H]

def SuiteCount(H):
    S=[0,0,0,0]
    C=[x//13 for x in H]
    for x in C: S[x]+=1
    return S

#Далее функции проверки типа комбинации,
#подразумевается, что аргумент - упорядоченный список карт
#--------------------------------------
def isFlush(H): #проверка на флеш 
    M=SuiteCount(H)
    for i in range(4):
        if M[i]>4:
            res=[x%13 for x in H if x//13==i]
            return sorted(res,reverse=True)
    return []
#--------------------------------------
def isSF(H):  #проверка на стрит-флеш (H-упорядоченная флеш комбинация, без повторений)
    for i in range(len(H)-4):
        if (H[i]==H[i+1]+1)and(H[i]==H[i+2]+2)and(H[i]==H[i+3]+3)and(H[i]==H[i+4]+4):
            return [H[i]]
    if (H[0]==12)and(H[-4]==3)and(H[-3]==2)and(H[-2]==1)and(H[-1]==0):
        return [3]
    return []    

#-------------------------------

def isST(C):  #проверка на стрит
    N=[C[0]]
    for i in range(1,len(C)):
        if C[i]<C[i-1]:
            N.append(C[i])
    if len(N)>4:
        for i in range(len(N)-4):
            if (N[i]==N[i+1]+1)and(N[i]==N[i+2]+2)and(N[i]==N[i+3]+3)and(N[i]==N[i+4]+4):return [N[i]]
        if (N[0]==12)and(N[-4]==3)and(N[-3]==2)and(N[-2]==1)and(N[-1]==0):return [3]
    return []

#------------------------------
def isQuad(C):
    for i in range(len(C)-3):
        if C[i]==C[i+1]==C[i+2]==C[i+3]:
            Kick=C[:i]+C[i+4:]
            return [C[i],Kick[0]]
    return []
#------------------------------
def isSet(C):
    for i in range(len(C)-2):
        if C[i]==C[i+1]==C[i+2]:
            Kick=C[:i]+C[i+3:]
            return [C[i]]+Kick
    return []
#-----------------------------

def isPair(C):
    for i in range(len(C)-1):
        if C[i]==C[i+1]:
            Kick=C[:i]+C[i+2:]
            return [C[i]]+Kick
    return []

#---------------------------
def getComb(H):  #возвращает тип комбинации и саму комбинацию
    C=sorted(Cards(H),reverse=True)    
    if isFlush(H):
        x=isSF(isFlush(H))
        if x:return [8,x]
        return [5,isFlush(H)[:5]]
    elif isQuad(C):return [7,isQuad(C)]
    elif isST(C):return [4,isST(C)]
    elif isSet(C):
        x=isSet(C)
        for i in range(1,len(x)-1):
            if x[i]==x[i+1]:
                return [6,[x[0],x[i]]]
        return [3,[x[0],x[1],x[2]]]
    elif isPair(C):
        x=isPair(C)
        for i in range(1,len(x)-1):
            if x[i]==x[i+1]:
                Kick=x[1:i]+x[i+2:]
                return [2,[x[0],x[i],Kick[0]]]
        return [1,x[:4]]
    else: return [0,C[:5]]
#---------------------------
'''
for i in range(30):
    RC=random.sample(range(52),7)
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
    H=list(range(52))
    H.remove(a)
    H.remove(b)
    H.remove(c)
    H.remove(d)
    s=len(H)
    bcomb=[[H[k1],H[k2],H[k3],H[k4],H[k5]] for k1 in range(s-4) for k2 in range(k1+1,s-3) for k3 in range(k2+1,s-2) for k4 in range(k3+1,s-1) for k5 in range(k4+1,s)]
    return bcomb
#---------------------------------------  
def eq(A,B):
    boards=boardcomb(A[0],A[1],B[0],B[1])
    e=[0,0,0]
    for x in boards: e[win(A+x,B+x)]+=1
    k=2*47*46*9*44
    return [x/k for x in e]
