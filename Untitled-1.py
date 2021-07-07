def check(m,n):
    if n==1:
        return -m
    else:
        return (m+1)+check(m+1,n-1)
print(check(5,5))