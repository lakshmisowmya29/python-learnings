"""
def read_compleate_data(filename):
    fd = open(filename, "rt")
    data = fd.read()
    length = len(data)

    print("len :%d, %s" % (length, data))

    fd.close()
    """
    
def read_text_file(tname):
    wc=0
    fd=open(tname, "rt")
    data = fd.read()
    tlist = data.split()
    for eword in tlist:
        if(eword == "and"):
            wc = wc + 1
    print(wc)
    fd.close()

fname = "t.txt"
read_text_file(fname)
