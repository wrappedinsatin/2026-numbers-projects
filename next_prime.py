# find prime numbers until user stops asking

# in a given expression 6n +- 1, n is a NON PRIME number greater than 3
# > all products are prime

is_running = True

def user_inputs():

    global entry_number

    entry_number = input("what number would you like to check? (q to quit): ")

    if entry_number.lower() in ["q", "quit"]:
        print("exiting program...")
        exit()

    try:

        entry_number = int(entry_number)
        if entry_number < 2:

            print(f"{entry_number} is less than +2!")
            print("input a number greater than +2.")
            entry_number = input("what number would you like to check?: ")

        else:
            return entry_number

    except ValueError:
        print(f"your input, '{entry_number}' is invalid.")
        print("insert a natural number greater than one.")


def prime_finder():

    if entry_number in (2, 3):
        print(f"{entry_number} IS a prime number!")
        return
    
    resultant = (entry_number + 1) / 6 or (entry_number - 1) / 6 # improve later
    if resultant % 1 == 0:
        print(f"{entry_number} IS a prime!")
        return
    else:
        print(f"{entry_number} is NOT a prime number!")
        return

def main():

    while True:
        
        user_inputs()
        prime_finder()

if __name__ == "__main__":
    main()