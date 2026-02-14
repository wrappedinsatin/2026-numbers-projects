
def what_is_happy(): # works as intended
    print()
    print("the definition of a happy number is as follows:")
    print()
    print("starting with a positive integer," \
    "replace the number by the sum of the squares of its digits, "
    "and repeat the process until the number equals 1 (where it will stay), "
    "or it loops endlessly in a cycle which does not include 1.")
    print()
    print("a number in which this process ends in 1 is a happy number," \
    "while those that do not end in 1 are unhappy numbers.") 

def user_input(): # works as intended

    while True:

        n = input("enter a natural number:")
        try:
            number = int(n)

            if number < 1:
                print(f"{number} is not a natural number.")
                print("please enter a natural number.")
                continue

            return number
        
        except ValueError:
            print(f"{n!r} is invalid. type in a positive integer.")

def happy_checker(number: int) -> bool:
    
    seen = set()
    while True:
        if number == 1:
            return True
        if number in seen:
            return False
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))


def main():
    
    while True:

        what_is_happy()
        print()
        number = user_input()
        is_happy = happy_checker(number)
        
        if is_happy: # true/false
            print(f"{number} is a HAPPY number!")
        else:
            print(f"{number} is an UNHAPPY number!")


if __name__ == "__main__":
    main()
