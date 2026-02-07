# return pi/e to desired accuracy
# set limit to how long accuracy can be

from math import pi, e

calc_running = True

def calculator():
    
    while calc_running:
        print("this is the pi/e calculator!")
        pie = input("choose between pi and e!: ")

        if pie not in ("pi", "Pi", "PI", "e", "E"):
            print(f"{pie} is not a valid option!")
            pie = input("choose between pi and e!: ")
        else:
            continue

        accuracy = input("select your degree of accuracy (max 15): ")
        try: 
            accuracy = int(accuracy)
        except ValueError:
            print(f"{accuracy} is not valid")
            print("your accuracy must be from 0-15 s.f.")
            continue

        # comparison statements can't be used in except cases
        # an if statement is used instead
        if int(accuracy) > 15:
            print(f"{accuracy} exceeds 15!")
            print("the degree of accuracy must not exceed 15")
        else:
            # continue/break allowed for if statements inside while loop
            # code carries onto next line of code
            continue

        if pie in ["pi", "Pi", "PI"]:
            pie = "pi"
            result = round(pi, int(accuracy))
            print(f"{result} is {pie} rounded of to {accuracy} degrees of accuracy!")
            break
        else:
            pie = "e"
            result = round(e, int(accuracy))
            print(f"{result} is {pie} rounded of to {accuracy} degrees of accuracy!")
            break

def main():

    while True:

        calculator()

        again = input("would you like to do another calculation? (q to quit): ")
        if again in ["quit", "q"]: #again = variable
            calc_running = False
        else:
            print("restarted!")
            print("")
            continue
        

if __name__ == "__main__":
    main()