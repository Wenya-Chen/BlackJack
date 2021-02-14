
import random
dealer_cards = []       # dealer cards
player_cards = []       # player cards

# deal the cards
# dealer cards
while len(dealer_cards)  != 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealer has: X &", dealer_cards[1])

# player cards
while len(player_cards)  != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("You have ", player_cards)

# sum of dealer cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

# sum of player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit?  "))
    if action_taken == "hit":
        player_cards.append(random.randint(1,11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
        else:
            print("You win!")
            break

# compare the sums of the cards between dealers and players
if sum(player_cards) > 21:
    print("You BUSTED! Deal wins.")
elif sum(player_cards) == 21:
    print("You have BLACKJACK! You Win!! 21")