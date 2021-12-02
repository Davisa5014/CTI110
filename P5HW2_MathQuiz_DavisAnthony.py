# CTI - 110
# P5HW2 - MathQuiz
# Anthony Davis
# 28 Nov 2021

# Write a program that gives simple math quizzes.
# The program should display two random numbers.
# Program should allow user to enter numbers for addition and subraction.
# Program should congratulate user if correct, display right answer if wrong.
# Program should be menu driven, and exit only when option to exit is chosen.



import random # Importing the ability to generate random numbers.

def adding():  # Addition Function
    value = random.randint(1, 99)
    print ('\t ', value)
    value2 = random.randint(1, 99)
    print ('\t+', value2)
    answer = value + value2
    userAnswer = int(input("Enter answer: "))
    print ()
    if userAnswer == answer:
        print ("Congratulations!! You got it right!")
    else:
        print ("Sorry,", answer, "is the correct answer.")
    print ()


def subtracting(): # Subraction Function
    subValue = random.randint(1, 99)
    print ('\t ', subValue)
    subValue2 = random.randint(1, 99)
    print ('\t-', subValue2)
    subAnswer = subValue - subValue2
    subUserAnswer = int(input("Enter answer: "))
    print ()
    if subUserAnswer == subAnswer:
        print ("Congratulations!! You got it right!")
    else:
        print ("Sorry,", subAnswer, "is the correct answer.")
    print()

# The Menu
def main():
    print ("Welcome to Math Quiz")
    print ()

    # declare variables
    repeat = True
    selection = 0

    while repeat == True:
        #print the menu, ask the user to make a choice.
        print ("Main Menu:")
        print ()
        print ("*" * 20)
        print ("1. Adding Random Numbers")
        print ("2. Subracting Random Numbers")
        print ("3. Exit")
        print ("*" * 20)
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
            adding() 
        if selection == 2:
            subtracting()
        if selection == 3:
            print ("Thanks for playing Math Quiz!")
            repeat = False # next time through, we won't loop
        # else: # anything else ---- Commented out due to exception handling.
            # print (selection, "is not a valid choice. Please try again.")
            

    # end ofo while loop
    print ("Goodbye.")



# program starts here
main ()

