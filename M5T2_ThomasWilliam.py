# CTI_110
# M5T2 - Bug Collector
# William Thomas
# 10 October 2017
# Program to keep a running total of bugs collected daily using a loop function.

def main():
    # Initialize accumulator.
    total = 0
    # Get user input for bugs collected each day.
    for day in range(1, 8):
    # Set user prompt.
        print('Enter the number of bugs collected on day', day,'below.')
    #input number of bugs.
        bugs = int(input())
    # Add bugs to total.
        total += bugs
    # Display the total bugs.
    print('You collected a total of', total, 'bugs.')
# Run program.
main()
    
