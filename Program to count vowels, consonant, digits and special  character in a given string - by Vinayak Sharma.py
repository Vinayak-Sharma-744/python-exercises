# Python3 Program to count vowels,consonant, digits and special character in a given string

# Declare a Function to count number of vowels, consonant, digits and special character in a string

def countCharacterType(str):
    
    # Declare the variable vowels,
    # consonant, digit and special
    # characters
    
    vowels = 0
    consonant = 0
    specialChar = 0
    digit = 0
    spaces = 0

    # len(str) function to count number of character in given string.
    # here ch stands for character (which is entered by the user)
    
    for i in range(0, len(str)):

        ch = str[i]

        if ((ch >= 'a' and ch <= 'z') or
                (ch >= 'A' and ch <= 'Z')):

            # To handle upper case letters
            
            ch = ch.lower()

            if (ch == 'a' or ch == 'e' or ch == 'i'
                    or ch == 'o' or ch == 'u'):
                vowels += 1
            else:
                consonant += 1

        elif (ch >= '0' and ch <= '9'):
            digit += 1

        elif i == " ":
            spaces += 1

        else:
            specialChar += 1

    print("Vowels:", vowels)
    print("Consonant:", consonant)
    print("Digit:", digit)
    print("spaces:", spaces)
    print("Special Character:", specialChar)
    
    # Drive function.
str = str(input('enter the string'))
countCharacterType(str)

