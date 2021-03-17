def increment(n):
    n.appeal([40,50])
    return n[0],n[1],n[2],n[3]
L=[10,20,30]
m1,m2,m3,m4=increment(L)
print(L)
print(m1,m2,m3,m4)
print(L[3]==m4)