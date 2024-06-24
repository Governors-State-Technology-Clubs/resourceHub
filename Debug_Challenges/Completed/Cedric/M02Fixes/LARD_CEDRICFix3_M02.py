# // This pseudocode segment is intended to compute and display
# // the cost of home ownership for any number of users
# // The program ends when a user enters 0 for the mortgage payment
# start
#    Declarations
#       num mortgagePayment
#       num utilities
#       num taxes
#       num upkeep
#       num total
#    startup()
#    while mortgagePayment not equal to 0
#       MainLoop()
#    endwhile
#    finishUp()
# stop

# startUp()
#    output "Enter your mortgage payment or 0 to quit"
#    input mtgPayment
# return

# mainLoop()
#    output "Enter utilities"
#    input utilities
#    output "Enter taxes"
#    input taxes
#    output "Enter amount for upkeep"
#    input upkeep
#    total = mortgagePayment + utilities + taxes + upkeep
#    output "Total is ", total
# return

# finishUp()
#    output "End of program"
# return

def MainLoop(mortgagePayment, taxes, utilities, upkeep):
    total = mortgagePayment + utilities + taxes + upkeep
    print(f"The total monthly payment is ${total}")

def isValid(control):
    values = []   
    try:
        control = float(control)
    except ValueError:
            score = input(f"{control} is not a number. Please enter a  to continue a number to continue\nOr a zero to exit.: ")
            values = isValid(control)
            return values
    else:
        if control == 0:
            values.append(False)
            values.append(control)
            return values
        else:
            values.append(True)
            values.append(control)
            return values
        
def finishUp():
    print("End of program.")

def startUp():
    control = False
    mortgagePayment = False
    utilities = False
    taxes = False
    upkeep = False
    values = []

    while mortgagePayment == False or mortgagePayment!= 0:
        control = input("Enter your mortgage payment or 0 to quit: ")
        values = isValid(control)
        mortgagePayment = values[1]
        if values[0] == False:
            break
        control = input("Enter your monthly utilities expense: ")
        values = isValid(control)
        utilities = values[1]
        control = input("Enter your monthly tax expense: ")
        values = isValid(control)
        taxes = values[1]
        control = input("Enter your monthly upkeep expense: ")
        values = isValid(control)
        upkeep = values[1]
        MainLoop(mortgagePayment, taxes, utilities, upkeep)






startUp()
finishUp()