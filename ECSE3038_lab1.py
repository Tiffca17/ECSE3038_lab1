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

#Write a function, `temperature_check()`, that accepts a single number, a patient's body temperature, and a single character, the unit of temperature. 
#The function should output whether the patient is hypothermic, hyperthermic or has normal body temperature based on the number passed to the function. 
#The second value passed as argument should tell the function whether the condition should calculated in degrees celcius or degrees fahrenheit.
#An appropriate message should be written to the screen with the result. You’re free to use what ever reasonable temperature limits you feel will 
#adequately act as boundaries for these conditions.
def temperature_check(temp,char:str):
    if (char == "C" or char =="c"):
        if temp < 35:
            print("The patient is hypothermic.")
        elif temp > 40:
            print("the patient is hyperthermic.") 
        else:
            print("the patient has a normal body temperature.")
    if (char == "F" or char == "f"):
        if temp < 95:
            print("The patient is hypothermic.")
        elif temp > 104:
            print("The patient is hyperthermic.")
        else:
            print("The patient has a normal body temperature.")
