# Step 1: Import the modules we need
import random
import string

# Step 2: Ask the user how long the password should be
length = int(input("Enter the length of the password: "))

# Step 3: Create a pool of characters to choose from
letters = string.ascii_letters   # a-z and A-Z
digits = string.digits           # 0-9
symbols = string.punctuation     # special characters like !, @, #

characters = letters + digits + symbols

# Step 4: Make an empty password string
password = ""

# Step 5: Pick random characters one by one
for i in range(length):
    password = password + random.choice(characters)

# Step 6: Show the final password
print("Your password is:", password)
