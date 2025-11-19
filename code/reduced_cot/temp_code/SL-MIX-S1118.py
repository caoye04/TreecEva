def fibonacci_sequence(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

sensor_grid = [
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [9, 8, 7, 6],
    [3, 1, 4, 1]
]

fib_weights = fibonacci_sequence(4)
weighted_grid = [[sensor_grid[i][j] * fib_weights[j] for j in range(4)] for i in range(4)]
row_sums = [sum(row) for row in weighted_grid]
transform = lambda x: x**2
squared_row_sums = [transform(s) for s in row_sums]
final_metric = sum(squared_row_sums) - (row_sums[0] * row_sums[-1])
print(f"Result: {final_metric}")