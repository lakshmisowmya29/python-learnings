i=1
j=1
while (i <= 5):
    print (i)
    j=1
    while(j<=5):
        print(j)
        if(j%2==0):
            i=i+2
        j=j+1
    print("")
    i=i+1

print(i,j)