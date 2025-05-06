matrix = [list(map(int, input().split())) for _ in range(9)]

row, col, val = 0, 0, -1
for i in range(9):
    for j in range(9):
        if matrix[i][j] > val:
            val = matrix[i][j]
            row = i+1
            col = j+1

print(f'{val}\n{row} {col}')