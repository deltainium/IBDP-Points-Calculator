#   Introduction | Welcome greeting and initial instructions
print()
print("** Welcome to the unofficial IB Diploma points calculator **")
print("** To start off please enter your Block 1 grade (Typically an integer from 1 to 7) **")
print()

#   Blockgrade definition | As you can see under "Main subject definition" block grade will be prompted several times. To delay our carpal tunnel syndrome we'll define a function here to call on repeatedly instead
def blockgrade(BlockNum):
    grade = 0  
    while grade<1 or 7<grade:
        try:
            grade = int(input(f"Block {BlockNum} grade: "))
            if grade<1 or 7<grade:
                print("You have inputted an invalid grade. Please try a value from 1 to 7.")
                print()
        except ValueError:
            print("You have inputted an invalid grade. Please try a value from 1 to 7.")
            print()
    return grade

# thedoor definition | A way to automate a user friendly way of exiting the program
def thedoor():
    input("Press any key to exit")
    exit()

# coreoopsie definition | Convenient automation of the error message displayed when an invalid grade is entered into core grades.
def coreoopsie():
    print("You have entered an invalid grade. Please try a value from A to E.")

#   Main subject definition | Grade variables are defined here through user inputs, and variable type is specified as an integer to avoid errors.
Nor = blockgrade(1)
Eng = blockgrade(2)
Soc = blockgrade(3) 
Sci = blockgrade(4)
Mat = blockgrade(5)
Che = blockgrade(6)

#   Core subject definition | Purpose is same as main subject definition, but due to IB shenanigan these grades are given as letters (A, B, C, etc.) 
print()
print("** Block grades accepted. Please enter your Core grades (TOK + EE). These are typically a letter from A to E) **")
print()
AccValls = ["A","B","C","D","E"]
TOK = "Z"
EE = "Z"
while TOK not in AccValls: 
    TOK = str(input("ToK grade: "))
    if TOK not in AccValls:
        coreoopsie()
while EE not in AccValls: 
    EE = str(input("Extended Essay grade: "))
    if EE not in AccValls:
        coreoopsie() 
#   CoreMix | A nested dictionary which acts as a table. The first CoreGrade is used as a key to an embedded dictionary,
#   which is then followed up with the second core grade used as a key. Both coregrades together result in an appropriate point score
CoreMix = {
        "A":{"A": 3,"B": 3,"C": 2,"D": 2,"E": 1,},
        "B":{"A": 3,"B": 2,"C": 1,"D": 1,"E": 0,},
        "C":{"A": 2,"B": 1,"C": 1,"D": 0,"E": 0,},
        "D":{"A": 2,"B": 1,"C": 0,"D": 0,"E": 0,},
        "E":{"A": 1,"B": 0,"C": 0,"D": 0,"E": -1,},
        }
CoreCombo = CoreMix[TOK][EE]

# Simple check to see if a condition for diploma failure has been met, otherwise the program continues
if CoreCombo == -1:
    print("It appears you have failed one or multiple of your core subjects, unfortunately a diploma score cannot be awarded")
    thedoor()
else:
    FinalGrade = (Nor + Eng + Soc + Sci + Mat + Che) + CoreCombo
    # Another check to see if a condition for diploma failure has been met
    if FinalGrade < 24:
        print()
        print("Unfortunately your diploma score is bellow 24 points which is considered a failing condition.")
        print("You are therefore not eligble to recieve a diploma score")
        print("If you're still curious, your diploma score would have been: ",FinalGrade)
        print()
        thedoor()
    else:
        print()
        print("----------")
        print("Your IB Diploma Score is: ", FinalGrade)
        print("----------")
        print()
        thedoor()
