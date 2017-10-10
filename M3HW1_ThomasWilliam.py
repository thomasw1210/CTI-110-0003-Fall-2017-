# CTI-110 
# M3HW1 - Age Classifier 
# William Thomas
# 7 October 2017
# Program to take an input number (age) and output an age classification.

def main():
# Define ages.
    infant = 1
    child = 12
    teen = 19
    adult = 20    

    # Get user input for age, and classify by age definitions.
    age = int (input('Enter age: '))
    
    if age <= infant:
        print('You are an infant.')
    elif age <= child:
        print('You are a child.')
    elif age <= teen:
        print('You are a teenager.')
    elif age >= adult:
        print('You are an adult.')


main()
