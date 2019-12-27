k=50
n=7
a=[1, 12, 5, 111, 200, 1000, 10]
print (a)
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
sum=0
count=0
print (a)
for i in range(0,n):
    if(sum<=k):
        sum=sum+a[i]
        count=count+1
print(count-1)