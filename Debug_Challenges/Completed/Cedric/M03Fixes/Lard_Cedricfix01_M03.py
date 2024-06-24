# // This pseudocode is intended to determine whether students have
# // passed or failed a course; student needs to average 60 or
# // more on two tests. 
# start
#    Declarations
#       num firstTest
#       num secondTest
#       num average
#       num PASSING = 60
#    output "Enter first score or 0 to quit "
#    while firstTest not equal to 0
#       output "Enter second score "
#       input secondTest
#       average = firstTest + secondTest / 2
#       ouput "Average is ", average
#       if average >= PASSING then
#          output "Pass"
#       else
#          output "Fail"
#       endif
#       output "Enter first score or 0 to quit "
#    endwhile
# stop

score = None

def isValid(score): 
    try:
        score = float(score)
    except ValueError:  
            score = input(f"{score} is not a number. Please enter a positive number to continue: ")
            score = isValid(score)
            return score
    else:
            return score
    
def mainLoop(score):
   firstTest = False
   secondTest = False
   average = False
   passing = 60
   while score != 0:
      if firstTest == False:
         score = input("Enter first score or 0 to quit: ")
         score = isValid(score)
         firstTest = score
      else:
         score = input("Enter second score or 0 to quit: ")
         score = isValid(score)
         secondTest = score
         score = 0
   if secondTest != 0:
      average = (firstTest + secondTest)/2
      print("Average is: ", average)
      if average >= passing:
         print("Pass")
         score = 1
      else: 
         print("Fail")
         score = 1
   firstTest = False
   secondTest = False
 
   return score

while score != 0:
   score = mainLoop(score)