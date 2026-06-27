# --- GLOBAL BORDER VARIABLES ---
total_width = 80
v_pad = 1         # Top/Bottom space
border = "*" * total_width
empty_row = "*" + " " * (total_width - 2) + "*"

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
    print(border)
    for _ in range(v_pad):   ## _ naming convention for when i don't care about index i
        print(empty_row)

    for row in rows:
        print(f"*{row.center(total_width - 2)}*")
    
    # 3. Bottom
    for _ in range(v_pad):
        print(empty_row)
    print(border)


#generate_screen()