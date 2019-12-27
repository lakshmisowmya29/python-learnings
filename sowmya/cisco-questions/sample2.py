a = "aura,networks.bangalore,and.hyderabad"
x = a.split(",")
x[1]=(x[1].replace("." ,","))
x[2]=(x[2].replace("." , ","))
print(".".join(x))
