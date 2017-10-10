# CTI-110 
# M3HW2 - Software Sales
# William Thomas
# 7 October 2017
# Program to determine discount rate and total cost based on amount of packages purchased.

def main():
# Get user input for quantity.
    quantity = float (input('Enter the number of packages to purchase: '))
# Define cost, discounts, and discount rate formulas.
    unit = 99
    reg_price = unit * quantity
    ten_p = 10
    twenty_p = 20
    thirty_p = 50
    forty_p = 100
    over_10_price = quantity * unit * 0.9
    over_10_discount = quantity * unit * 0.1
    over_20_price = quantity * unit * 0.8
    over_20_discount = quantity * unit * 0.2
    over_50_price = quantity * unit * 0.7
    over_50_discount = quantity * unit * 0.3
    over_100_price = quantity * unit * 0.6
    over_100_discount = quantity * unit * 0.4
    
# determine discount amount (if applicable) and output discount amount, discount, and total price.
    if quantity >= forty_p:
        print('The discount for ',quantity,' units is 40%. You save $',format(over_100_discount,',.2f'))
        print('The total discounted price of the purchase is $',format(over_100_price,',.2f'))
    elif quantity >= thirty_p:
        print('The discount for ',quantity,' units is 30%. You save $',format(over_50_discount,',.2f'))
        print('The total discounted price of the purchase is $',format(over_50_price,',.2f'))
    elif quantity >= twenty_p:
        print('The discount for ',quantity,' units is 20%. You save $',format(over_20_discount,',.2f'))
        print('The total discounted price of the purchase is $',format(over_20_price,',.2f'))
    elif quantity >= ten_p:
        print('The discount for ',quantity,' units is 10%. You save $',format(over_10_discount,',.2f'))
        print('The total discounted price of the purchase is $',format(over_10_price,',.2f'))
    elif quantity < ten_p:
        print('The total price of the purchase is $',format(reg_price,',.2f'))


main()
