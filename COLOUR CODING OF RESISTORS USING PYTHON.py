#PROJECT-02 TASK(30-07-2022)
#WAP identify the colour coding and print the exact resistance using python
import math
a=str(input("BAND 1 color="))
b=str(input("BAND 2 color="))
c=str(input("BAND 3 color="))
def check(a):
    if a=="black":
       return 0
    elif a=="brown":
       return 1
    elif a=="red":
       return 2
    elif a=="orange":
       return 3
    elif a=="yellow":
       return 4
    elif a=="green":
       return 5
    elif a=="blue":
       return 6
    elif a=="violet":
       return 7
    elif a=="grey":
       return 8
    elif a=="white":
       return 9
s=check(a)
v=check(b)
z=check(c)
print("The value of given resistor is \t:",s*10+v,"*10^{}".format(z))
print((s*10+v)*pow(10,z)) 
