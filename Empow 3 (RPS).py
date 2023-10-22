import random as rd

def rand():
    return str(rd.randint(1, 3))

def compare(player, computer): #1 for win 2 for lose
    if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        return 1
    return 2
    
rps = {1: "Rock", 2: "Paper", 3: "Scissors"}
running = True
while running:
    print()
    response = 1
    player = int(input("Rock (1), Paper (2), or Scissors (3)?: "))
    print("You chose: " + rps[player])
    computer = int(rand())
    print("The computer chose: " + rps[computer])
    while player == computer:
        print("You and the computer both chose " + rps[player] + ", so you tied.\nPlease choose again.\n")
        player = int(input("Rock (1), Paper (2), or Scissors (3)?"))
        print("You chose: " + rps[player])
        computer = int(rand())
        print("The computer chose: " + rps[computer])
    if compare(player, computer) == 1:
        response = input("You won since " + rps[player] + " beats " + rps[computer] + "! Good job! 1 to play again 2 to quit: ")
    else:
        response = input("You lost since " + rps[player] + " loses to " + rps[computer] + ". Too bad :( 1 to play again 2 to quit: ")

    if response == "2":
        print("\n\nThanks for playing!!")
        running = False
