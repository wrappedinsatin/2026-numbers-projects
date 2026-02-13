# find prime numbers until user stops asking

# in a given expression 6n +- 1, n is a NON PRIME number greater than 3
# > all products are prime

is_running = True

def user_inputs():

    global entry_number

    entry_number = input("what number would you like to check? (q to quit): ")

    if entry_number.lower() in ["q", "quit"]:
        is_running = False
        return

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

    if entry_number == (2, 3):
        return True
    
    resultant = (entry_number + 1) / 6 or (entry_number - 1) / 6
    if resultant % 1 == 0:
        return True
    else:
        return False
    
    if entry_number == True:
        print(f"{entry_number} IS a prime number!")
    else:
        print(f"{entry_number} is NOT a prime number!")

def main():

    while True:
        
        user_inputs()
        prime_finder()

if __name__ == "__main__":
    main()