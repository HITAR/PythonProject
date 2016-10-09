n = input("input lines' num:")
print("input value of matrix A")
a,b,c = [],[],[]
for i in range(0,n):
    a.append([int(x) for x in input("").split(" ")])

print("input value of matrix A")

for i in range(0,n):
    b.append([int(x) for x in input("").split(" ")])

for i in range(0, n):
    c.append([a[i][j] * b[j][i] for j in range(0,n)])