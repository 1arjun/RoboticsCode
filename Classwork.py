from random import randint
#HI
x = input("Guess a number between 1 and 5")
x = int (x)
y = randint (1,5)
print (y)
correct = False
if (x==y):
    print ("You win!")
while (correct == False):
    print ("Try again")
    x = input("Pick a new number:")
    x = int (x)
    if (x==y):
        correct = True
        print ("You win")
    

