def simple_read_few_bytes(filename):
    fd = open(filename, "r")

    data = fd.read(10)

    print("data :%s" % data)

    fd.close()

def simple_read_twice(filename):
    fd = open(filename, "rt")

    data = fd.read(10)
    print("1: data :%s" % data)

    data = fd.read(10)
    print("2: data :%s" % data)

    fd.close()

def read_compleate_text_file(filename):
    fd = open(filename, "rt")
    i = 1
    while(True):
        data = fd.read(10)
        length = len(data)
        print("%d: len :%d, %s" % (i, length, data))

        i = i + 1
        if (length < 10):
            break

    fd.close()

def read_compleate_data(filename):
    fd = open(filename, "rt")
    data = fd.read()
    length = len(data)

    print("len :%d, %s" % (length, data))

    fd.close()

#read
#readline
readlines

def read_line_text_file(filename):
    fd = open(filename, "rt")
    i = 1
    while(True):
        data = fd.readline()
        if (len(data) <= 0):
            break
        print("%d : len :%d, %s" % (i, len(data), data))
        i  = i + 1

    fd.close()

def read_lines_text_file(filename):
    fd = open(filename, "rt")

    data = fd.readlines()

    fd.close()

    print("len :%d, %s" % (len(data), data))

    i = 1
    for line in data:
        print("%d. %s" % (i, line))
        i = i + 1
    return
    exit(1)

#0 - Beginning
#1 - Current
#2 - End of file
def file_operations_seek(filename):
    #fd = open(filename, "rt") #Python 2.4.x
    fd = open(filename, "rb")  #Python 3.6.x

    print("file position :%d" % fd.tell())

    data = fd.read(10)
    print("file position :%d" % fd.tell())

    fd.seek(40)
    print("file position :%d" % fd.tell())

    data = fd.read(10)
    print("file position :%d" % fd.tell())

    fd.seek(0, 0)
    print("file position :%d" % fd.tell())

    fd.seek(10, 0)
    print("file position :%d" % fd.tell())

    fd.seek(20, 1)
    print("file position :%d" % fd.tell())

    fd.seek(-10, 2)
    print("file position :%d" % fd.tell())
    
    fd.seek(0, 2)
    print("file position :%d" % fd.tell())
    
    fd.seek(30, 0)
    print("file position :%d" % fd.tell())
    
    fd.seek(-10, 1)
    print("file position :%d" % fd.tell())
    
    print("Name of the file  :%s" % fd.name)
    print("Closed or not     :%r" % fd.closed)
    print("Opening mode      :%r" % fd.mode)

    fd.close()
    return

def write_to_file(filename):
    fd = open(filename, "r+")
    print("file position :%d" % fd.tell())

    fd.write("Hello world")
    print("file position :%d" % fd.tell())

    fd.seek(30, 0)
    print("file position :%d" % fd.tell())

    fd.write("Hello world")
    print("file position :%d" % fd.tell())

    fd.close()
    return

def main():
    filename = "t.txt"
    #simple_read_few_bytes(filename)
    #simple_read_twice(filename)
    #read_compleate_text_file(filename)
    #read_line_text_file(filename)
    #read_compleate_data(filename)
    read_lines_text_file(filename)
    #file_operations_seek(filename)
    #write_to_file(filename)
    #write_to_binary_file("a.txt")
    return
    
if (__name__ == "__main__"):
    main()

