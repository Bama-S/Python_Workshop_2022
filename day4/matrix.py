#3x3 matrix addition with lists and loop
mat1 = [[1,2,3],[1,2,1],[2,3,5]]
mat2 = [[1,2,3],[1,2,1],[2,3,5]]

total = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(mat1)):
    for j in range(len(mat2)):
        total[i][j] = mat1[i][j]+mat2[i][j]

print("matrix 1 ", mat1)
print("matrix 2 ", mat2)
print ("addition ", total)

#write a function to take  5 numbers in a list and double those.