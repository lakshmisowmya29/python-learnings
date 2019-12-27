i=2
j=0
sum=0
while(i<=100):
    for j in range(2,i):
        if(i%j==0):
            break
    if(j==i-1):
        sum=sum+i
        print(sum)
    i=i+1
 
    