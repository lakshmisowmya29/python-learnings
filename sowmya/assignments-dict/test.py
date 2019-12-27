def dump_dict(d1, er):
    print(f"\t# {tuple(d1)}")
    print(f"\t{tuple(d1)} : ", end="")
    print(f'"{er}",', end="")
    print()


def main():
    d1 = [10, 20, 30]
    er1 = "hello_world"

    d2 = [50, 2, 3]
    er2 = "Bye_world"

    print("data = {")
    dump_dict(d1, er1)
    print()
    dump_dict(d2, er2)
    print('}', end="")
    print()

if(__name__ == "__main__"):
    main()