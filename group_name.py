# Ben Lizza and Joe Degere
# 10/30/19

import random

print("Welcome to the B.J. Experience! The adventure game!")


def main_menu:
    print("You will pick what character to play as: ")
    print("ENTER B for Ben or ENTER J for Joe: ")
    input()
    if input() == "B" or "b":
        print("You selected Ben. Your adventure will now begin!")
    elif input() == "J" or "j":
        print("You selected Joe. Your adventure will now begin!")


main_menu()

print("You walk into a fork in the road. Pick which direction to walk.")


def first_action:
    print("If you type 1.) You will go to the right of the fork")
    print("If you type 2.) You will go the left of the fork")
    int(input())
    if int(input()) == 1:
        print("You walk down the right fork about a quarter of a mile when you see a mysterious man headed your way.")
    elif int(input()) == 2:
        print("You walk to the left fork and all you see is forrest for miles, until you hear a river flow.")


first_action()


while first_action() == 1:
    print("1.) Do you yell to the man to grab his attention or 2.) Do you run off into the woods to hide?")
    int(input())
    if int(input()) == 1:
        print("""You get the mans attention and he waves to you and walks a little faster than he was before.
            He says that he needs help in his cabin in the woods, there is a bear near the cabin and his on is stuck in there.""")
        print("1.) Do you help the man or 2.) Do you walk away?")
        int(input())
    elif int(input()) == 1:
        print("You follow him about a mile or two into the woods and u stumble upon the bear and the cabin. He says he has a rifle and a shotgun in the shed outside the cabin.")



