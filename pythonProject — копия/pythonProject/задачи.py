size = int(input())
matrix = [[0] * size for _ in range(size)]
for i in range(1, size):
    st = input().split()
    for col in range(len(st)):
        matrix[i][col] = matrix[col][i] = int(st[col])
table = matrix
for elem in table:
    print(*elem)
