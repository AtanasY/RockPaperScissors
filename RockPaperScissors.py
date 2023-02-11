import random


def play_game_rps_sl(p1, p2):
    beats = {'R': ['S', 'L'], 'P': ['R', 'K'], 'S': ['P', 'L'],
             'K': ['S', 'R'], 'L': ['K', 'P']}
    if p1 == p2:
        print("It's a tie!")
        return 'Ties'
    elif p2 in beats[p1]:
        print("Player wins!")
        return 'Player'
    else:
        print("Computer wins!")
        return 'Computer'


game_mode = ''
score = {'Player': 0, 'Computer': 0, 'Ties': 0}
while True:
    options = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors', 'K': 'Spock', 'L': 'Lizard'}
    if game_mode == '':
        game_mode = input("Welcome!\n Choose game mode - Classic(C) or Big Bang Version(BB): ")
    if not game_mode == "C" and not game_mode == "BB":
        print("Invalid Input... Try Again!")
        continue
    if game_mode == "BB":
        Player = input("Rock(R), Paper(P), Scissors(S), Spock(K), Lizard(L): ")
    else:
        options.pop("K"), options.pop("L")
        Player = input("Rock(R), Paper(P), Scissors(S): ")
    if Player not in options:
        print("Invalid Input... Try Again!")
        continue
    Computer = random.choice(list(options.keys()))
    print(f"Player Chose: {options[Player]}\nComputer chose: {options[Computer]}")
    result = play_game_rps_sl(Player, Computer)
    score[result] += 1
    print(', '.join("{}: {}".format(k, v) for k, v in score.items()))
    restart = input("Play Again? (Y/N): ")
    if restart.lower() == 'n':
        break
print("Thanks for playing!")