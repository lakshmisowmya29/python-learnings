def dump_dict(d,e):
    print(f"# {list(d)}")
    print(f"{tuple(d)} : ",end="")
    print(f'"{e}"',end="")
    print()

def main():
    d = [39, 50, 28, 8, 345, 43, 29, 40, 89, 34, 5, 6, 4, 29, 30, 48, 96, 4, 7, 9, 10, 20, 30, 35, 345, 45]
    exp_output = "Hello How are you"
    print("data = {")
    dump_dict(d, exp_output)
    print()
    print('}', end="")

if(__name__ == "__main__"):
    main()