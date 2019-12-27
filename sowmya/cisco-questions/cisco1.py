list=[]
a=[1,2,3,5,6,7,8,11,12,13,14]


def numbers():
    i=0
    if(a[i]==i+1):
        i=i+1
    return(a[i])

    

def main():
    list=[]
    a=[1,2,3,5,6,7,8,11,12,13,14]
    #print(a[0])
    list.append(a[0])
    i=0
    if(a[i]==i+1):
        i=i+1
    list.append(a[i])

    x = numbers()
    #print(x)
    list.append(x)

    print(list) 



if (__name__ == "__main__"):
    main()
    