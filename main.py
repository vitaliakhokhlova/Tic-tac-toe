from random import randrange

def display_board(board):
    corner="+"
    horizontal_line_symbol='-'
    vertical_line_symbol="|"
    cell_width=7
    n_cells=3
    
    cell_top=horizontal_line_symbol*cell_width+corner
    cell_inside=' '*cell_width+vertical_line_symbol
    
    line=corner+cell_top*n_cells
    empty_row=vertical_line_symbol+cell_inside*n_cells
    print(line)
    for row in board:
        c=empty_row
        print(empty_row)
        for i in range(len(row)):
            c=c[:4+i*(cell_width+1)]+str(row[i])+c[5+i*(cell_width+1):]
        print(c)
        print(empty_row)
        print(line)


def enter_move(board):
    return check(board, 'O')
    
def check(board, sign):
    stop=False
    while True:
        if sign=='X':
            move=randrange(8)+1
        else:
            move=input("Enter the free cell number:")
        t=move_to_tuple(move)
        free_fields=make_list_of_free_fields(board)

        if t in free_fields:
            update_board(board, move, sign)
            display_board(start_board)
            if victory_for(board, sign):
                print(sign+" won")
                return True
            break
        else:
            print("Not free number")

def move_to_tuple(move):
    s=int(move)-1
    i=s//3
    j=s%3
    return i, j

def update_board(board, move, sign):
    i, j=move_to_tuple(move)
    board[i][j]=sign

def make_list_of_free_fields(board):
    l=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!="X" and board[i][j]!='O':
                l.append((i,j))
    return l
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[1][1]==sign:
        for i in range(3):
            if board[0][i]==sign:
                if board[2][2-i]==sign: return True
        if board[1][0]==board[1][2]==sign: return True
    else:
        for i in [0,2]:
            if board[i][i]!=sign:
                if board[2-i][2-i]!=sign: return False
                else:
                    if board[2-i][i]==board[2-i][1]==sign: return True
                    if board[i][2-i]==board[1][2-i]==sign: return True
    return False



def draw_move(board):
    return check(board, 'X')
    # The function draws the computer's move and updates the board.

def init():
    start_board=[]
    for i in range(3):
        row=[]
        for j in range(3):
            row.append((j+1)+i*3)
        start_board.append(row)
    start_board[1][1]='X'
    return start_board

start_board=init()
display_board(start_board)
stop=False

while not stop:
    stop=enter_move(start_board)
    if stop: break
    stop=draw_move(start_board)
    
    
