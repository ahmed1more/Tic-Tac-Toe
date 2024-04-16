    AI()
    winner = check_winner()
    if winner is not None:
        print(f'Player {winner} wins!')
        game_over = True
    elif is_board_full():
        print("It's a tie!")
        game_over = True


board[0][0]="X"