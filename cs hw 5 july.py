def compute(x,y):
    if x>1:
        if x%y==0:
            print(y,end='')
            compute(int(x/y),y)
        else:
            compute(x,y+1)
a=int(input("enter a number"))
b=int(input("enter 2nd no"))
compute(a,b)