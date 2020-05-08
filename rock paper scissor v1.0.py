import random as rd

print ('WELCOME TO THE ROCK - PAPER - SCISSOR GAME. A 2000 YEAR OLD GAME.','\n')

Player_choice = input('Make your choice: R for rock; P for paper; S for scissor:''\n')
if Player_choice == ('R') or Player_choice == ('r'):
    print ('You have choose: rock')
if Player_choice == ('P') or Player_choice == ('p'):
    print ('You have choose: paper')
if Player_choice == ('S') or Player_choice == ('s'):
    print ('You have choose: scissor')

#Computer choice with random module can choose ('r','p','s')

Computer_choice = rd.choice(['r','p','s'])
dic = {'r':'rock', 'p':'paper', 's':'scissor'}
print ('Computer choice was:', dic[Computer_choice])

#choose the winner with player choosing 'R'

#Player choice 'R'

if Player_choice == Computer_choice:
        print ('draw')
if Player_choice == 'r':
    if Computer_choice == 'p':
        print('You lost.')
    elif Computer_choice == 's':
        print('You won.')

        
#Player choice 'P'

if Player_choice == 'p':
    if Computer_choice == 's':
        print('You lost.')
    elif Computer_choice == 'r':
        print('You won.')
    

    
#Player choice 'S'


if Player_choice == 's':
    if Computer_choice == 'r':
        print('You lost.')
    elif Computer_choice == 'p':
        print('You won.')

        
input('PRESS ENTER TO EXIT')