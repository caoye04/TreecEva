from collections import defaultdict

cost_matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
dp_table = defaultdict(lambda: defaultdict(int))
adjusted_cost_sum = 0

for i in range(4):
    for j in range(4):
        base_cost = cost_matrix[i][j]
        if base_cost > 100:
            dp_table[i][j] = base_cost * 0.9
        else:
            dp_table[i][j] = base_cost
        adjusted_cost_sum += dp_table[i][j]

print(f"Result: {int(adjusted_cost_sum)}")