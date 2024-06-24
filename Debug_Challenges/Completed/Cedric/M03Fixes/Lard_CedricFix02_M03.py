# // This pseudocode is intended to display employee net pay values.
# // All employees have a standard $45 deduction from their checks.
# // If an employee does not earn enough to cover the deduction
# // an error message is displayed.
# start
#    Declarations
#       string name
#       num hours
#       num rate
#       string DEDUCTION = 45
#       string EOFNAME = "ZZZ"
#       num gross
#       num net
#    output "Enter first name or ", EOFNAME, " to quit"
#    input name
#    if name not equal to EOFNAME
#       output "Enter hours worked for ", name
#       input hours
#       output "Enter hourly rate for ", name
#       input rate
#       gross = hours * rate
#       net = gross - DEDUCTION
#       while net > 0 then
#          output "Net pay for ", name, " is ", net
#       else
#           output "Deductions not covered. Net is 0."
#       endwhile
#       output "Enter next name or ", EOFNAME, " to quit"
#       input name
#    endif
#    output "End of job"
# stop

name = ""
hours = 0
rate = 0
deduction = 45
eofName = "ZZZ"
gross = 0
net = 0
control = None

def isValid(control): 
    try:
        control = float(control)
    except ValueError:  
            control = input(f"{control} is not a number. Please enter a positive number for the test to continue\nOr a negative number to exit.: ")
            control = isValid(control)
            return control
    else:
            return control
    
name = input(f"Enter first name or {eofName} to quit.: ")
while name.upper() != eofName:
    control = input("Enter hours worked for: ")
    hours = isValid(control)
    control = input(f"Enter hourly rate for {name}: $")
    rate = isValid(control)
    gross = hours * rate
    net = gross - deduction
    if net >= 0:
        print(f"Net pay for {name} is {net}")
        name = input(f"Enter next name to continue or {eofName} to exit: ")
    else:
         print(f"Deductions not covered. Net is less than 0")
         name = input(f"Enter next name to continue or {eofName} to exit: ")