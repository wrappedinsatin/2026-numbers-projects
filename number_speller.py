
import quit_option, confirm_number as check

def speller(output):
    pass

def main():
    
    while True:
        quit_option.begin()
        output = check.confirm_number()
        
        if isinstance(output, int):
            check.confirm_integer(output)
            print(f"integer: {output}")
        elif isinstance(output, float):
            print(f"float: {output}")
        
        if check.is_negative(output):
            print(f"negative {output}")
        else:
            print(f"(positive) {output}")
        quit_option.quit()

if __name__ == "__main__":
    main()
