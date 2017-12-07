# CTI-110
# M6T1: Kilometer Converter
# William Thomas
# 7 December 2017
# Program to convert distance given in kilometers to miles.


# Set conversion factor.
CONVERSION_FACTOR = 0.6214

# set main function.
def main():
    # Get distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)

# Set show_miles function.
def show_miles(km):
    # Calculate distance in miles using conversion factor.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km, 'kilometers equals', format(miles, ',.4f'), 'miles.')

# Call main function.
main()

