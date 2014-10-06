#Daniel Ogunlana
#selection develop exercise 2
#06-10-2014

temperature = int(input("What is the temperature of the water?:"))
if temperature <0:
    print("The water is a solid")
elif temperature >0 and temperature <=99.98:
    print("The water is a liquid")
else:
    print("The water is a gas")
