import random

user_wins = 0
computer_wins = 0


options = ["stone", "paper", "scissors"]

while True:
    user_input = input("Type stone/paper/scissors or Q to quit: ").lower()
    
    if user_input == "bye":
       break

    if user_input not in ["stone", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
   
    # stone: 0, paper: 1, scissors: 2
    computer_picks = options[random_number]
    print("computer choosed", computer_picks + ".")
    
    if user_input == "stone" and computer_picks == "scissors": 
        print("you won!")
        user_wins += 1
        continue


    elif user_input == "paper" and computer_picks == "stone": 
        print("you won!")
        user_wins += 1
        continue


    elif user_input == "scissors" and computer_picks == "paper": 
        print("you won!")
        user_wins += 1
        continue
    
    
    else:
        print("you lost!!")
        computer_wins += 1



print("you won", user_wins, "times.")
print("the computer won", computer_wins, "times.")

print("Goodbye..!")




