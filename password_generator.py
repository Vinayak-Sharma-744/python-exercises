import random

letters = 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

intro = print("welcome to password generator") 

user_input1 = int(input("how many alphabets you like in your password"))
print(user_input1)

user_input2 = int(input("how many symbols you like in your password"))
print(user_input2)

user_input3 = int(input("how many numbers you like in your password"))
print(user_input3)

#Eazy Level
# password = ""

# for char in range(1, user_input1 + 1):
#   password += random.choice(letters)

# for char in range(1, user_input2 + 1):
#   password += random.choice(symbols)

# for char in range(1, user_input3 + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, user_input1 + 1):
  password_list += random.choice(letters)

for char in range(1, user_input2 + 1):
  password_list += random.choice(symbols)

for char in range(1, user_input3 + 1):
  password_list += random.choice(numbers)


random.shuffle(password_list)


password = " "
for char in password_list:
  password += char

print(f"Your password is: {password}")


