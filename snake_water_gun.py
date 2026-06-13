import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice: ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1: "Snake", -1: "Water", 0:"Gun"}
you = youDict[youStr]

# By now we have 2 numbers (variables), you and computer
 
print(f"You choose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if(computer == you):
    print("It's a Draw")

else:
    if(computer == -1 and you == 1):  # computer - you = -2
        print("You Win!")

    elif(computer == -1 and you == 0): # computer - you = -1
        print("You Lost!")

    elif(computer == 1 and you == -1): # computer - you = 2
        print("You Lost!")

    elif(computer == 1 and you == 0): # computer - you = 1
        print("You Win!")

    elif(computer == 0 and you == -1): # computer - you = 1
        print("You Win!")

    elif(computer == 0 and you == 1): # computer - you = -1
        print("You Loose!")

    else:
        print("Something went wrong!")


    # Shortcut Method
    # if((computer - you) == -1 or (computer - you) == 2):
    #     print("You Loose")
    # else:
    #     print("You Win")