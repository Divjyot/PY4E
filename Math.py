# Math
import math
import random


def forloop():#Defining a function creates a variable with the same name.
    print(math.pi)
    for i in range(10):
        print(random.randint(700, 900))
        
def randChoice():
    #---------------------------------------------------
    choice = {1,3,5,6,7}
    print("random choice: try 1")
    try:
        print(random.choice(choice)) # choice is a set not sequence
    except:
        print("Try 1: Error\n")
    #---------------------------------------------------
    print("random choice: try 2")
    choice = [1,3,5,6,7] # sequnce
    print("Try 2: ", random.choice(choice)) 


def myFunc(printhis):
    return (str(printhis) * 4)
    

# Defining a function creates a variable with the same name.
# The value of myFunc is a function object, which has type "function".    
print(myFunc(' spam'))


    

