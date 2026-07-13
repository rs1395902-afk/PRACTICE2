import string
import random

print("WELCOME TO PASSWORD GENERATOR")

length = int(input("ENTER YOUR PASSWORD LENGTH : "))

character = string.digits

password = ""
if length == 0 or length < 0:
        print("INVALID LENGTH")
else:
    for i in range(length):
        password += random.choice(character)
        print("YOUR PASSWORD IS : ", password)


 


