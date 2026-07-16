import random

print("\n======-NUMBER GUESSING GAME-======")

n = random.randint(1,100)
a = -1
guess = 0
print("GUESS BETWEEN 1 TO 100")

while a != n:
    guess += 1
    a = int(input("GUESS THE NUMBER : "))
    if a < n:
        print("HIGHER NUMBER PLEASE")
    else:
        print("LOWER NUMBER PLEASE")

print(f"YOU GUESS THE CORRECT NUMBER {n} IN {guess} ATTEMPTS")

    
