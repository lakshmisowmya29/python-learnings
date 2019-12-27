"""
[
 "santhosh-laptop": [
     {"macaddr" : "e4:f8:9c:86:67:85"},
     {"ipaddr" : "192.168.1.214"}
    ],
 "santhosh-laptop2": [
     {"macaddr" : "e4:f8:9c:86:67:86"},
     {"ipaddr" : "192.168.1.215"}
    ]
]
"""

def parse_dhcpd_conf(dhcpdata):
    ldata = []
    for line in dhcpdata:
        line = (line.strip()).split(",")
        ldata.append(line)
    return(ldata)

def generate_dhcpd_rule(idata):
    for line in idata:
        sysname, macaddr = line.strip().split(",")
        data
        print (f"sysname :{sysname}, macaddr  :{macaddr}")

def get_input_data(inputfile):
    rfd = open(inputfile)
    data = rfd.readlines()
    rfd.close()
    return data

def main():
    ldata = []
    data_dict = {
        "name" : [
            {"macaddr" : []}
            {"ipadrr" : []}
        ]
        
    }
    inputfile = "fixed-ip-list.csv"
    #dhcpdconf = "dhcpd-conf.txt"
    dhcpdconf = "data2.txt"

    idata = get_input_data(inputfile)
    #print (idata)

    dhcpdata = get_input_data(dhcpdconf)
    #print (dhcpdata)

    dhcpdata = get_input_data(dhcpdconf)
    rule_data = parse_dhcpd_conf(dhcpdata)
    

    generate_dhcpd_rule(idata)

    return 

if (__name__ == '__main__'):
    main()
"""
data1=(ai1.split(","))
data2=(ai2.split())
#data3=(ai2[7].split(".")
data2[1]=data1[0]
data2[5]=data1[1]
data2[5]=data2[5].strip()
print(type(data2[7]))
data2[7]=str(str(data2[7].rstrip(";"))).split(".")
print(type(data2[7]))















#data2[7]=(data2[7].strip(";"))
#print(data2[7][1])

#data2[7][3]=int(data2[7][3])
#print(data2[7][3])
#data2[7]=".".join(str([data2[7]]))
#print(data2[7])

#data2[7] = data2[7].strip(";")
#print(data2[7][3])
#print(type(data2[7][3]))
#print(type(int(data2[7][3])))
#exit(1)
#data2[7][3]=int(data2[7][3])+1
#print(data2[7][3])
fd1.close()
fd2.close()

"""