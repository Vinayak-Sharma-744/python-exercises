import random
user_input = str(input("choose Heads or Tails!! "))

comp_ans = random.randint(0, 1)

if comp_ans == 0:
    print("Heads")

elif comp_ans == 1:
    print("Tails")

