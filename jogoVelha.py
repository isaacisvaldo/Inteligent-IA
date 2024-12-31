import random  

# Inicialização 
board = [' ' for _ in range(9)]  
board[4] = 'X'  

def show_board():  
    print(f"{board[0]}|{board[1]}|{board[2]}")  
    print("-+-+-")  
    print(f"{board[3]}|{board[4]}|{board[5]}")  
    print("-+-+-")  
    print(f"{board[6]}|{board[7]}|{board[8]}")  

def check_winner():  
   
    for i in range(0, 9, 3):  
        if board[i] == board[i+1] == board[i+2] != ' ':  
            return board[i]  
 
    for i in range(3):  
        if board[i] == board[i+3] == board[i+6] != ' ':  
            return board[i]  
  
    if board[0] == board[4] == board[8] != ' ':  
        return board[0]  
    if board[2] == board[4] == board[6] != ' ':  
        return board[2]  
  
    if ' ' not in board:  
        return 'D'  

    return None  

def player_move():  
    while True:  
        move = input("Insira sua jogada (1-9): ")  
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)-1] == ' ':  
            return int(move)-1  
        print("Jogada inválida. Tente novamente.")  

def computer_move():  
    while True:  
        move = random.randint(0, 8)  
        if board[move] == ' ':  
            return move  


while True:  
    show_board()  
    player_move_index = player_move()  
    board[player_move_index] = 'O'  
    result = check_winner()  
    if result is not None:  
        show_board()  
        if result == 'D':  
            print("Empate!")  
        elif result == 'O':  
            print("Você venceu!")  
        else:  
            print("O computador venceu!")  
        break  

    computer_move_index = computer_move()  
    board[computer_move_index] = 'X'  
    result = check_winner()  
    if result is not None:  
        show_board()  
        if result == 'D':  
            print("Empate!")  
        elif result == 'X':  
            print("O computador venceu!")  
        else:  
            print("Você venceu!")  
        break