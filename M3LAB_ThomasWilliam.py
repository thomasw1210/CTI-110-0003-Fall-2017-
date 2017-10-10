# CTI-110
# M3LAB - Debugging
# William Thomas
# 10 Oct 2017
# Program to take a number grade and output a letter grade.

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    # Get user input for score, and determine letter grade with if/else statements.    
    score = int (input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
             print('Your grade is: B')
        else:
            if score >= C_score:
                 print('Your grade is: C')
            else:
                if score >= D_score:
                     print('Your grade is: D')
                else:
                    print('Your grade is: F')


# program start
main()
