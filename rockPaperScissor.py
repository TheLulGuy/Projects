import random

def converter(thing):
    if thing == 'r':
        return 'Rock'
    elif thing == 'p':
        return 'Paper'
    elif thing == 's':
        return 'Scissors'

def interface(rounds, totalRounds, user, comp):
    user = converter(user)
    comp = converter(comp)
    print(f'\n\nRound number: {rounds + 1}/{totalRounds}')
    print(f'{user} vs {comp}')


def main():
    print('Choose how many rounds you want: ')
    rounds = int(input())
    roundsCompleted = 0
    user_wins = 0
    comp_wins = 0         
    stuff = ['r', 'p', 's']

    while True:
        comp = random.choice(stuff)
        while True:
            user = input('\nRock, paper or scissors?: ')
            if user == 'r' or user == 's' or user == 'p':
                break
            else:
                print('Invalid choice')
                continue
        
        interface(roundsCompleted, rounds, user, comp)
        if user == 'r' and comp == 'p' or user == 'p' and comp == 's' or user == 's' and comp == 'r':
            print('You lose!')
            roundsCompleted += 1
            comp_wins += 1
        elif user == comp:
            print('Draw!')
            roundsCompleted += 1
        
        else:
            print('You win!')
            roundsCompleted += 1
            user_wins += 1
        
        if roundsCompleted == rounds:
            print('\nResults: ')
            print(f'{user_wins} vs {comp_wins}')
            if user_wins > comp_wins:
                print('YOU WON')
            elif comp_wins > user_wins:
                print('YOU LOST')
            else:
                print('DRAW')
            break

if __name__ == "__main__":
    main()
            