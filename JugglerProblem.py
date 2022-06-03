def numTest(num):
    maxNum = 0
    totalRuns = 0
    runningNum = num
    while runningNum != 1:
        if runningNum%2 == 0:
            runningNum = int(runningNum**(1/2))
        elif runningNum%2 == 1:
            runningNum = int(runningNum**(3/2))
        if runningNum > maxNum:
            maxNum = runningNum
        totalRuns += 1
        print(runningNum)
    print("Runs: " + str(totalRuns) + ", Max: " + str(maxNum))
        
def userInput():
    tempInput = int(input("Enter your test value: "))
    if tempInput == 0:
        print("Cannot compute 0!")
        userInput()
    else:
        numTest(tempInput)

userInput()