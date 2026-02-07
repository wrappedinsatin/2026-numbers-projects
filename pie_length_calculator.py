# return pi/e to desired accuracy
# set limit to how long accuracy can be

from math import pi, e

calc_running = True

def calculator():
    
    while calc_running:
        print("this is the pi/e calculator!")
        pie = input("choose between pi and e!: ")

        if not pie == pi or e:
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
        except int(accuracy) > 15:
            print(f"{accuracy} exceeds 15!")
            print("the degree of accuracy must not exceed 15")
            continue

        if pie in ["pi", "Pi", "PI"]:
            pie = "pi"
            result = round(pie, accuracy)
            print(f"{result} is {pie} rounded of to {accuracy} degrees of accuracy!")
            break
        else:
            pie = "e"
            result = round(pie, accuracy)
            print(f"{result} is {pie} rounded of to {accuracy} degrees of accuracy!")
            break

def main():

    while True:

        calculator()

        again = input("would you like to do another calculation? (q to quit): ")
        if input in ["quit", "q"]:
            calc_running = False
        else:
            print("restarted!")
            print("")
            break
        

if __name__ == "__main__":
    main()