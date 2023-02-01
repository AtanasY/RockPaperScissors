import random
options = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']


def play_game(p1, p2):
    beats = {'Rock': ['Scissors', 'Lizard'], 'Paper': ['Rock', 'Spock'], 'Scissors': ['Paper', 'Lizard'],
             'Spock': ['Scissors', 'Rock'], 'Lizard': ['Spock', 'Paper']}
    if p1 == p2:
        print("It's a tie!")
    elif p2 in beats[p1]:
        print("Player wins!")
    else:
        print("Computer wins!")


while True:
    print("Welcome!")
    Player = input("Rock, Paper, Scissors, Spock, Lizard: ")
    if Player not in options:
        print("Invalid Input... Try Again!")
        continue
    print(f'Player Chose: {Player}')
    Computer = random.choice(['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard'])
    print(f"Computer chose: {Computer}")
    play_game(Player, Computer)
    restart = input("Play Again? (Y/N): ")
    if restart.lower() == 'n':
        break
print("Thanks for playing!")