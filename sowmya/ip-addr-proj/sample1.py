s=[
    "host santhosh-laptop {",
    "hardware ethernet e4:f8:9c:86:67:85;",
    "fixed-address 192.168.1.214;",
    "option routers 192.168.1.1;",
    "}"
]
def get_data(s):
    #print (data[0])
    ldata=[]
    for line in s:
        line = line.strip(";")
        line = line.split()
        ldata.append(line)
    return ldata

       
def main():
    idata = get_data(s)
    #print(idata[0][1])
    
    data_dict ={
          "name" :[],
        "macaddr" :[],
        "ipadrr" :[]
    }
    data_dict['macaddr'].append(idata[1][2])
    data_dict['ipadrr'].append(idata[2][1])
    data_dict['name'].append(idata[0][1])
    
    print(data_dict)





if (__name__ == '__main__'):
    main()
"""
for line in s:
    data=(line.strip(";")).split()
    print(data[1])
    
      
    for line in s:
        print("-->",line)
        print(type(line))
        data=line.split()
        print("----->",data)
        """