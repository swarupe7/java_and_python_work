k=int(input())
a=[int(x) for x in input().split(' ')]

def factor(x,y):
    fx=[]
    fy=[]
    for i in range(2,x+1):
        if x%i==0:
            fx.append(i)
    for j in range(2,y+1):
        if y%j==0:
            fy.append(j)
    for i in fx:
        if i in fy:
            return 0
    for i in fy:
        if i in fx:
            return 0
    return 1
c=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        c+=factor(a[i],a[j])
print(c)





