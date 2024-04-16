from Data.GameFuns import *


game_over = False

#############


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // (HEIGHT // 3)
            clicked_col = mouseX // (WIDTH // 3)

            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = 'O'

                winner = check_winner()
                if winner is not None:
                    print(f'Player {winner} wins!')
                    game_over = True
                elif is_board_full():
                    print("It's a tie!")
                    game_over = True
                else:####
                    AI()
                    winner = check_winner()
                    if winner is not None:
                        print(f'Player {winner} wins!')
                        game_over = True
                    elif is_board_full():
                        print("It's a tie!")
                        game_over = True
                        ######

    # Draw everything
    screen.fill(WHITE)
    draw_grid()
    draw_symbols()
    pygame.display.flip()