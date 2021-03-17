#user defined function without return values
def calc(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    return add,sub,mul
x=int(input("enter 1st no"))
y=int(input("enter 2nd no"))
z=int(input("enter 3rd no"))

p,q,r=calc(x,y)
print(x,y,z)