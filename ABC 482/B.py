grid = [input() for _ in range(5)]

row = min(5 - s.count('o') for s in grid)

col = min(5 - s.count('o') for s in zip(grid[0], grid[1], grid[2], grid[3], grid[4]))

dig1 = 5 - sum(1 for i in range(5) if grid[i][i] == 'o')

dig2 = 5 - sum(1 for i in range(5) if grid[i][4 - i] == 'o')

print(min(row, col,  dig1, dig2))