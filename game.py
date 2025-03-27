import random
import time

def displayintro():
    print('''You are in a land full of dragons. In front of you '
    'you see two caves. In one cave, the dragon is friendl;y and will share his treasure with you'
    'other other dragon is greedy and hungry, he will eat you on sight''')

    print()
    
    def chooseCave():
        cave = ''
        while cave != '1' and cave !='2':
            print('which cave will you go into (1 or 2)')
            cave = input()
        
        return cave
    
    def checkCave(chosenCave):
        print('you approach the cave...')
        time.sleep(2)
        print('Its dark and spooky...')
        time.sleep(2)
        print('A large dragon jumps out in front of you! He opens his jaws'
        'and...')
        print()
        time.sleep(2)

        friendlycave = random.randint(1, 2)

        if chosenCave == str(friendlycave):
            print('Gives you is treasure!')
        else:
            print('Gobbles you down in one bite')
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayintro()
    cavenumber = chooseCave()
    checkCave(cavenumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()