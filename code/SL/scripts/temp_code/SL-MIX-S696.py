def fibonacci_sequence(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

class LoadingTracker:
    def __init__(self):
        self.total_loaded = 0
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        
    def load_package(self, weight):
        self.total_loaded += weight
        return self.total_loaded

def optimize_loading(capacity, package_weights):
    loaded_weight = 0
    tracker = LoadingTracker()
    
    with tracker as loader:
        for weight in package_weights:
            if loaded_weight + weight <= capacity:
                loaded_weight = loader.load_package(weight)
            else:
                break
    return loaded_weight

import itertools

# Generate first 15 Fibonacci numbers as package weights
package_pool = list(fibonacci_sequence(15))

# Consider all combinations of 10 packages from the pool
combinations = list(itertools.combinations(package_pool, 10))

# Apply greedy loading to each combination with truck capacity 1000
max_loaded = 0
for combo in combinations:
    # Sort in ascending order for greedy approach (lightest first)
    sorted_combo = sorted(combo)
    loaded = optimize_loading(1000, sorted_combo)
    if loaded > max_loaded:
        max_loaded = loaded

final_loading_result = max_loaded
print(f"Result: {final_loading_result}")