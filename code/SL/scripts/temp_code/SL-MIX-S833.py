import itertools

def calculate_weight_class(weight):
    return 0 if weight < 5 else (1 if weight < 15 else 2)

def compute_package_priority(weights):
    classifications = [calculate_weight_class(w) for w in weights]
    # Apply dynamic programming to find max non-adjacent sum
    n = len(classifications)
    if n == 0:
        return 0
    elif n == 1:
        return classifications[0]
    dp = [0] * n
    dp[0] = classifications[0]
    dp[1] = max(classifications[0], classifications[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + classifications[i])
    return dp[-1]

# Package weights in kg
package_weights = [3, 7, 16, 2, 9, 14, 1, 18, 5, 11]

# Divide and conquer grouping: split into chunks of 3
chunk_size = 3
groups = [package_weights[i:i + chunk_size] for i in range(0, len(package_weights), chunk_size)]

# Compute priority scores for each group using dynamic programming
priority_scores = [compute_package_priority(group) for group in groups]

# Bitwise score adjustment based on group position
adjusted_scores = [
    score << (i & 3) if i % 2 == 0 else score >> (i & 3)
    for i, score in enumerate(priority_scores)
]

# Merge scores using XOR as a diversification operator
merged_score = 0
for score in adjusted_scores:
    merged_score ^= score

# Final ternary-based loading optimization
optimal_loading_score = (
    merged_score * 2 if merged_score > 10 
    else (merged_score + 5 if merged_score > 5 else merged_score)
)

print(f"Result: {optimal_loading_score}")