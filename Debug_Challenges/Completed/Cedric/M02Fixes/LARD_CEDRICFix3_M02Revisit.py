def finishUp():
    print("End of program.")

def MainLoop(values):
    expenses = ["utilities", "taxes", "upkeep"]
    total = 0
    for cost in expenses:
        values.append(input(f"Please enter in the monthly expense of {cost}: $"))
        values = validEntry(values)
    n = len(values)
    for x in range(n):
        total += values[x]
    print(f"Total is: ${total:.2f}")

def validEntry(values):
    if 1 == len(values):
        try:
            values[0] = float(values[0])
        except ValueError:
            values[0] = input(f"{values[0]} is not a number. Please enter a  to continue a number to continue\nOr a zero to exit.: $")
            values = validEntry(values)
            return values
        else:
            return values
    else:
        num = len(values)
        try:
            values[num-1] = float(values[num-1])
        except ValueError:
            values[num-1] = input(f"{values[num-1]} is not a number. Please enter a  to continue a number to continue.: $")
            values = validEntry(values)
            return values
        else:
            return values
        
def startUp():
    values = []
    values.append(input("Enter your mortgage payment or 0 to quit.: $"))
    values = validEntry(values)
    while values[0] != 0:
        MainLoop(values)
        values .clear()
        values.append(input("Enter another mortgage payment or 0 to quit.: $"))
        values = validEntry(values)
    

startUp()
finishUp()