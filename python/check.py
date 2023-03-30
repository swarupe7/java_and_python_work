def check(n):
    if n[0]!='4' and n[0]!='5' and  n[0]!='6':
        return 'Invalid'
    co=0
    for i in n:
        if  (ord(i)>=45 and ord(i)<=54):
            co+=1
    if(co!=16):
        return 'Invalid'
    