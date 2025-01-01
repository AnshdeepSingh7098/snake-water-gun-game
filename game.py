import random
computer=random.choice(["s","w","g"])
you = input("enter your choice: s for snake, w for water, g for gun : ")
dict1 = {"s": "snake", "w": "water", "g": "gun"}

if you not in dict1:
    print("Invalid choice, please select 's', 'w', or 'g'")
    exit()

print(f"computer chose {dict1[computer]}\n you chose {dict1[you]}")

if computer==you:
    print("tie")
else:
    if computer == 's':
        if you == 'w':
            print("you loose")
        elif you == 'g':
            print("you win")
    elif computer == 'w':
        if you == 's':
            print("you win")
        elif you == 'g':
            print("you loose")
    elif computer == 'g':
        if you == 's':
            print('you loose')
        elif you == 'w':
            print("you win")
    else:
        print("something went wrong")
