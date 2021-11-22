"""
3. Write a program that asks a user for an integer, print "Odd" if it's odd and print "Even" otherwise.
Hint use % (modular). Any even integer is divisible by 2 and the remainder is 0. Any odd integer when divided by 2 will have a remainder of 1. 
"""
Even_or_odd = int(input("Give me an integer and I will determine wether is even or odd "))
if Even_or_odd % 2 == 1:
  print ("odd")
else:
  print ("even")