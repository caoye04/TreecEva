from collections import deque

def log_operations(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

class PackageOptimizer:
    def __init__(self):
        self.processed_packages = []
        self.optimization_matrix = {}
    
    @log_operations
    def calculate_optimal_loading(self, packages_weights, packages_priorities, truck_capacity):
        n = len(packages_weights)
        # Initialize DP table
        dp = [[0 for _ in range(truck_capacity + 1)] for _ in range(n + 1)]
        
        # Fill DP table using dynamic programming
        for i in range(1, n + 1):
            for w in range(truck_capacity + 1):
                # Don't take the item
                dp[i][w] = dp[i-1][w]
                
                # Take the item if it fits
                if packages_weights[i-1] <= w:
                    value_with_item = dp[i-1][w - packages_weights[i-1]] + packages_priorities[i-1]
                    dp[i][w] = max(dp[i][w], value_with_item)
        
        # Backtrack to find selected items
        selected = []
        w = truck_capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:
                selected.append(i-1)
                w -= packages_weights[i-1]
        
        return dp[n][truck_capacity], selected

# Package data
package_weights = [10, 20, 30, 40, 50]
package_priorities = [60, 100, 120, 140, 160]
truck_max_capacity = 100

# Initialize optimizer
optimizer = PackageOptimizer()

# Process packages using a stack for validation
package_stack = deque(list(zip(package_weights, package_priorities)))
validated_packages_weights = []
validated_packages_priorities = []

while package_stack:
    weight, priority = package_stack.pop()
    # Validate package (simple check)
    if weight > 0 and priority > 0:
        validated_packages_weights.insert(0, weight)
        validated_packages_priorities.insert(0, priority)

# Apply greedy preprocessing to sort by priority-to-weight ratio
ratio_indices = [(package_priorities[i]/package_weights[i], i) for i in range(len(package_weights))]
ratio_indices.sort(reverse=True)

sorted_weights = [package_weights[i] for _, i in ratio_indices]
sorted_priorities = [package_priorities[i] for _, i in ratio_indices]

# Calculate optimal loading
optimized_priority_score, selected_items = optimizer.calculate_optimal_loading(
    sorted_weights, 
    sorted_priorities, 
    truck_max_capacity
)

print(f"Result: {optimized_priority_score}")