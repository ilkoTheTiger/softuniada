from pprint import pprint

n = int(input())

matrix = []
for row in range(n):
    matrix.append([int(num) for num in input().split()])

def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

new_matrix = rotate_matrix(matrix)
new_matrix = rotate_matrix(new_matrix)
new_matrix = rotate_matrix(new_matrix)

for row in new_matrix:
    print(" ".join([str(x) for x in row]))