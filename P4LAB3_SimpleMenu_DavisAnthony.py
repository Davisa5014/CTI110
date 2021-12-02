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






def main():
    print ("Simple Menu")
    print ()

    # declare variables
    repeat = True
    selection = 0

    while repeat == True:
        #print the menu, ask the user to make a choice.
        print ("Menu:")
        print ()
        print ("*" * 12)
        print ("1. Option 1")
        print ("2. Option 2")
        print ("3. Option 3")
        print ("4. Quit")
        print ("*" * 12)
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
        if selection == 2:
            print ("You chose option", selection) # for testing
        if selection == 3:
            print ("You chose option", selection) # for testing
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
