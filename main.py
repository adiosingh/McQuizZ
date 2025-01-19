def main():
    total_score = 0  
    SECTION = 1

    maths_score=0
    chem_score=0
    phy_score=0

    while SECTION < 4:
        choice = int(input("Enter the choice for the subject you want to choose: (Maths-1, Chem-2, Physics-3), To exit enter -0 :-"))

        if choice != 1 and choice != 2 and choice != 3 and choice != 0:
            print("Enter a valid choice")

        elif choice == 0:
            print("You have successfully exited.")
            break

        else:
            if choice == 1:
                SECTION += 1
                maths_score=maths()
                total_score += maths_score
            elif choice == 2:
                SECTION += 1
                chem_score=chem() 
                total_score += chem_score
                
            elif choice == 3:
                SECTION += 1
                phy_score=phy() 
                total_score += phy_score
        
    print('''
********************************************''')
    print("MATHS SCORE       : ",maths_score)
    print("CHEMISTRY SCORE   : ",chem_score)
    print("PHYSICS SCORE     : ",phy_score)
    print('''
********************************************''')

    print("TOTAL SCORE       : ", total_score)  # Print the total score after all subjects are attempted
