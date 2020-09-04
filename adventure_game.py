import time
import random


def print_pause(msg, sec):
    time.sleep(sec)
    print(msg)


def fight(items):
    print_pause("1.fight 2.run-away", 1)
    choice = input()
    if choice == "1" and "2" in items:
        print_pause("you won", 1)
        play_again(items)
    elif choice == "2":
        print_pause("you are out in the field again", 1)
        print_pause("figure out what to do again", 1)
        game_start(items)
    elif choice == "1" and "2" not in items:
        print_pause("you lost", 1)
        play_again(items)
    else:
        fight(items)


def play_again(items):
    print_pause("would you like to play this"
                " game again or not?(y/n)", 1)
    choice = input().lower()
    if choice == "y":
        items.clear()
        intro()
        game_start(items)
    elif choice == "n":
        print_pause("Goodbye", 1)
    else:
        play_again(items)


def intro():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.", 2)
    print_pause("Rumor has it that a wicked fairie is somewhere"
                " around here, and has been terrifying the nearby village.", 2)
    print_pause("find it and kill it", 2)
    print_pause("let's go", 2)


def game_start(items):
    print_pause("\nEnter 1 to knock on the door of the house. ", 1)
    print_pause("Enter 2 to peer into the cave. ", 1)
    print_pause("What would you like to do?", 1)
    while True:
        print_pause("(Please enter 1 or 2).", 1)
        choice = input()
        if choice == "1":
            choice_one(items)
            break
        elif choice == "2":
            choice_two(items)
            break


def choice_one(items):
    print_pause("Entered the house", 1)
    if "2" in items:
        print_pause("you are ready for battle", 1)
        fight(items)
    else:
        print_pause("you are not ready for battle", 1)
        fight(items)


def select_weapon(weapons, items):
    weapon = random.choice(weapons)
    print_pause(f"you found a {weapon}", 1)
    while True:
        print_pause(f"Would you like to collect the {weapon}?"
                    "(\"y\" or \"n\")", 1)
        answer = input().lower()
        if answer == "y":
            items.append("2")
            print_pause(f"you collected the {weapon}", 1)
            print_pause("go back to the field", 1)
            print_pause("you are out in the field again", 1)
            print_pause("figure out what to do again", 1)
            break
        elif answer == "n":
            print_pause("you have no weapon to fight with, good luck!!", 1)
            print_pause("go back to the field", 1)
            print_pause("you are out in the field again", 1)
            print_pause("figure out what to do again", 1)
            break
        else:
            print_pause("you have entered a invalid input", 1)
    game_start(items)


def choice_two(items):
    weapons = ["gun", "sword", "knife"]
    print_pause("Entered the cave", 1)
    if "2" in items:
        print_pause("you have been here before", 1)
        print_pause("go back to the field", 1)
        print_pause("you are out in the field again", 1)
        print_pause("figure out what to do again", 1)
        game_start(items)
    else:
        select_weapon(weapons, items)


def play_game():
    items = []
    intro()
    game_start(items)


if __name__ == "__main__":
    play_game()
