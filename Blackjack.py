# Author: Grant Horner (h.grant.horner@gmail.com)
# Create an interactive game of Blackjack
# Draw between 1-11

import random

print("Hi there! What's your name?")
name = input("Enter your name: ")
print("Nice to meet you " + name +"!")
play = input("Want to play? (y or n)\n")
while play != 'y' and play != 'n':
    play = input("Please write y for yes or n for no.\n")
while play == 'y':
    print("Here are your cards.")
    # Deal player and dealer 2 cards
    cards = [random.randint(1,11),random.randint(1,11)]
    dcards = [random.randint(1,11),random.randint(1,11)]
    print(cards)
    draw = input("Want to draw a card? (y or n)\n")
    while draw == 'y' and play == 'y':
        cards.append(random.randint(1,11))
        if sum(dcards) <= 16:
            dcards.append(random.randint(1,11))
        print(cards)
        if (sum(dcards) == 21 and sum(cards) == 21):
            draw = 'x'
            play = input("Looks like we both got 21! Play again? (y or n)\n")
        elif sum(dcards) > 21 and sum(cards) > 21
            draw = 'x'
            play = input("Oops! Looks like we both went over. Play again? (y or n)\n") 
        elif sum(dcards) == 21 and sum(cards) != 21:
            draw = 'x'
            play = input("I've got blackjack! Play again? (y or n)\n")
        elif sum(dcards) != 21 and sum(cards) == 21:
            draw = 'x'
            play = input("You've got blackjack. You win! Play again? (y or n)\n")
        elif sum(dcards) > 21 and sum(cards) < 21:
            draw = 'x'
            play = input("I went over. You win! Play again? (y or n)\n")
        elif sum(dcards) < 21 and sum(cards) > 21:
            draw = 'x'
            play = input("Looks like you went over. Play again? (y or n)\n")
        else:
            draw = input("Want to draw again? (y or n)\n")
    if draw == 'n' and play == 'y':
        print("Alright. I've got "+ str(sum(dcards)) +" and you have "+ str(sum(cards))+".")
        if sum(cards) > sum(dcards):
            play = input("You win! Play again? (y or n)\n")
        elif sum(cards) < sum(dcards):
            play = input("Looks like I win. Play again? (y or n)\n")
        else:
            play = input("Looks like a draw. Play again? (y or n)\n")
print("Nice playing with you "+name+".")