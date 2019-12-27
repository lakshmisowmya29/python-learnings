def factorial_sowmya(n):
	f=1
	for i in range(1, n+1):
		f=f*i
	return f
    

n = 10
sum = s = 0
for i in range (2, n+2):
    x1 = factorial_sowmya(i)
    x2 = factorial_sowmya(i-1)
    print(x1)
    print(x2)
    s = s + x1/x2
    sum = sum + factorial_sowmya(i)/factorial_sowmya(i-1)

print ("s   value is :%d" % s)
print ("sum value is :%d" % sum)


n = 10
sum1 = 0
for i in range (1,n):
    sum1 = sum1 + factorial_sowmya(i)
print ("sum1 value is :%d" %s) 
    
