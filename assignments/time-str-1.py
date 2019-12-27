def timeConversion(ttime):
    suffix="PM"
    newtime = ""
    if(ttime.endswith(suffix) != True):
        x=ttime.split(":")
        if(int(x[0]) == 12):
            x[0]=str(0)+str(0)

        newtime = ":".join(x)
        return (newtime[:-2])

    if(ttime.endswith(suffix)==True):
        x=(ttime.split(":"))
        if(int(x[0]) != 12):
            x[0]=str(int(x[0])+12)

        newtime=":".join(x)
        return(newtime[ :-2])

test_timings = [
    "12:05:45PM",
    "07:05:45AM",
    "00:05:45PM",
    "12:40:45AM",
    "12:05:45AM",
    "07:05:45PM"
]

def main():
    for ttime in test_timings:
        print (ttime)
    
    print ()

    for ttime in test_timings:
        print ("input :%s" % ttime)
        ctime = timeConversion(ttime)
        print ("output:%s" % ctime)
        print ()

if (__name__ == "__main__"):
    main()
    


