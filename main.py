import random
print("Welcome to the Rock Paper Scissors game!\n")
computer_choice= random.randint(0,2)
user_choice=int(input("What would you like to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choices= ["Rock", "Paper", "Scissors"]
art=[("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """), ("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """), ("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)]
print(f"\nThe computer has picked {choices[computer_choice]}\n {art[computer_choice]}")
print(f"You have picked {choices[user_choice]}\n {art[user_choice]}")

if computer_choice==user_choice:
  print("It's a draw!")
elif computer_choice==0 and user_choice==1:
  print("You win!")
elif computer_choice==0 and user_choice==2:
  print("You lose!")
elif computer_choice==1 and user_choice==0:
  print("You lose!")
elif computer_choice==1 and user_choice==2:
  print("You win!")
elif computer_choice==2 and user_choice==0:
  print("You win!")
elif computer_choice==2 and user_choice==1:
  print("You lose!")
