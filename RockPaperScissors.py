import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
spock = 'Spock'
lizard = 'Lizard'

while True:
    player_move = input("Choose [R] - Rock, [P] - Paper, [S] - Scissors, [SP] - Spock or [L] - Lizard: ")
    if player_move == "R":
        player_move = rock
    elif player_move == "P":
        player_move = paper
    elif player_move == "S":
        player_move = scissors
    elif player_move == "SP":
        player_move = spock
    elif player_move == "L":
        player_move = lizard
    else:
        raise SystemExit("Input not yet added. Try again...")
    computer_random_number = random.randint(1, 5)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    if computer_random_number == 2:
        computer_move = paper
    if computer_random_number == 3:
        computer_move = scissors
    if computer_random_number == 4:
        computer_move = spock
    if computer_random_number == 5:
        computer_move = lizard
    print(f'The computer chose {computer_move}.')
    if (player_move == rock and (computer_move == scissors or computer_move == lizard)) or \
            (player_move == paper and (computer_move == rock or computer_move == spock)) or \
            (player_move == scissors and (computer_move == paper or computer_move == lizard)) or \
            (player_move == spock and (computer_move == rock or computer_move == scissors)) or \
            (player_move == lizard and (computer_move == paper or computer_move == spock)):
        print("You win!")
    elif player_move == computer_move:
        print("Draw!")
    else:
        print("You lose!")
    restart = input("Would you like to play again? [Y] - Yes or [N] - No: ")
    if restart == "Y":
        continue
    else:
        print("Thanks for playing!")
        break
