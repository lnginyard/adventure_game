import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(item, option):
    print_pause("You find yourself standing🚶‍♂️ in an dark alley🛤🌑, filled "
                "with graffitti,rats and trash.\n")
    print_pause("Rumor has it that a " + option + " is somewhere around "
                "here, and has been terrifying the streets at night.\n")
    print_pause("In front of you is an abandoned cave.\n")
    print_pause("To your right is a dark pathway to the busy street.\n")
    print_pause("In your pocket you have your good ole handy-dandy pocket"
                "knife and in your backpack there is your stun-gun, all for"
                "your protection.\n")


def cave(item, option):
    if "knife" in item:
        print_pause("\nYou peer cautiously into the cave.⛩🕋")
        print_pause("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an cave🛖"
                    " now.")
        print_pause("\nYou walk back to the alley.🛤🚶‍♂️\n")
    else:
        print_pause("\nYou peer cautiously into the 🏚house🏚.")
        print_pause("\nIt turns out to be only a very narrow 🏚house🏚.")
        print_pause("\nYour eye👀 catches a glint of 🪙metal🖱 behind a "
                    "rock.🪦")
        print_pause("\n🔨⚡️You have found the deadly hammer of Ragnorak⛏⚡️!")
        print_pause("\nYou discard 🗑your silly little pocket knife and take "
                    "the hammer with you.")
        print_pause("\nYou walk back out to the alley.\n")
        item.append("knife")
    alley(item, option)


def empty_house(item, option):
    print_pause("\nYou approach the entrance of the cave.")
    print_pause("\nYou are about to run when a door "
                "opens and out steps a " + option + ".")
    print_pause("\nEep! This is the " + option + "'s turf!")
    print_pause("\nThe " + option + " attacks you!\n")
    if "knife" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny pocket_knife.\n")
    while True:
        choice2 = input("Would you like to (1️⃣)👊❌fight or (2️⃣)🏃🏃"
                        "run away?")
        if choice2 == "1":
            if "knife" in item:
                print_pause("\nAs the " + option + " moves to attack, "
                            "you unsheath your new weapon.")
                print_pause("\nThe Hammer of Ragnorak shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("\nBut the " + option + "takes one look at "
                            "your deadly new toy and runs away!")
                print_pause("\nYou have rid the town of the " + option +
                            ". You are victorious!🏆\n")
            else:
                print_pause("\nYou do your best...🤺")
                print_pause("but your knife🔪 is no match for the "
                            + option + ".")
                print_pause("\nYou have been defeated!😵💀🚨\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou 🏃‍♂️🏃‍♂️💨run back into the alley.🛤"
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
           alley(item, option)
            break


def alley(item, option):
    print_pause("Enter 1️⃣ to knock on the door of the empty cave.")
    print_pause("Enter 2️⃣ to peer into the house.")
    print_pause("What would you like to do")
    while True:
        choice1 = input("(🙏🏾Please enter 🔘1️⃣ or 🔘2️⃣.)\n")
        if choice1 == "1":
            cave(item, option)
            break
        elif choice1 == "2":
            house(item, option)
            break


def play_again():
    again = input("Would you like to play again❔❓💁‍♀️ 💁‍♂️(y/n)").lower()
    if again == "y":
        print_pause("\n\n\n👍Excellent❗️❕ 🔄Restarting the game🔂...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\n🫡Thanks for playing! See you next time.👋✌️🤝🫱🏾‍🫲🏻🫱🏾‍🫲🏼\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice
    (["🧙‍♀️Wicked-Witch🧙‍♀️", "🥷Ninja🥷", "🐺Vicious-Werewolf"🐺, "🧝Sorceror🧝", "🧛🏻‍♂️Vampire🧛🏻‍♂️"])
    alley(item, option)

play_game()
