# Prime Factorization - Have the user enter a number
# find all Prime Factors (if there are any) and display them.

from sympy import isprime
from math import sqrt

global is_running
is_running = True

def user_inputs():
    
    print("prime factorisation")
    print("this program accepts a natural number from the user and returns its prime factors")
    begin = input("begin? type any key. (q to quit): ")

    if begin in ("q", "quit", "Q", "QUIT", "Quit"):
        exit()

def check_input():

    global number 
    while True:

        number = input("what number would you like to factorise? (q to quit): ")
        
        if number in ("q", "quit", "Q", "QUIT"):
            exit()
        
        try:

            number = int(number)
            if number < 1:
                print(f"{number} is not valid.")
                print()
            else:
                break

        except (ValueError, TypeError):
            print(f"{number} is not valid.")
            print("your input must be a natural number")
            print()

def factorise():

    factors_list = []

    for num in range (1, number): 
        if number % num == 0 and isprime(num):
            factors_list.append(num)
        # no need for continue, doesn't do anything
    print(f"your number, {number}, has these prime factors: {factors_list}")

def main():

    while is_running:
        
        user_inputs()
        check_input()
        factorise()

        again = input("would you like to factorise another number? (y/n)").lower()

        if again in ("n", "no", "quit"):
            print("thanks for trying!")
            break
        elif again in ("y", "yes", "again"):
            print()
            print("restarted!")
            print()
        else:
            print(f"{again} is not a valid input.")
            again = input("would you like to factorise another number? (y/n)").lower()

if __name__ == '__main__':
    main()

