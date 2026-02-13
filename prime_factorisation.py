# Prime Factorization - Have the user enter a number
# find all Prime Factors (if there are any) and display them.

from sympy import isprime
from math import sqrt

def user_inputs():

    is_running = True
    
    print("prime factorisation")
    print("this program accepts a natural number from the user and returns its prime factors")
    begin = input("begin? type any key. (q to quit): ")

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

    for num in range (1, number): 
        if number % num == 0 and isprime(num):
            factors_list.append(num)
            continue
        
    print(f" your number, {number}, has these prime factors: {factors_list}") 
    
def main():

    while True:
        
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