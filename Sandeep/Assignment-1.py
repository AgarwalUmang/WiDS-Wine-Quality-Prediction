# 2) Mastermind
import random
def generator():
    for i in range(1):
        yield random.randint(1000,9999)
random.seed(2)
for randomnumber in generator():
    random_number=list(str(randomnumber))
ran=[int(i) for i in random_number]
def guess():
    guesses=list(str(input("enter your guess: - ")))
    return guesses

def mastermind():
    i=0
    while i<10:
        result=""
        num=[int(i) for i in guess()]
        if len(num) !=4:
            print("Please enter only 4 digit number.")
            continue
        if ran==num:
            print("Congrats.")
    
        for digits in num:
            if digits in ran:
                if num.index(digits)==ran.index(digits):
                    result+="R"
                else:
                    result+="Y"
            else:
                result+="B"
        print(result)
        i+=1
    else:
        print("Game over!",num)
mastermind()
        
    
