# CTI-110 
# M2HW1 - Distance Traveled  
# William Thomas
# 12 September 2017
# Calculates and displays distance travelled after a given time (input) at a constant speed 70 miles per hour.

# Declare Variables and test program function.
# Declare Value of flat speed (70mph).
flat_speed = 70

#Calculate distance travelled in 6 hours.
six_hour_distance = flat_speed * 6

#Calculate distance travelled in 10 hours.
ten_hour_distance = flat_speed * 10

#Calculate distance travelled in 15 hours.
fifteen_hour_distance = flat_speed * 15

#Display distances travelled.
print ('The distance travelled after 6 hours at a constant speed of 70mph is:', six_hour_distance, 'mph')
print ('The distance travelled after 10 hours at a constant speed of 70mph is:', ten_hour_distance, ',mph')
print ('The distance travelled after 15 hours at a constant speed of 70mph is:', fifteen_hour_distance, ',mph')

# Facilitate user input with program.
# Add functionality for user input of time as an integer.
# Get input for time variable.
seventy_time =  int (input('To find out how far you can travel at 70mph after a specific amount of time, enter the amount of hours travelled: '))

# Calculate the distance travelled as time (in hours) multiplied by 70(mph).
flat_distance_travelled = seventy_time * flat_speed

# Display distance travelled at 70 miles per hour calculation.
print('The distance travelled at 70mph after', seventy_time, 'will be:', flat_distance_travelled, 'miles.')

# Add functionality for user input of speed as an integer.
# Prompt user to apply a new variable.
print('Now that we have seen 70 miles per hour, try it with your own speed!')

# Get input for speed.
speed = int (input('Enter your speed in miles per hour (mph): '))

# Get input for time.
time =  int (input('Enter the amount of hours travelled: '))

# Calculate distance travelled with the variables of "speed" and "time" as user input integers.
distance_travelled = speed * time

# Display calculation for distance travelled.
print('The distance travelled at', speed,'mph, after', time,'hours will be:', distance_travelled)


