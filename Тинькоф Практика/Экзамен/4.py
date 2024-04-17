def rotate_matrix(matrix, direction):
    n = len(matrix)

    operations = []

    for i in range(n):
        for j in range(i + 1, n):
            operations.append((i, j, j, i))
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    if direction == 'R':
        for i in range(n):
            for j in range(n // 2):
                operations.append((i, j, i, n - 1 - j))
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
    else:
        for i in range(n // 2):
            for j in range(n):
                operations.append((i, j, n - 1 - i, j))
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

    return operations


n, direction = input().split()
n = int(n)

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

operations = rotate_matrix(matrix, direction)
print(len(operations))
for op in operations:
    print(op[0], op[1], op[2], op[3])
