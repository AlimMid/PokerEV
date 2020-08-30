import math
import random
'''
print('A-12, K-11, Q-10, J-9, T-8, 9-7, 8-6, 7-5, 6-4, 5-3, 4-2, 3-1, 2-0')
print('введите комбинацию значений карт H1,H2,H3,H4,H5:')
h1=input('H1=')
h2=input('H2=')
h3=input('H3=')
h4=input('H4=')
h5=input('H5=')

Str='23456789TJQKA'
M='hdcs'
CombStr=['карта','пара','допер','сет','стрейт','флаш','фулл хауз','каре','стрейт флаш']
Allcards=[]
for i in range(52):
    k=i%13
    l=i//13
    H=Str[k]+M[l]
    Allcards.append(H)

H=[21,19]
Board=[14,23,10,36,49]
Hand=H+Board
print(Hand)
'''


def Str(): return '23456789TJQKA'
def M(): return 'hdcs'
def CombStr(): return ['карта','пара','допер','сет','стрейт','флаш','фулл хауз','каре','стрейт флаш']
def Allcards():
    s=[]
    for i in range(52):
        k=i%13
        l=i//13
        H=Str()[k]+M()[l]
        s.append(H)
    return s

def HandStr(H):
    res=''
    for i in range(len(H)):
        res=res+Allcards()[H[i]]
    return res
#--------------------------
def SortHand(Hand):
    H=Hand[:]
    for i in range(0,len(H)):
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
#---------------------------
def Cards(H):
    Card=[x%13 for x in H]
    return Card

