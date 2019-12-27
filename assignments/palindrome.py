a=626
c=0
p=a

c=(c*10)+(a%10)
print(c)
a=int(a/10)
print(a)
c=(c*10)+(a%10)
print(c)
a=int(a/10)
print(a)
c=(c*10)+(a%10)
print(c)
a=a/10
print(a)

if (c==p):
print(a is palindrome)

else:
print(a is not a palindrome)

