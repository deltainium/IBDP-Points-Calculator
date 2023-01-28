#   Introduction block | Welcome greeting and initial instructions
print()
print("** Welcome to the unofficial IB Diploma points calculator **")
print()
print("To start off please enter your Block 1 grade (Typically an integer from 1 to 7)")
print()

#   Variable definition block | Grade variables are defined here through user inputs, and variable type is specified as an integer to avoid errors.
#   Note to self: Add input check to ensure user isn't inputting a string or invalid grade, if check fails return a message to user
NorwegianGrade = int(input("Block 1 grade: "))
EnglishGrade = int(input("Block 2 grade: "))
SocStudiesGrade = int(input("Block 3 grade: "))
ScienceGrade = int(input("Block 4 grade: "))
MathGrade = int(input("Block 5 grade: "))
ChemGloGrade = int(input("Block 6 grade: "))

#   Purpose is same as previous block, but due to IB shenanigan these grades are given as letters (A, B, C, etc.) 
print()
print("Block grades accepted. Please enter your Core grades (TOK + EE). These are typically a letter from A to E)")
print()
TOKGrade = str(input("ToK grade: "))
EEGrade = str(input("Extended Essay grade: "))

#   The core grades are combined into a single string so as to easily compare it to an upcomming table
CoreCombo = (TOKGrade + EEGrade)

#   Letter combinations are assigned a score variable which will later be converted into a point score
ThreePointers = ["AA", "AB", "BA"]
TwoPointers = ["CA", "DA", "AC", "AD", "BB"]
OnePointers = ["DB", "CC", "BD"]
ZeroPointer = ["DC", "DD", "CD"]
Fail = ["EE"]

#   Aforementioned combination variables will now be tested, and recieve a suitable score
if CoreCombo in ThreePointers:
    ExtraGrade = 3
elif CoreCombo in TwoPointers:
    ExtraGrade = 2
elif CoreCombo in OnePointers:
    ExtraGrade = 1
elif CoreCombo in ZeroPointer:
    ExtraGrade = 0
elif CoreCombo in Fail:
    print("It appears you have failed one or multiple of your core subjects, unfortunately a diploma score cannot be awarded")
else:
    print("It appears you have entered an invalid grade for your core subjects. Please restart the program and try again. Hint: Core subject grades usually range from A to E.")

#   Block Grades are now summed up, and the ExtraGrade is added to generate a final diploma grade. The ExtraGrade is converted into an integer just for good measure so as to avoid errors.
BlockGrade = NorwegianGrade + EnglishGrade + SocStudiesGrade + ScienceGrade + MathGrade + ChemGloGrade
FinalGrade = BlockGrade + int(ExtraGrade)
print()
print("----------")
print("Your IB Diploma Score is: ", FinalGrade)
print("----------")
print()
input("Pres any key to exit")
