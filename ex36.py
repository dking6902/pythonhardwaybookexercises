from sys import exit

def final_room():
    print("Welcome to the final room")
    print("Here you will make a choice")
    print("On the table infront of you are five goblets")
    print("You must choose one and drink from it.")
    print("1 goblet will leave you victorious.")
    print("1 will kill you")
    print("1 will take you to the very beginning")
    print("The other 2 will take you to either the Sphinx room or Tiger room")
    print("The choice is yours")
    print("Which goblet will you choose? 1, 2, 3, 4 or 5")

    goblet_choice = input("> ")

    if goblet_choice == "1":
        tiger_room()
    if goblet_choice == "2":
        dead()
    if goblet_choice == "3":
        print("You win")
        exit(0)
    if goblet_choice == "4":
        start()
    if goblet_choice == "5":
        sphinx_room()




def sphinx_room():
    print("Here you are greeted by a Sphinx.")
    print("To go through this room \nYou must solve a riddle.")
    proceed = input("Would you like to hear the riddle? yes or no: ")
    if "no" in proceed:
        print("You will regret that choice as I am now going to eat you.")
        dead()
    if "yes" in proceed:
        print("What has a face and two hands but no arms and legs?")
        answer = input("> ")
        if answer == "a clock" or answer == "clock":
            print("That is correct, you may proceed")
            print("The door creaks open and you enter a new room")
            final_room()
        if answer != "a clock" or answer != "clock":
            dead()
    if proceed != "yes" or "no":
        sphinx_room()
def tiger_room():
    print("There is a tiger prowling the room")
    print("It will only move if you answer a maths sum")
    print("What is 8 + 7?")
    tiger_moved = False

    while True:
        answer = input("> ")
        if answer == "15" and not tiger_moved:
            tiger_moved = True
            print("That is correct you may open the door.")
        elif answer != "15" and not tiger_moved:
            print("That is wrong, the tiger pounces on you")
            dead()
        elif answer == "open door" or answer == "open" and tiger_moved:
            final_room()

def dead():
    print("Game Over!")
    exit(0)

def start():
    print("Welcome to the Haunted House")
    print("You see two doors in front of you?")
    print("Do you take the left or right door?")
    choice = ("")
    choice = input("> ")

    if choice == "left":
        sphinx_room()
    if choice == "right":
        tiger_room()
    else:
        print("You made the wrong or no choice so you are going to die!")
        dead()

start()
