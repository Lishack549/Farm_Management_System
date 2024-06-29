board=[' ',' ',' ',
       ' ',' ',' ',
       ' ',' ',' ']
def print_board():

    print(board[0] ,'|', board[1] ,'|',board[2])
    print(board[3],'|',board[4],'|',board[5])
    print(board[6],'|',board[7],'|',board[8])
def check_win(player):
    for i in range(0,9,3):
        if board[i]==board[i+1]==board[i+2]==player:
            return True
    for i in range(3):
        if board[i]==board[i+3]==board[i+6]==player:
            return True
        if board[0]==board[4]==board[8]==player:
            return True
        if board[2]==board[4]==board[6]==player:
            return True
    return False
def play_game():
    print("welcome to tic tac toe")
    print_board()
    player='X'
    while True:
        move=int(input("player"+player+"enter move from 0-8"))
        if board[move]==' ':
            board[move]=player
        else:
            print('invalid mobe try again ')
            continue
        if check_win(player):
            print('congrats'+player+'player won game')
            break
        if ' 'not in board:
            print('its a tie')
            break
    if player=='X':
        player='O'
    else:
        player='X'
    print_board()
play_game()