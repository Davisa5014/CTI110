# CTI - 110
# P5HW1 - Lists and Functions
# Anthony Davis
# 18 Nov 2021

"""
Program has two parts:
makeList() - builid a list from user entered values
displayList() - take a list, display each item
TODO: Maybe add input validation
"""

def getNumber():
    """
    input: none
    output: an int
    """

    goodInput = False # repeat until we get good input
    while goodInput == False:
        try:
            num = int(input("Enter a number: "))
            goodInput = True
        except ValueError:
            print ("This is not a valid int... please try again.")
    return num


def makeListOfSize(size):
    """
    Makes a list from user entered numbers
    input: none
    returns: a list
    """
    newList = []
    for i in range(size): # repeats size times
        # num = int(input("Enter a number: "))
        num = getNumber()
        newList.append(num)
    return newList


def displayList(items):
    """
    Display a list of items.
    input: a list
    returns: none
    """
    for item in items:
        print(item, end=" ")
    print ()

def removeDupes(items):
    """
    Take a list and remove duplicates (using set)
    input: a list
    returns: a list without duplicate entries
    """
    mySet = set(items)
    noDupeList = list(mySet)

    return noDupeList


def getMinandMaxOf(numbers):
    """
    input: a list
    returns: two numbers, the min and max values in list
    """
    minNum = min(numbers)
    maxNum = max(numbers)
    return minNum, maxNum

def getTotalAndAverage(numbers):
    """
    input: a list
    returns: two numbers, total and average of all values
    """
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return total, average


def makeList():
    # print ("Making a list...")
    # size = int(input("How many items in the list? "))
    print ("Please enter 10 numbers.")
    size = 10
    numbers = makeListOfSize(size)


def showList(newList):
    print ("Displaying list...")
    displayList(numbers)
    print ("Removing duplicates...")
    numbersNoDupes = removeDupes(numbers)
    displayList(numbersNoDupes)
    # multiple variable return
    minNum, maxNum = getMinandMaxOf(numbers)
    print("Smallest =", minNum, "Largest =", maxNum)
    
    total, average = getTotalAndAverage(numbers)
    print("Total =", total, "Average =", average)
    print("Done.")

 


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
        print ("1. Create List")
        print ("2. Display Results")
        print ("3. Exit")
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
            makeList()
        if selection == 2:
            showList()
        if selection == 3:
            print ("Exiting...")
            repeat = False # next time through, we won't loop
        # else: # anything else ---- Commented out due to exception handling.
            # print (selection, "is not a valid choice. Please try again.")
            

    # end ofo while loop
    print ("Goodbye.")


#start
main()
