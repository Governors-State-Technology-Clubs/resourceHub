# // This pseudocode is intended to display
# // employee net pay values. All employees have a standard
# // $45 deduction from their checks.
# // If an employee does not earn enough to cover the deduction
# // an error message is displayed.
# // This example is modularized.
# start
#    Declarations
#       string name
#       string EOFNAME = ZZZZ
#    while name not equal to EOFNAME
#       housekeeping()
#    endwhile
#    while name not equal to EOFNAME
#       mainLoop()
#    endwhile
#    while name not equal to EOFNAME
#       finish()
#    endwhile
# stop

# housekeeping()
#    output "Enter first name or ", EOFNAME, " to quit "
# return

# mainLoop()
#    Declarations
#       num hours
#       num rate
#       num DEDUCTION = 45
#       num net
#    output "Enter hours worked for ", name
#    input hours
#    output "Enter hourly rate for ", name
#    input rate
#    gross = hours * rate
#    net = gross - DEDUCTION
#    if net > 0 then
#       output "Net pay for ", name, " is ", net
#    else
#       output "Deductions not covered. Net is 0."
#    endif
#    output "Enter next name or ", EOFNAME, " to quit "
#    input name
# return

# finish()
#    output "End of job"
# return

name =""
eofName = "ZZZZ"
def finishUp():
     print("End of Job")

def isValidNumber(control): 
    try:
        control = float(control)
    except ValueError:  
            control = input(f"{control} is not a number. Please enter a number to continue.: ")
            control = isValidNumber(control)
            return control
    else:
            return control

def isValidString(name):
    isTrueString = None
    try:
        name = float(name)
    except ValueError:
        isTrueString = name.isalpha()
        if isTrueString == True:
            return name
        else: 
             name = input(f"{name} names don't contain numbers, please enter a valid name.: ")
             name = isValidString(name)
             return name
    else:
        name = input(f"{name} is a number. Please enter a new name to continue or {eofName} to exit.: ")
        name = isValidString(name)
        return name

def housekeeping(eofName):
     name = ""
     name = input(f"Enter first name or {eofName} to quit.: ")
     name = isValidString(name)
     return name

def mainLoop(name, eofName):
        deduction = 45
        control = input("Enter hours worked for: ")
        hours = isValidNumber(control)
        control = input(f"Enter hourly rate for {name}: $")
        rate = isValidNumber(control)
        gross = hours * rate
        net = gross - deduction
        if net >= 0:
            print(f"Net pay for {name} is {net}")
            name = input(f"Enter next name to continue or {eofName} to exit: ")
            return name
        else:
            print(f"Deductions not covered. Net is less than 0")
            name = input(f"Enter next name to continue or {eofName} to exit: ")
            return name

name = housekeeping(eofName)
while name.upper() != eofName:
    name= mainLoop(name, eofName)
finishUp()