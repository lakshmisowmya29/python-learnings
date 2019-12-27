def dump_dict(d,e):
    print(f"\t#{tuple(d)}")
    x = f"\t{tuple(d)}:"
    print(type(x))
    print(f"{e}",end="")
    print()

def main():
    d1=[10,20,30]
    e1="hello_world"
    d2=[50,2,3]
    e2="Bye_world"
    data = {dump_dict(d1,e1)}
    data = {dump_dict(d2,e2)}
    print(data)
    print(type(data))
    #print("data={"dump_dict(d1,e1)"}")
    #print("data={"dump_dict(d2,e2)"}")


if(__name__=="__main__"):
    main()