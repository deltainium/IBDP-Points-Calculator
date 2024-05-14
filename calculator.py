if __name__ == "__main__":
    all_grades = []

    print("\n** Welcome to the unofficial IB Diploma points calculator **")
    print("** To start off please enter your Block 1 grade (Typically an integer from 1 to 7) **\n")

    # For loop that prompts the user for all 6 core subjects
    for i in range(6):
        grade = 0  

        # Loops until valid grade is given
        while (grade < 1) or (grade > 7): 
            grade = int(input(f"Block {i+1} grade: "))
    
            # Checks if provided grade was within valid range
            if (grade < 1) or (grade > 7):
                print("You have inputted an invalid grade. Please try a value from 1 to 7.")
                print()
            else:
                all_grades.append(grade) 



    #   Core subject definition | Purpose is same as main subject definition, but due to IB shenanigan these grades are given as letters (A, B, C, etc.) 
    print("\n** Block grades accepted. Please enter your Core grades (TOK + EE). These are typically a letter from A to E) **\n")
    AccValls = ("A","B","C","D","E")
    TOK = "Z"
    EE = "Z"

    while TOK not in AccValls: 
        TOK = str(input("ToK grade: "))

        if TOK not in AccValls:
            print("You have entered an invalid grade. Please try a value from A to E.")

    while EE not in AccValls: 
        EE = str(input("Extended Essay grade: "))

        if EE not in AccValls:
            print("You have entered an invalid grade. Please try a value from A to E.")

    #   CoreMix | A nested dictionary which acts as a table. The first CoreGrade is used as a key to an embedded dictionary,
    #   which is then followed up by the second core grade used as a "nested" key. Both coregrades together result in an appropriate point score
    CoreMix = {
            "A":{"A": 3,"B": 3,"C": 2,"D": 2,"E": 1,},
            "B":{"A": 3,"B": 2,"C": 1,"D": 1,"E": 0,},
            "C":{"A": 2,"B": 1,"C": 1,"D": 0,"E": 0,},
            "D":{"A": 2,"B": 1,"C": 0,"D": 0,"E": 0,},
            "E":{"A": 1,"B": 0,"C": 0,"D": 0,"E": -1,},
            }

    CoreCombo = CoreMix[TOK][EE]

    # Simple check to see if a condition for diploma failure has been met
    if CoreCombo == -1:
        print("\nIt appears you have failed one or multiple of your core subjects, unfortunately a diploma score cannot be awarded")
        input("Press any key to exit")
        exit()

    else:
        FinalGrade = sum(all_grades) + CoreCombo

        # Another check to see if a condition for diploma failure has been met
        if FinalGrade < 24:
            print("\nUnfortunately your diploma score is bellow 24 points which is considered a failing condition.")
            print("You are therefore not eligble to recieve a diploma score")
            print(f"If you're still curious, your diploma score would have been: {str(FinalGrade)}\n")
            input("Press any key to exit")
            exit()

        else:
            print("\n----------")
            print("Your IB Diploma Score is: ", FinalGrade)
            print("----------\n")
            input("Press any key to exit")
            exit()
