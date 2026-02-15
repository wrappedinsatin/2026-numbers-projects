def quit_option():
    ask = input("do you want to restart? (y/n):")
    if ask in ["n", "N"]:
        print("thanks for trying!")
        exit()
    elif ask in ["y", "Y"]:
        print("restarting...")
    else:
        print(f"{ask} was not valid.")
        ask = input("do you want to restart? (y/n):")

    quit_option()