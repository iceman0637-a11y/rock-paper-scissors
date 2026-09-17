import random

print("===================\nRock Paper Scissors\n===================")
player = int(input("Pick a number: \n1)✊\n2)✋\n3)✌️\nPick a number: "))
computer = random.randint(1, 3)

if player == 1:
    print("You chose: ✊")
elif player == 2:
    print("You chose: ✋")
elif player == 3:
    print("You chose: ✌️")

if computer == 1:
    print("CPU chose: ✊")
elif computer == 2:
    print("CPU chose: ✋")
elif computer == 3:
    print("CPU chose: ✌️")

if player == computer:
    print("Tie!")
elif player == 1 and computer == 2:
    print("The computer won!")
elif player == 1 and computer == 3:
    print("The player won!")
elif player == 2 and computer == 1:
    print("The player won!")
elif player == 2 and computer == 3:
    print("The computer won!")
elif player == 3 and computer == 1:
    print("The computer won!")
elif player == 3 and computer == 2:
    print("The player won!")


