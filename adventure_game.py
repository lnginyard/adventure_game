import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


print_pause("Rumor👂 has it that a wicked fairie🧟‍♀️ is somewhere around here, and has been terrifying😱 the nearby village...😟")
print_pause("🛑Stop Enter 1️⃣ to knock on the door of the house or Enter  2️⃣ to peer into the cave.")
print_pause("What would you like to do? 💁‍♀️")
user_choice = int(input("Please enter  1  or 2:"))
while True:
    user_choice = input("Please enter 1 or 2:")
    if user_choice == "1":
        name = True
        print("You've chosen to knock on the door")
    elif user_choice == "2":
        name = True
        print("You've chosen to peer into the cave")
        break
    else:
        print("\n❌That was not an option🚫  Please try again...🔘Select 1️⃣🤏 or 2️⃣🤏:\n")
    

   # else:
   #     user_choice == "2"
   #     print("You've chose to peer into the cave!")
   #     if user_choice != 2:
   #         user_choice = int(input("❌That was not an option🚫  Please try again...🔘Select 1️⃣🤏 or 2️⃣🤏"))
   #         user_choice()
if user_choice == "1":
    print_pause("You knock on the door and all of a sudden it opens as you knock as if someone left the door open.")
    print_pause("You walk slowly and enter into a dark hallway and shouts 'is anyone home?'")
    
        #break
