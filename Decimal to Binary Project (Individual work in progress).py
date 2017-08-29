# Decimal to Binary (I/O function)
# 29 August 2017
# <Individual Practice>
# William Thomas

# Adjusting code to input/output function(work in progress)

def convertToBinary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# Input Decimal number
dec = float (input('Enter decimal format number: '))

#Convert Decimal to Binary
convertToBinary(dec)
