import sys
from screen import generate_screen
from options import print_options
from gameplay import game

def main():
    try:
        generate_screen()
        selected, op = print_options()
        op_index = [x + 1 for x in list(range(len(op)))]
        while (int(selected) not in op_index ):
            selected = input("Option not listed. Pick another: ")
        if (int(selected) == op_index[0]):
            print()
            generate_screen()
            print("\033[2A")
            game()
        elif(selected == op_index[1] ):
            print("Goodbye!")

        ## --- one line while loop
        '''while int(selected := print_options()[0]) not in range(1, len(print_options()[1]) + 1):
            pass '''
        
    except Exception as e:
        if (type(e).__name__ == "ValueError"):
            print("Invalid value entered")
        else:
            print(type(e).__name__)

if __name__ == "__main__":
    sys.exit(main())