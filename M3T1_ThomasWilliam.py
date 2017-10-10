# CTI-110
# M3T1 - Areas Of Rectangles
# William Thomas
# 28 September 2017
# Program to calculate the area of rectangles with user input length and width

# Get the dimensions for rectangle 1.
length_1 = int(input("Enter the length of the first rectangle: "))
width_1 = int(input("Enter the width of the first rectangle: "))

# Get dimesions for rectangle 2.
length_2 = int(input("Enter the length of the second rectangle: "))
width_2 = int(input("Enter the width of the second rectangle: "))

# Calculate the area of rectangle_1.
area_1 = length_1 * width_1
area_2 = length_2 * width_2

# Determine which rectangle has the greater area.
if area_1 > area_2:
    print('The first rectangle has the greater area.')
elif area_2 > area_1:
    print('The second rectangle has the greater area.')
else:
    print('Both rectangles have the same area.')
