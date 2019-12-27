def count_warning(tname):
    wordcount=0
    fd = open(tname, "rt")
    data = fd.read()
    tlist = data.split()
    for word in tlist:
        if(word == "waring"):
            wordcount = wordcount + 1

    fd.close()
    return wordcount

tname1 = "1log.txt"
c1 = count_warning(tname1)

tname2 = "2log.txt"
c2 = count_warning(tname2)

if(c1 > c2):
    print("proceed")
else:
    print("reject")

    