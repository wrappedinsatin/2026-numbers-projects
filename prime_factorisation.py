# Prime Factorization - Have the user enter a number
# find all Prime Factors (if there are any) and display them.

from sympy import nextprime
from math import sqrt

def user_inputs():

    is_running = True
    
    print("prime factorisation")
    print("this program accepts a natural number from the user and returns its prime factors")
    begin = input("begin? (q to quit): ")

    if begin in ("q", "quit", "Q", "QUIT", "Quit"):
        exit()

def check_input():
    
    global number 

    while True:
        number = input("what number would you like to factorise?: ")

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
            number = input("what number would you like to factorise? (q to quit): ")

def factorise():

    factors_list = []

    end_range = round(sqrt(number))

    for num in range (1, end_range): 
        if number % num == 0:
            factors_list.append(num)
            num = nextprime(num) #sympy function to update num to the next prime
            continue
        else:
            return factors_list 
            break

    print(f"your number, {number}, has these prime factors: {factors_list}")

def main():

    while True:
        
        user_inputs()
        check_input()
        factorise()

        again = input("would you like to factorise another number? (y/n)").lower()

        if again in ("n", "no", "quit"):
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