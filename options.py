def print_options():
    word = "OPTIONS"
    total_width = 80
    border_width = 60
    half_width = int((total_width - border_width) / 2)
    v_pad = 1
    border = '*' * border_width
    empty_row = " " * (half_width) + "*" + " " * (border_width - 2) + "*"
    input_str = "Please select which option: "


    # --- PRINT OPTIONS BOX ---
    options = ["Play", "Exit"]
    max_opt_len = max(len(opt) for opt in options)
    
    # --- PRINT TOP BORDER ---
    print(border.center(total_width))
    print(empty_row)
    print(f"{' ' * 10}*{word.center(border_width - 2)}*")
    
    # --- PRINT EMPTY ROW
    for _ in range(v_pad):
        print(empty_row)

    # --- PRINT OPTIONS ---
    for i, opt in enumerate(options, 1):
        # Format the string so the "number. text" is a fixed block
        # Example: "1. Open File    "
        formatted_opt = f"[{i}] {opt.ljust(max_opt_len)}"
        #formatted_opt = f"{opt.ljust(max_opt_len)}"
        
        # Center that entire block inside the box
        print(f"{' ' * (half_width)}*{formatted_opt.center(border_width - 2)}*")
    
    # --- PRINT BOTTOM PORTION ---
    print(empty_row)
    print(f"{' ' * (half_width)}*{input_str.center(border_width - 2)}*")
    print(empty_row)
    
    # --- PRINT INPUT AND MOVE CURSOR --- \033 escape ANSI
    # \033[2A = cursor moves 2 row up \033[49C = cursor moves 49 spaces right
    selected = input(f"{border.center(total_width)}\r\033[2A\033[54C")
    
    # --- REPRINT BOTTOM PORTION ---
    ## so border does not disappear change after input
    print(empty_row)
    print(border.center(total_width))
    
    return int(selected), options