from board_constants import TOTAL_WIDTH, TOTAL_BORDER, TOTAL_EMPTY_ROW, V_PAD

def generate_screen():
    letters = {
        'T': ['*****', '  *  ', '  *  ', '  *  ', '  *  '],
        'I': ['*****', '  *  ', '  *  ', '  *  ', '*****'],
        'C': [' ****', '*    ', '*    ', '*    ', ' ****'],
        '-': ['     ', '     ', '*****', '     ', '     '],
        'A': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
        'O': ['*****', '*   *', '*   *', '*   *', '*****'],
        'E': ["*****", "*    ", "*****", "*    ", "*****"]
    }

    word = "TIC-TAC-TOE"
    rows = [" ".join(letters[char][i] for char in word) for i in range(5)]

    # 1. Top
    print(TOTAL_BORDER)
    for _ in range(V_PAD):   ## _ naming convention for when i don't care about index i
        print(TOTAL_EMPTY_ROW)

    for row in rows:
        print(f"*{row.center(TOTAL_WIDTH - 2)}*")
    
    # 3. Bottom
    for _ in range(V_PAD):
        print(TOTAL_EMPTY_ROW)
    print(TOTAL_BORDER)
    print()


#generate_screen()