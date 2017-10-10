# CTI_110
# M5HW2 - Distance Travelled
# William Thomas
# 10 October 2017
# Program to calculate distance travelled when given user input for speed and time (in hours).

def main():
    # Get user input for speed.
    speed = int(input('What is the speed of the vehicle in mph? '))
    # Get user input for hours travveled (hours).
    hours = int(input('How many hours has the vehicle travelled? '))
    # Initialize accumulator.
    time = 0
    # Set parameters for loop.
    max_time = hours
    # Define loop.
    while time < max_time:
    # set loop to increase by 1 per iteration.
        time = time + 1
    # Define distance travelled formula.
        distance = speed * time
    # Display the distance travelled.
        print('The distance travelled after',time,' hour(s) is', distance,'miles.')
# Run program.
main()
    
