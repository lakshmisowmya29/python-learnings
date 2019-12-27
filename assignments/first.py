a=426
sum=0
sum=sum+a%10
a=a/10
sum=sum+a%10
a=a/10
sum=int(sum+a%10)
a=int(a/10)
print(sum)
print(a)

