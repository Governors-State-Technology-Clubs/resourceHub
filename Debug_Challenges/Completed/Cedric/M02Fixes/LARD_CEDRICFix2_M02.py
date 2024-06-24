def endOfJob():
    print("End of program") 

def isValid(score): 
    values = []  
    try:
        score = float(score)
    except ValueError:  
            score = input(f"{score} is not a number. Please enter a positive number for the test to continue\nOr a negative number to exit.: ")
            values = isValid(score)
            return values
    else:
        if score >= 0:
            values.append(True)
            values.append(score)
            return values
        else:
            values.append(False)
            values.append(score)
            return values

def mainLoop(test1, test2, test3):
    average = (test1 + test2 + test3)/3
    print("Average is: " , average)

def housekeeping():
    score = False
    average = False
    test1 = False
    test2 = False
    test3 = False
    beenHere1 = False
    beenHere2 = False
    beenHere3 = False
    validInput = []
    while average == False:
        if test1 == False:
            score = input("Enter three test scores one at a time to calculate their average or a negative number to exit: ")
            validInput = isValid(score)
            score = validInput[1]
            if True == validInput[0]:
                test1 = score   
            else:
                average = True
        elif test2 == False:
            score = input("Enter a test score for test 2: ")
            validInput = isValid(score)
            score = validInput[1]
            if True == validInput[0]:
                test2 = score
            else: 
                average = True
        elif test3 == False: 
            score = input("Enter a test score for test 3: ")
            validInput = isValid(score)
            score = validInput[1]
            if True == validInput[0]:
                test3 = score
            else:
                average = True
            average = True   
    if score >= 0:   
        mainLoop(test1, test2, test3)
    while score >= 0: 
        if beenHere1 == False:
            score = input("Enter a new test score for test 1\nOr enter a negative number to exit: ")
            validInput = isValid(score)
            score = validInput[1]
            if  True == validInput[0]:
                test1 = score 
                beenHere1 = True
        elif beenHere2 == False:
            score = input("Enter a new test score for test 2: ")
            validInput= isValid(score)
            score = validInput[1]
            if  True == validInput[0]:
                test2 = score
            beenHere2 = True
        elif beenHere3 == False:
            score = input("Enter a new test score for test 3: ")
            validInput = isValid(score)
            score = validInput[1]
            if True == validInput[0]:
                test3 = score
            beenHere3 = True
        else:
            mainLoop(test1, test2, test3)   
            beenHere1 = False
            beenHere2 = False
            beenHere3 = False

housekeeping()
endOfJob()