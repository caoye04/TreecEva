import re

def calculate_max_profit():
    vehicle_capacity = 15
    banned_keywords = ['fragile', 'liquid', 'hazard']
    
    # Package data: (weight, profit, description)
    packages = [
        (2, 3, 'electronics'),
        (3, 4, 'books'),
        (4, 5, 'fragile items'),
        (5, 6, 'clothing'),
        (1, 2, 'liquid materials'),
        (3, 5, 'tools'),
        (2, 3, 'toys'),
        (4, 7, 'hazardous goods')
    ]
    
    # Step 1: Filter out packages with banned keywords using regex
    safe_packages = [pkg for pkg in packages if not any(re.search(r'\b' + keyword + r'\b', pkg[2]) for keyword in banned_keywords)]
    
    # Step 2: Sort packages by profit/weight ratio descending (greedy)
    safe_packages.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    # Step 3: Dynamic Programming Knapsack
    n = len(safe_packages)
    dp = [[0 for _ in range(vehicle_capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight, profit, _ = safe_packages[i-1]
        for w in range(vehicle_capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + profit)
            else:
                dp[i][w] = dp[i-1][w]
    
    max_profit = dp[n][vehicle_capacity]
    return max_profit

result = calculate_max_profit()
print(f'Result: {result}')