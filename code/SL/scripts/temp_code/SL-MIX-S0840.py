from collections import defaultdict

def calculate_loading_efficiency(weights):
    n = len(weights)
    if n == 0:
        return 0
    
    # dp[i] stores the maximum efficiency up to package i
    dp = [0] * (n + 1)
    weight_count = defaultdict(int)
    
    for i in range(1, n + 1):
        weight = weights[i-1]
        weight_count[weight] += 1
        
        # Efficiency gain is weight multiplied by its occurrence count
        current_gain = weight * weight_count[weight]
        
        # Ternary operator to decide whether to include current package
        dp[i] = dp[i-1] + current_gain if current_gain > 0 else dp[i-1]
        
        # Additional bonus if consecutive packages have same weight
        if i > 1 and weights[i-2] == weight:
            dp[i] += weight // 2
    
    return dp[n]

# Package sequence for truck loading
packages = [10, 15, 15, 10, 20, 15, 10, 25]
max_efficiency = calculate_loading_efficiency(packages)
print(f"Result: {max_efficiency}")