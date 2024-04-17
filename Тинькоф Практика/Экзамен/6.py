n = int(input())
board = [list(input().strip()) for _ in range(n)]

knight = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
king = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def is_valid(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


queue = []
visited = set()
for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            queue.append((i, j, 0, 'k'))
            visited.add((i, j, 'k'))
        elif board[i][j] == 'K':
            visited.add((i, j, 'k'))
        elif board[i][j] == 'G':
            visited.add((i, j, 'kg'))

min_moves = float('inf')
found = False

while queue:
    x, y, moves, transform = queue.pop(0)

    for dx, dy in (knight if transform == 'k' else king):
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y):
            if board[new_x][new_y] == 'F':
                min_moves = min(min_moves, moves + 1)
                found = True
                break

            if (new_x, new_y, transform) not in visited:
                if board[new_x][new_y] == 'K' and transform == 'k':
                    transform = 'kg'
                elif board[new_x][new_y] == 'G' and transform == 'k':
                    transform = 'g'
                visited.add((new_x, new_y, transform))
                queue.append((new_x, new_y, moves + 1, transform))

if found:
    print(min_moves)
else:
    print(-1)
