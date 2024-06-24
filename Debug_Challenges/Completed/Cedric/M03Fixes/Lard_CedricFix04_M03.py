def endOfJob():
     print("End of program")

def isValidNumber(control): 
    try:
        control = float(control)
    except ValueError:  
            control = input(f"{control} is not a number. Please enter a number to continue.: ")
            control = isValidNumber(control)
            return control
    else:
            return control

def mainLoop(miles, gallons):
    mpg = miles/gallons
    print(f"miles per gallon is {mpg}.")
    return miles

def housekeeping():
    endVal = 0
    control = None
    miles = 1  
    gallons = None
    while miles > endVal:
        control = input("How many miles did you drive? Enter 0 to quit: ")
        miles = isValidNumber(control)
        if miles == None or miles > 0:
            control = input("How many gallons have you used: ")
            gallons = isValidNumber(control)
            mainLoop(miles, gallons)
housekeeping()
endOfJob()