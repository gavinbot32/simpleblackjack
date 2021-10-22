
import random
while True:
    # main
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    total = 0

    stand = False
    #this starts the dealers turn
    def dealerHand(total):
        dealTotal = 0
        global stand
        while True:
            print("Your hand total:", total)
            print("Dealers Hand total:", dealTotal)
            if dealTotal > 21:
                input("You Win")
                stand = True
                return
            elif dealTotal == 21:
                # since 21 is the highest you can go without a bust unless player got a 21 dealer auto wins
                input("You Lose")
                stand = True
                return
            if dealTotal >= 17:
                if dealTotal > total:
                    # this will stand rendering all totals complete and determining the win con
                    print("Dealer Stands ")
                    input("you lose")
                    stand = True
                    return

                elif dealTotal <= total:
                    # this will hit and remove the first instance of the card from the deck
                    print("Dealer Hits")
                    handChoice = random.choice(deck)
                    dealTotal += handChoice
                    print(handChoice)
                    deck.remove(handChoice)
                    input()
            else:
                # this will hit and remove the first instance of the card from the deck
                print("Dealer Hits")
                handChoice = random.choice(deck)
                dealTotal += handChoice
                print(handChoice)
                deck.remove(handChoice)
                input()
    #this is your turn
    while True:
        print("Your hand total:",total)
        if total > 21:
            input("you lose")
            break
        elif total == 21:
            #if dealer hits 21 tie goes to player so if total == 21 player auto wins
            input("you win")
            break
        choice = input("Hit or Stand")
        if not choice.isalpha():
            input("Please enter the given options")
        else:
            choice = choice.lower()
            #this will hit and remove the first instance of the card from the deck
            if choice == 'hit':
                handChoice = random.choice(deck)
                total += handChoice
                print(handChoice)
                deck.remove(handChoice)
                input()
            elif choice == 'stand':
                # this will stand rendering your total complete
                dealerHand(total)
        #if stand = true game is over
        if stand:
            break
    #Restart? yes/no
    restart = input("Do you want to play again? Yes/No ")
    if restart.isalpha():
        restart = restart.lower()
        if "yes" in restart:
            input("Press enter to play again")
        else:
            break
    else:
        break

    #end
input("Thanks for playing")

#
# Notes
# The Dealers AI system check if the dealers hand is greater than or equal to 17 if it is it will ask if its 18, 19, or 20 if it is 18, 19, or 20 it will check
# if its hand is greater than the players hand if it is it will stand however if its not it will hit because then it has a chance at winning, if its hand is 17
#     it will check if the players hand is greater than its hand. if it is it will hit. if its equal it will hit if its less it will stand.