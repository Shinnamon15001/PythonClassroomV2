import random
print("What is my magic number (1 to 100) ?")
myNumber = random.randint(1, 100)
ntries = 1
yourGuess = -1
while (ntries < 7) and (yourGuess != myNumber):
    msg = str(ntries) + ">>"
    
    if(ntries == 6):
        print("This is last round to Guess")
        
    yourGuess = int(input(msg))
    
    if yourGuess > myNumber:
        print("--> Too high")
        
    if yourGuess < myNumber:
        print("--> Too low")
        
    ntries = ntries + 1

if yourGuess == myNumber:
    print("Yes! It's", myNumber)
else:
    print("Sorry my Number is", myNumber)