def dict_forming(d,e):
    print(f"    # {list(d)}")
    print(f"    {tuple(d)} :",end="")
    print(f'"{e}"',end="")
    print()
    

def main():
    d1 = [39, 50, 28, 8, 345, 43, 29, 40, 89, 34, 5, 6, 4, 29, 30, 48, 96, 4, 7, 9, 10, 20, 30, 35, 345, 45]
    #d1 = [39, 50, 28, 8, 345]
    exp_output1 = "Hello How are you"
    d2 = [39, 50, 89, 346, 5, 20, 30, 35, 345, 28, 8, 345, 43, 29, 40, 48, 96, 6, 4, 29, 30, 4, 7, 5, 2, 4, 67, 29, 9, 10, 45]
    #d2 = [39, 50, 89, 8, 346]
    exp_output2 = "Bye now"

    print("data = {")
    data1 = dict_forming(d1,exp_output1)
    print()
    data2 = dict_forming(d2,exp_output2)
    print("}",end="")
    print()


if(__name__=="__main__"):
    main()