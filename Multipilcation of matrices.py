
#PROJECT-03 TASK(30-07-2022)
#Program to multiply two matrices using nested loops
X=[[1,2],[3,4]]
Y=[[5,6],[7,8]]
print("1st matrix:",X)
print("2nd matrix:",Y)
result=[[0,0],[0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j]+=X[i][k]*Y[k][j]
for r in result:
  print(r)
     
