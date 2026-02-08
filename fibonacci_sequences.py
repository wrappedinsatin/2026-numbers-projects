def user_inputs():

    global is_running
    global sequence 

    is_running = True

    while is_running:
        print("this is a fibonacci sequence generator.")
        print()
        sequence = input("how many numbers do you want the sequence to have?(q to quit): ") 

    while True:
        if sequence.lower() in ("q", "quit", "end"):
            is_running = False
            return

        try:
            sequence = int(sequence)
        except ValueError:
            print(f"{sequence} was not a valid option!")
            print("please type in an integer starting from 1.")
        
        if sequence == "":
            print("type in an integer.")
            sequence = input("how many numbers do you want the sequence to have?: ")
        elif sequence < 1:
            print(f"{sequence} is not valid!")
            print("your sequence must be a natural number.")
            print()
            sequence = input("how many numbers do you want the sequence to have?: ")

def fibonacci():
    fibo_list = []
    num1 = 0
    num2 = 1
    count = 0

    # repeats until count == sequence
    while count < sequence:
        result = num1 + num2
        fibo_list.append(result)
        count += 1
    # [start:end:step]
    fibo_list = fibo_list[2:]
    return fibo_list

def main():
    
    while True:

        user_inputs()
        fibonacci()

        print(f"your fibonacci sequence is: {sequence}")

        again = input("would you like to generate a new sequence? y/n: ")
        if again in ["n", "no", "quit"]:
            break
        elif again in ["y", "yes"]:
            print()
            print("restarted!")
        else:
            print(f"{again} was not an valid option.")
            again = input("would you like to generate a new sequence? y/n: ")

if __name__ == "__main__":
    main()