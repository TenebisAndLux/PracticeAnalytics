def max_mushrooms(forest):
    maximum = 0

    for i in range(3):
        if forest[0][i] != 'W':
            maximum = max(maximum, dfs(forest, 1, i, 0))

    return maximum


def dfs(forest, i, j, mushrooms):
    if i == len(forest):
        return mushrooms

    maximum = 0

    for k in range(3):
        if (0 <= j + k - 1 < len(forest[0])) and (forest[i][j + k - 1] != 'W'):
            if forest[i][j + k - 1] == 'C':
                maximum = max(maximum, dfs(forest, i + 1, j + k - 1, mushrooms + 1))
            else:
                maximum = max(maximum, dfs(forest, i + 1, j + k - 1, mushrooms))

    return maximum


n = int(input())
forest = [list(input()) for _ in range(n)]
print(max_mushrooms(forest))
