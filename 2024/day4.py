import re

# Read in the input file
file = open('/Users/ringi/Documents/code/advent_code/2024/input_day4.txt','r')

test = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


# Directions for 8 neighbors (row_offset, col_offset)
M_directions = [
    (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
    (0, -1),         (0, 1),     # Left,         Right
    (1, -1), (1, 0), (1, 1)      # Bottom-left, Bottom, Bottom-right
]


rows = []
for line in test.splitlines():
    row = list(line.strip())
    rows.append(row)

print(rows)
# count = 0
# visited = set() 

# for i, row in enumerate(rows):      
#     for j, col in enumerate(row):   
#         if col == "X" and (i, j) not in visited:  # Check 'X' and ensure it's not revisited
#             for dr, dc in M_directions:  # Check all 8 directions
#                 ni, nj = i + dr, j + dc
#                 # Check if 'M' is within bounds
#                 if 0 <= ni < len(rows) and 0 <= nj < len(row) and rows[ni][nj] == 'M':  
#                     ai, aj = i + 2 * dr, j + 2 * dc
#                     # Check if 'A' is within bounds
#                     if 0 <= ai < len(rows) and 0 <= aj < len(row) and rows[ai][aj] == 'A':
#                         si, sj = i + 3 * dr, j + 3 * dc
#                         # Check if 'S' is within bounds
#                         if 0 <= si < len(rows) and 0 <= sj < len(row) and rows[si][sj] == 'S':
#                             count += 1
#                             visited.update([(i, j), (ni, nj), (ai, aj), (si, sj)])  # Mark all parts of 'XMAS' as visited



with open('input_day4.txt') as content:
    rows = []
    for line in content:
        row = list(line.strip())
        rows.append(row)
        # print(rows)

        count = 0
        visited = set() 
    # print(rows)
        for i, row in enumerate(rows):      
            for j, col in enumerate(row):   
                if col == "X" and (i, j) not in visited:  # Check 'X' and ensure it's not revisited
                    for dr, dc in M_directions:  # Check all 8 directions
                        ni, nj = i + dr, j + dc
                        # Check if 'M' is within bounds
                        if 0 <= ni < len(rows) and 0 <= nj < len(row) and rows[ni][nj] == 'M':  
                            ai, aj = i + 2 * dr, j + 2 * dc
                            # Check if 'A' is within bounds
                            if 0 <= ai < len(rows) and 0 <= aj < len(row) and rows[ai][aj] == 'A':
                                si, sj = i + 3 * dr, j + 3 * dc
                                # Check if 'S' is within bounds
                                if 0 <= si < len(rows) and 0 <= sj < len(row) and rows[si][sj] == 'S':
                                    count += 1
                                    visited.update([(i, j), (ni, nj), (ai, aj), (si, sj)])  # Mark all parts of 'XMAS' as visited

    
print("Part 1 solution: ", count)

