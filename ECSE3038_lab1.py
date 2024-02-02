#Write a function, parallel(), that, when called, outputs the effective resistance of a network of 2 or more resistors connected in parallel. 
#The function should be able to accept a list of numbers of any length.

def parallel(*resistances):
    totalres = 1 / sum((1 / resistance) for resistance in resistances)
    print("The total resistance is",totalres)

#Write a function, potential_divider(), that takes two values as argument, a number that represents a voltage 
#supply value and a list of numbers that represent resistance values of resistors connected in series. 
#The function should output the voltage drop across each resistor in your resistor list. 
#The function should be able to accept a list of numbers of any length.
    
def potential_divider(voltage,*res):
    volt_drops = [voltage * resistance / sum(res) for resistance in res]
    print("The voltage drops are", volt_drops)

potential_divider(5,100,20,50)
