from game import Game

def main():
    game = Game()
    while True:
        game.start_game()
        if not game.ask_to_continue("Wanna play again?(y/n) "):
            break
    # Assuming the first player is always the human player
    human_player = game.players[0]
    print(f"Your final amount of money is: {human_player.money}")


if __name__ == '__main__':
    main()
