import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand_gesture = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

print(hand_gesture[user_choice])

computer_choice = random.randint(0, 2)      # 0,  1, or 2
print("Computer chose:")
print(hand_gesture[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")     #in case the user is typing in something invalid
elif user_choice == 0 and computer_choice == 2:
    print("You win!")       # user:rock vs pc:scissors
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")      # user:scissors vs pc:rock
elif computer_choice > user_choice:
    print("You lose!")      # (pc) scissors > paper > rock (user)
elif user_choice > computer_choice:
    print("You win!")       # (user) scissors > paper > rock (pc)
elif computer_choice == user_choice:
    print("It's a draw!")   # same choice means draw
