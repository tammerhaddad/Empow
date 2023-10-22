import random

values = ['Two','Three','Four','Five','Six', 'Seven',
'Eight','Nine','Ten','Jack','Queen','King','Ace']
suits = ['Hearts','Spades','Diamonds','Clubs']
deck = []
for v in values:
    for s in suits:
        deck.append(v + " of " + s)
running = True

while running:
    print()
    random.shuffle(deck)
    hand = []
    for i in range (5):
        hand.append(deck[i])
    print("Player Hand: ")
    for i in hand:
        print("   " + i)
    cont = input("Generate again? (y/n): ")
    if cont == "n" or cont == "N":
          running = False
