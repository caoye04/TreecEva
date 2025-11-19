import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def min_delivery_cost(cost_matrix, start, visited, memo):
    if visited == (1 << len(cost_matrix)) - 1:
        return cost_matrix[start][0]
    
    if (start, visited) in memo:
        return memo[(start, visited)]
    
    min_cost = float('inf')
    for i in range(len(cost_matrix)):
        if not (visited & (1 << i)):
            new_visited = visited | (1 << i)
            cost = cost_matrix[start][i] + min_delivery_cost(cost_matrix, i, new_visited, memo)
            min_cost = min(min_cost, cost)
    
    memo[(start, visited)] = min_cost
    return min_cost

costs = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Compute LCM of first row as part of preprocessing
preprocess_lcm = lcm(lcm(costs[0][0]+1, costs[0][1]+1), lcm(costs[0][2]+1, costs[0][3]+1))

memoization_table = {}
visited_mask = 1  # Start from warehouse 0
initial_cost = min_delivery_cost(costs, 0, visited_mask, memoization_table)

# Apply logical conditions to adjust final cost
if initial_cost > 50 and preprocess_lcm < 500:
    final_cost = initial_cost - (preprocess_lcm % 10)
elif initial_cost <= 50 or preprocess_lcm >= 500:
    final_cost = initial_cost + (preprocess_lcm // 10)
else:
    final_cost = initial_cost

print(f"Result: {final_cost}")