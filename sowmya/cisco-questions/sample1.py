a=['A','A','A',1,2,'A',3,'A',4,5,'A','A',7,'A','A']

c=0
for i in range(0,14):
    #print(a[i])
    if(a[i]=='A'and a[i-1]!='A'):
        c=c+1
print(c)
