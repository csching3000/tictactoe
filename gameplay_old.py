import random

def add_to_board(board, place, player):
    ## getting indexes of  the 2D game board array
    i, j = 0, 0
    if (isinstance(place, int)):
        i = row.get(place)
        j = col.get(place)
    ## assigning the token to game board
    if (isinstance(i, int) and isinstance(j, int)):
        board[i][j] = str(player)

def check_draw(array):
    if (len(used) == 9):
        print("Game ends with a draw")
        return True

def check_win(array, player):
    chunk_size = 3
    x_win = ['X'] * 3
    o_win = ['O'] * 3
    two_d_list = [array[i : i + chunk_size] for i in range(0, len(array), chunk_size)]
    
    for row in two_d_list:
        if ((row == x_win) or (row == o_win)):
            return True
    for col in zip(*two_d_list):
        if((list(col) == x_win) or (list(col) == o_win)):
            return True
        #print(list(col))
    if ([array[0], array[4], array[8]] == x_win or [array[2], array[4], array[6]] == x_win):
        return True
    elif ([array[0], array[4], array[8]] == o_win or [array[2], array[4], array[6]] == o_win):
        return True
    return False


game_board = [["|", "_", "|", "_", "|", "_", "|"],
              ["|", "_", "|", "_", "|", "_", "|"],
              ["|", "_", "|", "_", "|", "_", "|"]]

reference_board = [["|", "1", "|", "2", "|", "3", "|"],
                   ["|", "4", "|", "5", "|", "6", "|"],
                   ["|", "7", "|", "8", "|", "9", "|"]]

p1, p2 = '', ''
row = {1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 1, 7: 2, 8: 2, 9: 2}
col = {1: 1, 2: 3, 3: 5, 4: 1, 5: 3, 6: 5, 7: 1, 8: 3, 9: 5}
place = 0
win_flag = False
draw_flag = False
who_wins = ''


def generate_board(board, ref_board):
    for row in range(3):
        print(*board[row], end="")
        print("  ", end="")
        print(*ref_board[row])

arr = [' '] * 9
used = []
print()
while ((token := input("Choose X or O (Q to quit): ").upper()) not in ('X', 'O', 'Q')):
    print("Invalid choice, try again.")

if (token == 'Q'):
    exit(1)
elif (token == 'O'):
    p1 = 'O'
    p2 = 'X'
else:
    p1 = 'X'
    p2 = 'O'
print()
generate_board(board=game_board, ref_board=reference_board)

while(win_flag == False):
    print()
    ## p1 turn
    while ((place := int(input(f"Enter a number to place {p1}: "))) not in range(1, 10)):
        draw_flag = check_draw(used)
        if (draw_flag == True):
            exit(1)
        else:
            print("Number out of range.")
    if(draw_flag == True):
        break
    ## checks if place has already been used
    while(place in used):
        draw_flag = check_draw(used)
        if(draw_flag == True):
            exit(1)
        else:
            place = int(input("Place already used. Please pick another: "))
    
    
    print()
    arr[place - 1] = p1
    used.append(place)
    add_to_board(board=game_board, place=place, player=p1)
    print()
    generate_board(board=game_board, ref_board=reference_board)
    print()
    win_flag = check_win(array=arr, player=p1)
    if (win_flag):
        exit(1)
    

    
    ## p2's turn
    while ((place := random.randint(1, 9)) in used):
        draw_flag = check_draw(used)
        if (draw_flag == True):
            exit(1)
        else:
            place = random.randint(1, 9)
    
    print(f"{p2}'s turn")    
    arr[place - 1] = p2
    used.append(place)
    
    #print(used)
    add_to_board(board=game_board, place=place, player=p2)
    generate_board(board=game_board, ref_board=reference_board)
    win_flag = check_win(array=arr, player=p2)
    if (win_flag):
        exit(1)



'''
   1     2     3
  0,1   0,3   0,5
  0,0   0,1   0,2
   4     5     6
  1,1   1,3   1,5
  1,0   1,1   1,2
   7     8     9 
  2,1   2,3   2,5
  2,0   2,1   2,2
'''