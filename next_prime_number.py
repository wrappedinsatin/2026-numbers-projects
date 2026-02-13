# find prime numbers until user stops asking

# in a given expression 6n +- 1, n is a NON PRIME number greater than 3
# > all products are prime

def user_inputs():

    is_running = True
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
    except ValueError:
        print(f"your input, '{entry_number}' is invalid.")
        print("insert a natural number greater than one.")

    return entry_number

def prime_finder():
    pass
    # find an algorithm that computes prime numbers

def main():

    while is_running:
        
        user_inputs()
        prime_finder()

if __name__ == "__main__":
    main()