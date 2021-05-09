import random
from termcolor import colored

spades = ['♠ A', '♠ 1', '♠ 2', '♠ 3', '♠ 4', '♠ 5', '♠ 6', '♠ 7', '♠ 8', '♠ 9', '♠ K', '♠ Q', '♠ J']
hearts = ['♥︎ A', '♥︎ 1', '♥︎ 2', '♥︎ 3', '♥︎ 4', '♥︎ 5', '♥︎ 6', '♥︎ 7', '♥︎ 8', '♥︎ 9', '♥︎ K', '♥︎ Q', '♥︎ J']
cloves = ['♣︎ A', '♣︎ 1', '♣︎ 2', '♣︎ 3', '♣︎ 4', '♣︎ 5', '♣︎ 6', '♣︎ 7', '♣︎ 8', '♣︎ 9', '♣︎ K', '♣︎ Q', '♣︎ J']
diamonds = ['♦︎ A', '♦︎ 1', '♦︎ 2', '♦︎ 3', '♦︎ 4', '♦︎ 5', '♦︎ 6', '♦︎ 7', '♦︎ 8', '♦︎ 9', '♦︎ K', '♦︎ Q', '♦︎ J']
cards = [spades, hearts, cloves, diamonds]

def chooser(A=False):
    if A == False:
        choice = random.choice(random.choice(cards))
        return choice
    else:
        choices = [1, 11]
        return random.choice(choices)

def interface(playerCards, compCards, playerScore, compScore):
    print(f'\nYour cards: ')
    print(playerCards)
    print(colored('Score: {}'.format(playerScore), 'blue'))
    print("Dealer's cards: ")
    if len(compCards) == 0:
        print('?')
    else:
        print(compCards)
    print(colored('Score: {}'.format(compScore), 'red'))
    
    
def main():
    playerScore, compScore, playerCards, compCards = 0, 0, '', ''
    playerCards = chooser() + '  ' + chooser()
    print(playerCards)

if __name__ == "__main__":
    main()

#♣︎♥︎♦︎