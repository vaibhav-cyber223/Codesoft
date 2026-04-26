# Password generator

import random
import string

length = int(input("The length of the password :"))

character = string.ascii_letters
digit = string.digits
symbol = string.punctuation

Total = character+ digit + symbol

password = ""

for i in range(length):
    password = password + random.choice(Total)

print("The password  is :",password)