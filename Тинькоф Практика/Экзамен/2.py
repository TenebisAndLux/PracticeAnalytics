n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

r_matrix = [[0] * n for _ in range(m)]

for i in range(n):
    for j in range(m):
        r_matrix[j][n - i - 1] = matrix[i][j]

for row in r_matrix:
    print(' '.join(map(str, row)))
