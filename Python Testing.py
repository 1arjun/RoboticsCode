osurhgosg

# Declaring Variables:

# e.g. x = 5, No syntax
# Example for loop
# for i in range (5)
#   print ("x")
# There is no ending syntax, instead python is sensitive to indents, everything
# in the for loop with be under one indent, and a indent reset will signal that
# the code in the for loop has ended.

#Inputting values in the print box:
# e.g. x=input("enter a number: ")
# What is in the Quotations will be printed, and whatever number is inputted
# be assigned to x

#If/Elif/Else Statments:
#e.g. x=input("Pick a number between 1 and 5 ")
# if (x==3):
#   print("You got it right!")
# elif (x>3):
#   print("lower")
# else:
#   print ("Higher")
# You can have as many elif statements as you want



#x=input("Pick a number between 1 and 1000 ")
#x = float (x)
#if (x==548.1):
#    print("You got it right!")
#elif (x>548.1):
#    print("lower")
#else:
#    print ("Higher")

x, y=input("Pick two numbers")
x = int (x)
if (x==5):
    print("The first number is right!")
elif (x>5):
    print("lower")
else:
    print ("Higher")
y = int (y)
if (y==3):
    print("The second number is right")
elif (x>3):
    print ("higher")
else:
    print ("Lower")

