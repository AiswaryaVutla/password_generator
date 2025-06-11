import random
import string

# Get password criteria from the user
print("Hello use,welcome to the Password Generator!")

# Get the desired password length,checking whether it is valid one or not
while True:
    length_input = input("Enter the desired password length (NOTE:Minimum 6 characters): ")
    if length_input.isdigit():
        length = int(length_input)
        if length >= 6:
            break
        else:
            print("Password length must be at least 6.")
    else:
        print("Please enter a valid number.")

# Ask the user which character types to include in password
use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

# Make sure at least one character type is selected
while not (use_letters or use_numbers or use_symbols):
    print("You must include at least one type of character.")
    use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

# Step 2: Create a character pool based on user preferences
characters = ""

if use_letters:
    characters += string.ascii_letters
if use_numbers:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

# Step 3: Generate the password
password = ""
for i in range(length):
    password += random.choice(characters)

# Step 4: Show the password
print("\nHere's your generated password :")
print(password)