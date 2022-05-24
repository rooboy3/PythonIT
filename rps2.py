#! usr/bin/python3
import random


def game():

    computer_count = 0
    user_count = 0

    while True:
        base_choice = ['scissors', 'paper', 'rock']
        computer_choice = random.choice(base_choice)

        user_choice = input('(scissors, paper, rock) Type your choice: ').strip().lower()
        print()
        computer_wins = 'The computer wins!'
        you_win = 'You win!'

        print(f'You played {user_choice}, the computer played {computer_choice}')
        if user_choice == 'scissors' and computer_choice == 'rock' or \
           user_choice == 'paper' and computer_choice == 'scissors' or \
           user_choice == 'rock' and computer_choice == 'paper':
            print(computer_wins)
            computer_count += 1

        elif user_choice == 'rock' and computer_choice == 'scissors' or \
            user_choice == 'scissors' and computer_choice == 'paper' or \
                user_choice == 'paper' and computer_choice == 'rock':
                print(you_win)
                user_count += 1

        else:
            if user_choice == computer_choice:
                print('Its a draw!')
                computer_count += 0
                user_count += 0

        print(f'Computer: {computer_count} - You: {user_count}')
        print()
        if computer_count == 10:
            break
        if user_count == 10:
            break

game()