import string
import random

# Character Sets
letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation

# Characters that can sometimes be confusing
confusing_characters = "O0l1I"

# Display Menu
print("=" * 50)
print("        🔐 PASSWORD GENERATOR")
print("=" * 50)

# Password length
while True:
    try:
        length = int(input("\nEnter password length: "))

        if length < 4:
            print("Password length should be at least 4.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")


print("""
Choose character types:

1. Letters
2. Digits
3. Special characters
""")

# Take all choices at once
while True:

    choices = input("Enter your choices separated by spaces (e.g. 1 2 3): ").split()

    if all(choice in ["1", "2", "3"] for choice in choices) and choices:
        break

    print("Invalid choice! Please enter only 1, 2 or 3.")


# Remove duplicate choices
choices = list(set(choices))

# Create Character Pool
character_pool = ""

if "1" in choices:
    character_pool += letters

if "2" in choices:
    character_pool += digits

if "3" in choices:
    character_pool += special_characters

# Generate Password
def generate_password(length):

    password = []

    # Guarantee at least one character
    # from every selected category

    if "1" in choices:
        password.append(random.choice(letters))

    if "2" in choices:
        password.append(random.choice(digits))

    if "3" in choices:
        password.append(random.choice(special_characters))

    # Fill remaining positions
    while len(password) < length:
        password.append(random.choice(character_pool))

    # Shuffle password so guaranteed characters
    # are not always at the beginning
    random.shuffle(password)

    return "".join(password)

# Number of Passwords
while True:
    try:
        number = int(input("\nHow many passwords do you want? "))

        if number > 0:
            break

        print("Enter a number greater than 0.")

    except ValueError:
        print("Please enter a valid number.")

# Generate Passwords
print("\n" + "=" * 50)
print("Generated Passwords")
print("=" * 50)

for i in range(number):

    password = generate_password(length)

    print(f"{i + 1}. {password}")


print("\n" + "=" * 50)
print("Password generation completed!")
print("=" * 50)

