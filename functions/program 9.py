def fun(s):
    k=len(s)
    m=""
    for i in range(0,k):
        if s[i].isupper():
            m=m+s[i].lower()
        elif s[i].isalpha():
            m=m+s[i].upper()
        elif s[i].isdigit():
            m=s[i]
        else:
            m=m+"bb"
    print(m)
fun('School2@Com')