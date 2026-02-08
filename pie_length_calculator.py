# return pi/e to desired accuracy
# set limit to how long accuracy can be

from math import pi, e

def calculator():
    
    global calc_running
    calc_running = True

    while calc_running:
        print("this is the pi/e calculator!")
        pie = input("choose between pi and e!: ")

        if pie in ["q", "quit", 'exit', "end"]:
            calc_running = False
            return
            # not every if statement needs an else pairing

        while True:
            if pie not in ("pi", "Pi", "PI", "e", "E"):
                print(f"{pie} is not a valid option!")
                pie = input("choose between pi and e!: ")
            else:
                break
        
        while True:
            accuracy = input("select your degree of accuracy (min 0, max 15): ")
            try: 
                accuracy = int(accuracy)
                if int(accuracy) > 15:
                    print(f"{accuracy} exceeds 15!")
                    print("the degree of accuracy must not exceed 15")
                    accuracy = input("select your degree of accuracy (max 15): ")
                elif int(accuracy) < 0:
                    print(f"{accuracy} is less than zero!")
                    print("please select an integer between 0-15.")
                    accuracy = input("select your degree of accuracy (max 15): ")
            except ValueError:
                print(f"{accuracy} is not valid")
                print("your accuracy must be from 0-15 s.f.")
                accuracy = input("select your degree of accuracy (max 15): ")

        # comparison statements can't be used in except cases
        # an if statement is used instead
            # continue/break allowed for if statements inside while loop

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

        again = input("would you like to do another calculation? (y to continue, q to quit): ")
        if again in ["quit", "q"]: #again = variable
            break
        else:
            print("restarted!")
            print("")
        

if __name__ == "__main__":
    main()