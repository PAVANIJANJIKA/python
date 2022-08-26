"""#PROJECT-01 TASK(30-07-2022)
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


#Program to multiply two matrices using nested loops
X=[[1,2],[3,4]]
Y=[[5,6],[7,8]]
result=[[0,0],[0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j]+=X[i][k]*Y[k][j]
for r in result:
  print(r)  """
     
#Program to multiply two matrices by using NUMPY 
import numpy k
X=([1,2],[3,4])
Y=([5,6],[7,8])
res=k.dot(x,y)
print(res)



















