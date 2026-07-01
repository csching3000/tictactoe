from board_constants import TOTAL_WIDTH, BORDER_WIDTH, HALF_WIDTH, BORDER, V_PAD

# --- GLOBAL BORDER VARIABLES ---
empty_row = " " * (HALF_WIDTH) + "*" + " " * (BORDER_WIDTH - 2) + "*"

def print_options():
    
    word = "OPTIONS"
    options = ["Play", "Exit"]
    input_str = "Please select which option: "

    # --- PRINT OPTIONS BOX ---

    max_opt_len = max(len(opt) for opt in options)
    
    # --- PRINT TOP BORDER ---
    print(BORDER.center(TOTAL_WIDTH))
    print(empty_row)
    print(f"{' ' * 10}*{word.center(BORDER_WIDTH - 2)}*")
    
    # --- PRINT EMPTY ROW
    for _ in range(V_PAD):
        print(empty_row)

    # --- PRINT OPTIONS ---
    for i, opt in enumerate(options, 1):
        # Format the string so the "number. text" is a fixed block
        # Example: "1. Open File    "
        formatted_opt = f"[{i}] {opt.ljust(max_opt_len)}"
        #formatted_opt = f"{opt.ljust(max_opt_len)}"
        
        # Center that entire block inside the box
        print(f"{' ' * (HALF_WIDTH)}*{formatted_opt.center(BORDER_WIDTH - 2)}*")
    
    # --- PRINT BOTTOM PORTION ---
    print(empty_row)
    print(f"{' ' * (HALF_WIDTH)}*{input_str.center(BORDER_WIDTH - 2)}*")
    print(empty_row)
    
    # --- PRINT INPUT AND MOVE CURSOR --- \033 escape ANSI
    # \033[2A = cursor moves 2 row up \033[49C = cursor moves 49 spaces right
    selected = input(f"{BORDER.center(TOTAL_WIDTH)}\r\033[2A\033[54C")
    
    # --- REPRINT BOTTOM PORTION ---
    ## so border does not disappear change after input
    print(empty_row)
    print(BORDER.center(TOTAL_WIDTH))
    print()

    return int(selected), options