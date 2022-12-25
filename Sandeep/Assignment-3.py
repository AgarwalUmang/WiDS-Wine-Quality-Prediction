# 3) Matrix Script
import re
#help(re)
p,q=map(int, input("Input rows and columns.(Format:row<space>column) ").split())
mat=list()
for i in range(p):
    mat.append(input("Input Matrix: "))
print(mat)
mat=list(zip(*mat))
print(mat)
matrix=""
for i in mat:
    matrix= matrix+"".join(i)
print(matrix)

matrix=re.sub(r'\b[^a-zA-Z0-9]+\b',r' ',matrix )
print(matrix)
