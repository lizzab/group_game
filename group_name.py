# Ben Lizza and Joe Degere
# 10/30/19

import random

# i made if statement and added some print statements to roll


def roll():
    die = random.randint(1,6)
    print("""If the dice rolls an even number you hit your shot.
    If the dice rolls an odd number you miss the shot and face the consequences!""")
    input("Enter: ")
    print(f"You rolled a {die}")
    if die == 1 or 3 or 5:
        print("You missed your shot and you died!")
    else:
        print("You hit your shot!")


print("Welcome to the B.J. Experience! The adventure game!")


def main_menu():
    print("You will pick what character to play as: ")
    character = input("ENTER B for Ben or ENTER J for Joe: ")
    if character == "B" or character == "b":
        print("You selected Ben. Your adventure will now begin!")
    elif character == "J" or character == "j":
        print("You selected Joe. Your adventure will now begin!")


main_menu()


def fork():
    print("You walk into a fork in the road. Pick which direction to walk.")


fork()


def first_action():
    print("If you type 1.) You will go to the right of the fork")
    print("If you type 2.) You will go the left of the fork")
    print("ENTER: ")
    choice = int(input())
    if choice == 1:
        print("You walk down the right fork about a quarter of a mile when you see a mysterious man headed your way.")
    elif choice == 2:
        print("You walk to the left fork and all you see is forrest for miles, until you hear a river flow.")


first_action()

# I got rid of the while function and combined the if statements


def second_action():
    print("1.) Do you yell to the man to grab his attention or 2.) Do you run off into the woods to hide?")
    print("ENTER: ")
    choice2 = int(input())
    if choice2 == 1:
        print("""You get the mans attention and he waves to you and walks a little faster than he was before.
    He says that he needs help in his cabin in the woods, there is a bear near the cabin and his son is stuck in there.""")
        print("1.) Do you help the man or 2.) Do you walk away?")
    else:
        print("""You run off as quickly as you can into thick brush, you watch the man pass bye he seems frantic. 
        You here leaves and brush moving behind you. You turn around and it's a bear.""")
        print("The bear kills you with one clean swat of its giant claw.")
        print("Game Over!")
    choice3 = int(input())
    if choice3 == 1:
        print("You follow the man into the woods where you both spot the bear.")
        print("You aim in your rifle and take a shot")
        print("")
        roll()
    elif choice3 == 2:
        print("You walk away from the man into a bear trap on the side of the road. The man comes running to you and u pull out your rifle in a panic.")
        print("You aim at the man telling him to stop and...")
        roll()



second_action()
