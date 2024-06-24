def endOfJob():
    print("End of Job")

def isName(name):
    try:
         name = float(name)
    except ValueError:
         return name
    else: 
        name = input("You have only entered a number. Please enter an alphanumerical name to continue: ")
        name = isName(name)
        return name

def isNumber(quantity): 
    try:
        quantity = int(quantity)
    except ValueError:
            try: 
                quantity =  float(quantity)
            except ValueError: 
                quantity = input(f"{quantity} is not a number. Please enter a number to continue. : ")
                quantity = isNumber(quantity)
            return quantity
    else:
            return quantity

def detailLoop(name):
    quantity = input("Enter the quantity of the product: ")
    quantity = isNumber(quantity)
    pricePer = 2.0
    total = quantity * pricePer
    print(f'The price of {quantity}, "{name}" is ${total:.2f}.')


def housekeeping():
    fallOut = "XXX"
    name = ""
    while name.upper() != fallOut:
        name = input('Enter the name of the product or enter "XXX" to quit: ')
        name = isName(name)
        if name.upper() == fallOut:
             break
        else:
            detailLoop(name)


housekeeping()
endOfJob()