def SortSuite(H):
    C=SortHand(H)
    Suite=[x//13 for x in C]
    return Suite

def SuiteCount(H):
    S=[0,0,0,0]
    Suite=SortSuite(H)
    for i in range(0,len(H)):
        S[Suite[i]]+=1
    return S
'''
print(SortHand(Hand))
print(Cards(SortHand(Hand)))
print(SuiteCount(Hand))
print(HandStr(Hand))
input()
'''
#-----------------------------
def isFlush(H):
    res=[]
    C=SortHand(H)
    x=SuiteCount(H)
    for i in range(0,4):
        if x[i]>4:
            k=i
            break
    else:
        return res
    for i in range(len(H)):
        if C[i]//13==k:
            res.append(C[i])
    return res
#-------------------------------

def isST(H):
    C=SortHand(H)
    NoDubl=[C[0]]
    S=[NoDubl[0]%13]
    for i in range(1,len(H)):
        a=C[i]%13
        b=C[i-1]%13
        if a<b:
            NoDubl.append(C[i])
            S.append(a)
    res=[]
    for i in range(len(NoDubl)-4):
        if (S[i]==S[i+1]+1)and(S[i]==S[i+2]+2)and(S[i]==S[i+3]+3)and(S[i]==S[i+4]+4):
            res=NoDubl[i:i+5]
            return res
    return res
#-------------------------------
def isSF(H):
    res=[]
    F=isFlush(H)
    if F:
        res=isST(F)
    return res
#------------------------------

def isQuad(H):
    res=[]
    C=SortHand(H)
    S=Cards(C)
    for i in range(len(H)-3):
        if S[i]==S[i+1]==S[i+2]==S[i+3]:
            Kare=[C[i],C[i+1],C[i+2],C[i+3]]
            Kick=C[:i]+C[i+4:]
            res=Kare+Kick
            return res
    return res
#------------------------------
def isSet(H):
    res=[]
    Trips=[]
    C=SortHand(H)
    S=Cards(C)  
    for i in range(len(H)-2):
        if S[i]==S[i+1]==S[i+2]:
            Trips=[C[i],C[i+1],C[i+2]]
            Kick=C[:i]+C[i+3:]
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
    C=SortHand(H)
    S=Cards(C)
    for i in range(len(H)-1):
        if S[i]==S[i+1]:
            P1=[C[i],C[i+1]]
            Kick=C[:i]+C[i+2:]
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
def isHigh(H):
    C=SortHand(H)
    return C[0:5]

"""
Rcards=[x for x in range(52)]
for j in range(30):
    Hand=random.sample(Rcards,7)
    print(j,':',Hand)
    print(Cards(SortHand(Hand)))
    print(SortHand(Hand))
    print(SortSuite(Hand))
    print(SuiteCount(Hand))
    print(HandStr(SortHand(Hand),Allcards))
    print('стрейт флаш',isSF(Hand))
    print('каре',isQuad(Hand))
    print('фулл хауз',isFH(Hand))
    print('флаш',isFlush(Hand)[:5])
    print('стрейт',isST(Hand))
    print('сет',isSet(Hand)[:5])
    print('допер',isDoper(Hand))
    print('пара',isPair(Hand)[:5])
    print('карта',isHigh(Hand))
    input()
"""
def getComb(H):  #возвращает тип комбинации и саму комбинацию
    if isSF(H): return [8,isSF(H)[:5]]
    elif isQuad(H): return [7,isQuad(H)[:5]]
    elif isFH(H): return [6,isFH(H)[:5]]
    elif isFlush(H): return [5,isFlush(H)[:5]]
    elif isST(H): return [4,isST(H)[:5]]
    elif isSet(H): return [3,isSet(H)[:5]]
    elif isDoper(H): return [2,isDoper(H)[:5]]
    elif isPair(H): return [1,isPair(H)[:5]]
    else: return [0,isHigh(H)[:5]]

def Flush(): #все флеш комбинации без стрит флешей
    K=[]
    for k1 in range(0,13):
        for k2 in range(0,k1):
            for k3 in range(0,k2):
                for k4 in range(0,k3):
                    for k5 in range(0,k4):
                        H=[k1,k2,k3,k4,k5]
                        if not((k1==k2+1) and (k1==k3+2) and (k1==k4+3) and (k1==k5+4)):
                            K.append(H)
    return K

def SF(): #все стрит флеши
    K=[[3,2,1,0,12]]
    for i in range(4,13):
        H=[i,i-1,i-2,i-3,i-4]
        K.append(H)
    return K

def Quad(): #все каре
    K=[]
    for q in range(0,13):
        for k in range(0,13):
            if not(q==k):
                H=[q,q,q,q,k]
                K.append(H)
    return K

def FH(): #все фуллы
    K=[]
    for q in range(0,13):
        for k in range(0,13):
            if not(q==k):
                H=[q,q,q,k,k]
                K.append(H)
    return K

def Set(): #сеты но не фуллы
    K=[]
    for s in range(0,13):
        for k1 in range(0,13):
            if not(k1==s):
                for k2 in range(0,k1):
                    if not(k2==s):
                        H=[s,s,s,k1,k2]
                        K.append(H)
    return K

def Doper(): #2 пары
    K=[]
    for p1 in range(0,13):
        for p2 in range(0,p1):
            for k in range(0,13):
                if (not(k==p1))and(not(k==p2)):
                    H=[p1,p1,p2,p2,k]
                    K.append(H)
    return K

def Pair(): #пары
    K=[]
    for p in range(0,13):
        for k1 in range(0,13):
            for k2 in range(0,k1):
                for k3 in range(0,k2):
                    if (not(k1==p))and(not(k2==p))and(not(k3==p)):
                        H=[p,p,k1,k2,k3]
                        K.append(H)
    return K

def ST(): #стриты
    return SF()

def High(): #старшие карты
    return Flush()

def Rank(Hand): #возвращает силу комбинации в зависимости от типа
    r=getComb(Hand)[0]
    H=Cards(getComb(Hand)[1])
    if r==8:   return [8,SF().index(H)]
    elif r==7: return [7,Quad().index(H)]
    elif r==6: return [6,FH().index(H)]
    elif r==5: return [5,Flush().index(H)]
    elif r==4: return [4,ST().index(H)]
    elif r==3: return [3,Set().index(H)]
    elif r==2: return [2,Doper().index(H)]
    elif r==1: return [1,Pair().index(H)]
    else:      return [0,High().index(H)]

def win(H1,H2):
    r1=getComb(H1)[0]
    r2=getComb(H2)[0]
    if r1>r2: i=0
    elif r1<r2: i=2
    elif r1==r2:
        s1=Rank(H1)[1]
        s2=Rank(H2)[1]
        if s1>s2: i=0
        elif s1<s2: i=2
        elif s1==s2: i=1
    return i

def EQ(A,B):
    allc=[x for x in range(52)]
    bcards=allc
    bcards.remove(A[0])
    bcards.remove(A[1])
    bcards.remove(B[0])
    bcards.remove(B[1])
    print(bcards)
    input()
    s=len(bcards)
    e=[0,0,0]
    for k1 in range(s-4):
        for k2 in range(k1+1,s-3):
            print(k2)
            for k3 in range(k2+1,s-2):
                for k4 in range(k3+1,s-1):
                    for k5 in range(k4+1,s):
                        b1=bcards[k1]
                        b2=bcards[k2]
                        b3=bcards[k3]
                        b4=bcards[k4]
                        b5=bcards[k5]
                        board=[b1,b2,b3,b4,b5]
                        H1=A+board
                        H2=B+board
                        x=win(H1,H2)
                        e[x]+=1
    k=2*47*46*9*44
    return [x/k for x in e]

def boardcomb(H):
    s=len(H)
    comb=[]
    for k1 in range(s-4):
        for k2 in range(k1+1,s-3):
            for k3 in range(k2+1,s-2):
                for k4 in range(k3+1,s-1):
                    for k5 in range(k4+1,s):
                        b1=H[k1]
                        b2=H[k2]
                        b3=H[k3]
                        b4=H[k4]
                        b5=H[k5]
                        x=[b1,b2,b3,b4,b5]
                        comb.append(x)
    return comb

def eq(A,B):
    allc=[x for x in range(52)]
    L=allc
    L.remove(A[0])
    L.remove(A[1])
    L.remove(B[0])
    L.remove(B[1])
    e=[0,0,0]
    for x in boardcomb(L): e[win(A+x,B+x)]+=1
    return e
'''       
print('Straigt Flush:',len(SF()))
print('Quad:',len(Quad()))
print('Full House:',len(FH()))
print('Flush:',len(Flush()))
print('Straight:',len(ST()))
print('Set:',len(Set()))
print('Doper:',len(Doper()))
print('Pair:',len(Pair()))
print('High Card:',len(High()))
print(len(SF())+len(Quad())+len(FH())+len(Flush())+len(ST())+len(Set())+len(Doper())+len(Pair())+len(High()))
All=High()+Pair()+Doper()+Set()+ST()+Flush()+FH()+Quad()+SF()
print('к-во всех уникальных комбинаций:',len(All))
print('eq([2,8],[4,11])',HandStr([2,8]),HandStr([4,11]))
print(EQ([2,8],[4,11]))

Rcards=[x for x in range(52)]
for j in range(3000):
    Rhand=random.sample(Rcards,7)
#    Rpp=Rhand[:2]
#    Rboard=Rhand[2:]
    i=getComb(Rhand)[0]
#    comb=getComb(Rhand)[1]
    r=Rank(Rhand)[1]
#    print(j,end='')
#    print(j,':',Rhand,HandStr(Rpp,Allcards),HandStr(Rboard,Allcards),HandStr(comb,Allcards),i,':',CombStr[i],',ранг=',r,end='')
#    input()
'''
