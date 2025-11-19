from functools import reduce
from collections import defaultdict

def max_non_consecutive_load(weights):
    n = len(weights)
    if n == 0:
        return 0
    if n == 1:
        return weights[0]
    
    dp = [0] * n
    dp[0] = max(0, weights[0])
    dp[1] = max(dp[0], weights[1])
    
    for i in range(2, n):
        # Early return if all remaining weights are negative
        if all(w < 0 for w in weights[i:]):
            return dp[i-1]
        dp[i] = max(dp[i-1], dp[i-2] + weights[i])
    
    return dp[-1]

package_weights = [2, 1, 4, 9, -1, 3, 5, 2]
intermediate_sums = list(map(lambda x: x*2 if x%2==0 else x+1, package_weights))
filtered_weights = list(filter(lambda x: x > 0, intermediate_sums))

load_map = defaultdict(int)
for idx, val in enumerate(filtered_weights):
    load_map[idx] = val

weight_list = [load_map[i] for i in sorted(load_map.keys())]
max_load = max_non_consecutive_load(weight_list)
print(f"Result: {max_load}")