#Write a function, parallel(), that, when called, outputs the effective resistance of a network of 2 or more resistors connected in parallel. 
#The function should be able to accept a list of numbers of any length.

def parallel(*resistances):
    totalres = 1 / sum((1 / resistance) for resistance in resistances)
    print("The total resistance is",totalres)