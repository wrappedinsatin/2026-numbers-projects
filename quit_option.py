def begin():
    begin = input("begin? type any key (n/no to quit):")
    if begin.lower() in ["n", "no"]:
        print()
        print("program exited.")
        exit()

def quit():
    ask = input("do you want to restart? (y/n):")
    if ask in ["n", "N"]:
        print("thanks for trying!")
        exit()
    elif ask in ["y", "Y"]:
        print("restarting...")
    else:
        print(f"{ask} was not valid.")
        ask = input("do you want to restart? (y/n):")

