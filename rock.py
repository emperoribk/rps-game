import random
print('Welcome to Rock, Paper and Scissors')

option = input('Do you want to play against computer or human: ')
list_display = ['rock','paper','scissors']

if option=='computer':
    player_b_name = input('Player B input your name: ')
    computer_number = True
    while computer_number:
        computer_choice =random.choice(list_display)
        player_b = input('Enter your choice of game Player B: ')
        if computer_choice == 'rock' and player_b == 'paper':
            print(f"computer's choice was {computer_choice}")
            print(f'Player B {player_b_name} beat computer')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                computer_number = True
            else:
                computer_number = False
        elif computer_choice == 'rock' and player_b == 'scissors':
            print(f"computer's choice was {computer_choice}")
            print(f'computer beat {player_b_name}')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                computer_number = True
            else:
                computer_number = False
        elif computer_choice == 'paper' and player_b == 'rock':
            print(f"computer's choice was {computer_choice}")
            print(f'computer beat {player_b_name}')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                computer_number = True
            else:
                computer_number = False
        elif computer_choice == 'scissors' and player_b == 'rock':
            print(f"computer's choice was {computer_choice}")
            print(f'Player B {player_b_name} beat computer')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                computer_number = True
            else:
                computer_number = False
        elif computer_choice == 'scissors' and player_b == 'paper':
            print(f"computer's choice was {computer_choice}")
            print(f'computer beat {player_b_name}')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                computer_number = True
            else:
                computer_number = False
        elif computer_choice == 'paper' and player_b == 'scissors':
            print(f"computer's choice was {computer_choice}")
            print(f'Player B {player_b_name} beat computer')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                computer_number = True
            else:
                computer_number = False
        else:
            print(f"computer's choice was {computer_choice}")
            print('Nobody wins')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                computer_number = True
            else:
                computer_number = False
elif option == 'human':
    player_a_name = input('Player A input your name: ')
    player_b_name = input('Player B input your name: ')
    number = True
    while number:
        player_a = input('Enter your choice of game Player A: ')
        player_b = input('Enter your choice of game Player B: ')
        if player_a=='rock' and player_b=='paper':
            print(f'Player B {player_b_name} wins')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                number = True
            else:
                number = False
        elif player_a =='paper' and player_b=='scissors':
            print(f'Player B {player_b_name} wins')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                number = True
            else:
                number = False
        elif player_a =='scissors' and player_b=='rock':
            print(f'Player B {player_b_name} wins')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                number = True
            else:
                number = False
        elif player_a=='paper' and player_b=='rock':
            print(f'Player A {player_a_name} wins')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                number = True
            else:
                number = False
        elif player_a=='scissors' and player_b=='paper':
            print(f'Player A {player_a_name} wins')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                number = True
            else:
                number = False
        elif player_a=='rock' and player_b=='scissors':
            print(f'Player A {player_a_name} wins')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                number = True
            else:
                number = False
        else:
            print('Nobody wins')
            again = input('Do you wish to continue: ')
            if again == 'yes':
                number = True
            else:
                number = False
