import sys
from screen import generate_screen
from options import print_options
from gameplay import game

def main():
    try:
        generate_screen()
        print()
        selected = print_options()
        while (int(selected) != 2 and int(selected) != 1):
            selected = input("Option not listed. Pick another: ")
        if (int(selected) == 1):
            game()
        elif(selected == 2):
            print("Goodbye!")
                
    except Exception:
        print("Error")

if __name__ == "__main__":
    sys.exit(main())