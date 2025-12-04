test = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

test = test.strip().splitlines()

grid = [list(row) for row in test]

print(grid)

surround_arr = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print((i, j), grid[i][j])
        if grid[i][j] == '@':
            # surround_arr.append(grid[i][j])
