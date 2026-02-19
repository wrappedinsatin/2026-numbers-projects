
def confirm_number() -> int | float: # expects int/float
    
    while True:
    
        number = input("what is your number?: ")
        try:
            output = int(number)
            return output
        except ValueError:
            try:
                output = float(number)
                return output
            except ValueError:
                print(f"invalid input: {number} is not a number.")

def is_negative(output):
    if output < 0:
        return True
    else:
        return False

def confirm_integer(output):
    try:
        output = int(output)
        return output
    except ValueError:
        pass # after going through confirm_number, if not an int, output must be a float
