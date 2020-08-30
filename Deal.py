Str='23456789TJQKA'
M='hdcs'
CombStr=['карта','пара','допер','сет','стрейт','флаш','фулл хауз','каре','стрейт флаш']
Allcards=[]
for i in range(52):
    k=i%13
    l=i//13
    H=Str[k]+M[l]
    Allcards.append(H)

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


Royal=0;SF=0;Quad=0;FH=0;Flush=0;St=0;Set=0;Doper=0;Pair=0;A=0;Spam=0
for k1 in range(0,52):
    for k2 in range(0,k1):
        for k3 in range(0,k2):
            for k4 in range(0,k3):
                for k5 in range(0,k4):
                    H=SortHand([k1,k2,k3,k4,k5])
                    if (H[0]//13==H[1]//13==H[2]//13==H[3]//13==H[4]//13):
                        if (H[0]%13==12)and(H[1]%13==11)and(H[2]%13==10)and(H[3]%13==9)and(H[4]%13==8):
                            Royal+=1
                        elif ((H[0]%13==H[1]%13+1)and(H[0]%13==H[2]%13+2)and(H[0]%13==H[3]%13+3)and(H[0]%13==H[4]%13+4))or((H[0]%13==12)and(H[1]%13==3)and(H[2]%13==2)and(H[3]%13==1)and(H[4]%13==0)):
                            SF+=1
                        else:
                            Flush+=1
                    elif (H[0]%13==H[1]%13==H[2]%13==H[3]%13)or(H[1]%13==H[2]%13==H[3]%13==H[4]%13):
                        Quad+=1
                    elif ((H[0]%13==H[1]%13==H[2]%13)and(H[3]%13==H[4]%13))or((H[0]%13==H[1]%13)and(H[2]%13==H[3]%13==H[4]%13)):
                        FH+=1
                    elif ((H[0]%13==H[1]%13+1)and(H[0]%13==H[2]%13+2)and(H[0]%13==H[3]%13+3)and(H[0]%13==H[4]%13+4))or((H[0]%13==12)and(H[1]%13==3)and(H[2]%13==2)and(H[3]%13==1)and(H[4]%13==0)):
                        St+=1
                    elif (H[0]%13==H[1]%13==H[2]%13)or(H[1]%13==H[2]%13==H[3]%13)or(H[2]%13==H[3]%13==H[4]%13):
                        Set+=1
                    elif ((H[0]%13==H[1]%13)and(H[2]%13==H[3]%13))or((H[0]%13==H[1]%13)and(H[3]%13==H[4]%13))or((H[1]%13==H[2]%13)and(H[3]%13==H[4]%13)):
                        Doper+=1
                    elif (H[0]%13==H[1]%13)or(H[1]%13==H[2]%13)or(H[2]%13==H[3]%13)or(H[3]%13==H[4]%13):
                        Pair+=1
                    elif H[0]%13==12:
                        A+=1
                    else:
                        Spam+=1
Allcomb=52*51*50*49*48/(2*3*4*5)
print('всего комбинаций:',Allcomb)
print('Флаш Рояль:',Royal)
print('Стрейт Флаш:',SF)
print('Каре:',Quad)
print('Фулл Хауз:',FH)
print('Флаш:',Flush)
print('Стрейт:',St)
print('Сет:',Set)
print('Допер:',Doper)
print('Пара:',Pair)
print('Туз:',A)
print('Мусор:',Spam)
print('все:',Royal+SF+Quad+FH+Flush+St+Set+Doper+Pair+A+Spam)
deal7=(Royal*22000+SF*250+Quad*30+FH*5+Flush*1+St*0.5+Set*0.25+Doper*0.07+Pair*0.02+A*0.01)/Allcomb
deal70=(Royal*22000+SF*22000+Quad*300+FH*75+Flush*25+St*10+Set*3+Doper*0.7+Pair*0.1)/Allcomb
print('эквити deal7:',deal7)
print('эквити deal70:',deal70)
  
