n=97
f=0
for i in range (1,n+1):
    if(n%i==0):
        f=f+1
    
if(f==2):
    print("n is prime")
else:
    print( "n is not prime")