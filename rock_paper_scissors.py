#TASK-2
from random import choice
arr=["rock","paper","scissors"]
total=0#user points
tota=0#comp points
while True:
    print("1.rock 2.paper, 3.scissors 4.exit")
    user=input().lower()
    computer=choice(arr)
    if user == computer:
        print("It's a tie! No points")
    elif (user == "rock" and computer == "scissors") \
     or (user == "paper" and computer == "rock") \
     or (user == "scissors" and computer == "paper"):
        print("User wins this round!")
        total += 1   
    elif user=="exit":
        break
    else:
        print("Computer wins this round!")
        tota += 1   
if total > tota:
    print("User won the game! Win points", total)
elif tota > total:
    print("Computer won the game! Win points",tota)
else:
    print("It's a draw overall!")

