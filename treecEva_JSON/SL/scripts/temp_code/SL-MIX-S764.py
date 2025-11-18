from collections import defaultdict

def optimize_loading(weights, T):
    n = len(weights)
    # Initialize DP table with defaultdict for automatic zero initialization
    dp = defaultdict(lambda: defaultdict(int))
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(T + 1):
            # Don't take the current package
            dp[i][w] = dp[i-1][w]
            # Take the current package if it fits
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + weights[i-1])
    
    return dp

# Package weights
package_weights = [3, 8, 9, 6, 5]
threshold = 15

dp_table = optimize_loading(package_weights, threshold)

# What is the value of dp[4][15]?
result = dp_table[4][15]
print(f"Result: {result}")