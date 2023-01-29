#   Introduction | Welcome greeting and initial instructions
print()
print("** Welcome to the unofficial IB Diploma points calculator **")
print("** To start off please enter your Block 1 grade (Typically an integer from 1 to 7) **")
print()

#   Blockgrade definition | As you can see under "Main subject definition" block grade will be prompted several times. To delay our carpal tunnel syndrome we'll define a function here to call on repeatedly instead
def blockgrade(BlockNum):
    grade = 0  
    while grade<1 or 7<grade:
        grade = int(input(f"Block {BlockNum} grade: "))
        if grade<1 or 7<grade:
            print("You have inputted an invalid grade. Please try a value from 1 to 7.")
            print()
    return grade

def thedoor():
    input("Press any key to exit")
    exit()

#   Finalgrade definition | A function for the final greade is being defined for later use. All Block grades are summed up, then the ExtraGrade (derived from the CoreGrade) is added.
#   The final score is then outputted, and the user is prompted to exit.
def finalgrade():
    BlockGrade = Nor + Eng + Soc + Sci + Mat + Che
    FinalGrade = BlockGrade + int(ExtraGrade)
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

def coreoopsie():
    print("It appears you have entered an invalid grade for your core subjects. Please Try another value. Hint: Core subject grades usually range from A to E.")

#   Main subject definition | Grade variables are defined here through user inputs, and variable type is specified as an integer to avoid errors.
#   Note to self: Add input check to ensure user isn't inputting a string or invalid grade, if check fails return a message to user
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
#   The core grades are combined into a single string so as to easily compare it to the table bellow
CoreCombo = (TOK + EE)

#   Letter combinations are assigned a score variable which will later be converted into a point score
ThreePointers = ["AA", "AB", "BA"]
TwoPointers = ["CA", "DA", "AC", "AD", "BB"]
OnePointers = ["DB", "CC", "BD"]
ZeroPointer = ["DC", "DD", "CD"]
Fail = ["EE"]

#   Aforementioned combination variables will now be tested, and recieve a suitable score
if CoreCombo in ThreePointers:
    ExtraGrade = 3
    finalgrade()
elif CoreCombo in TwoPointers:
    ExtraGrade = 2
    finalgrade()
elif CoreCombo in OnePointers:
    ExtraGrade = 1
    finalgrade()
elif CoreCombo in ZeroPointer:
    ExtraGrade = 0
    finalgrade()
elif CoreCombo in Fail:
    print("It appears you have failed one or multiple of your core subjects, unfortunately a diploma score cannot be awarded")
    thedoor()
