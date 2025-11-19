from collections import defaultdict
import math

elevation_grid = [
    [10, 15, 20, 18],
    [12, 14, 19, 21],
    [11, 13, 17, 22],
    [16, 18, 20, 25]
]
rows, cols = len(elevation_grid), len(elevation_grid[0])

dp = [[float('inf')] * cols for _ in range(rows)]
dp[0][0] = elevation_grid[0][0]

for r in range(rows):
    for c in range(cols):
        if r > 0:
            dp[r][c] = min(dp[r][c], dp[r-1][c] + elevation_grid[r][c])
        if c > 0:
            dp[r][c] = min(dp[r][c], dp[r][c-1] + elevation_grid[r][c])

optimal_trail_length = dp[rows-1][cols-1]
print(f"Result: {optimal_trail_length}")