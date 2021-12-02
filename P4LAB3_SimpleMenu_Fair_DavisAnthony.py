# CTI 110
# P4LAB3
# Anthony Davis
# 28 Oct 2021

# A simple menu, which can be expanded.
# For this program, we'll be making a menu with 4 or more options.
# One of the options should be "Quit".
# The program should print the menu and then ask the user to make a choice.
# If the user makes a choice other than those listed,
# they are asked to make the choice again.
# Once the user picks a menu option, print a message specific to that choice,
# and then return to the main menu.

def budgetEscape(sponsor):
    """
    This method just keeps you in a room until you leave.
    (Our budget was $0.)
    """
    print("This escape room brought to you by:", sponsor)
    # this time we loop based on user input
    leave = "no"
    while leave != "yes" and leave != "y":
        print ("You're in a room. There is a door.")
        # more description could go here
        leave = input("Will you leave (yes/no)? ")
    print("You leave. Nice job.")

def tacoTruck():
    taco = "" # add toppings later
    orderUp = False
    while (orderUp == False):
        answer = input ("Would you like a taco? (y/n)")
        if answer == "y":
            taco += "a taco."
            orderUp = True
            
        if answer == "n":
            taco += "nothing."
            orderUp = True

    print ("Here's your order of", taco)

def surprise():
    loop = False
    while loop == False:
        print ()
        fight = input ("A tiny car pulls up with 20 killer clowns in it. Do you fight? (y/n) ")
        print ()
        if fight == "y":
            weapon = input("You see a balloon sword, do you use it? (y/n) ")
            if weapon == "y":
                print ()
                print ("With a WAAAAGH! you fend off the 20 clowns with your balloon sword!")
                print ()
                print ("You gain 100 experience points! You level up! Hooray!")
                loop = True
            if weapon == "n":
                print ()
                print ("The killer clowns pull out balloon weapons and slay your soul!")
                loop = True
        if fight == "n":
            print ("You run away! Clowns are scary!")
            loop = True

    print ()
    print ("Well that was weird...")
    print ()



def main():
    print ("Faire Menu")
    print ()

    # declare variables
    repeat = True
    selection = 0

    while repeat == True:
        #print the menu, ask the user to make a choice.
        print ("Menu:")
        print ()
        print ("*" * 25)
        print ("1. Budget Escape Room")
        print ("2. Taco Truck")
        print ("3. Surprise!")
        print ("4. Quit")
        print ("*" * 25)
        print ()
        # exception handling
        try:
            selection = int(input("Choose option: "))
        except:
            print("That is not a valid choice. Please try again.")
            selection = 0 # so we don't pick the previous menu option
            
        # either pick a branch based on the selection,
        # or print error and repeat (if not from listed options)
        if selection == 1:
            print ("You chose option", selection) # for testing
            budgetEscape("Raid Shadow Legends")
        if selection == 2:
            print ("You chose option", selection) # for testing
            tacoTruck()
        if selection == 3:
            print ("You chose option", selection) # for testing
            surprise()
        if selection == 4:
            print ("Exiting...")
            repeat = False # next time through, we won't loop
        # else: # anything else ---- Commented out due to exception handling.
            # print (selection, "is not a valid choice. Please try again.")
            

    # end ofo while loop
    print ("Goodbye.")



# program starts here
main ()


# the complex version (this is optional for now)
"""
if__name__ == "__main__":
    main()
"""
