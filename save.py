'''t1=[2,4,5,6]
t1.insert(2,15)
print(t1)'''

'''L:L=[1,23,'hi',6]
print(L)'''

'''d={}
d[1]=1
d['1']=2
d[1.0]=4
sum=0
for k in d:
sum+=d[k]
print(sum)'''

'''def increment(n):
    n.append([49])
    return n[0],n[1],n[2],n[3]
l=[23,35,47]
m1,m2,m3,m4=increment(l)
print(l,l[3]==m4)'''

'''def Display(str):
    m=""
    for i in range(0,len(str)):
        if(str[i].isupper()):
            m=m+str[i].lower()
        elif str[i].islower():
            m=m+str[i].upper()
        else:
            if i%2==0:
                m-m+str[i1]
    else:
        m-m+'#'
    print(m)
Display("Welcome to DPS@NAC")'''

'''import random
string='CBSEONLINE'
number=random.randint(0,3)
n=9
while string[n]!='L':
    print(string[n]+string[number]+'#'
number+=1
n-=1
print(string)'''

'''a=open("mama.txt","r")
upper,lower=0,0
for b in a.read():
    if b.isupper():
          upper+=1
print(upper,lower)'''

def change(p,q=30):
    p=p+q
    q=p-q
    print(p,'#',q)
    return p
r=150
s=100
r=change(r,s)
print(r,'#',s)
s=change(s)

    
