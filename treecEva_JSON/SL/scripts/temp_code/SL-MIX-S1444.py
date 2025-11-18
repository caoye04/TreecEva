from collections import Counter

class LoadOptimizer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.weights = []
        self.best_count = 0
        
    def load_packages(self, available_weights):
        self.weights = sorted(available_weights, reverse=True)
        self._backtrack(0, 0, 0, [])
        return self.best_count
    
    def _backtrack(self, index, current_weight, count, selected):
        # Update best count if we found a better solution
        if count > self.best_count:
            self.best_count = count
            
        # Base case: reached end of list
        if index >= len(self.weights):
            return
            
        # Try including current package if it fits
        if current_weight + self.weights[index] <= self.capacity:
            selected.append(self.weights[index])
            self._backtrack(index + 1, current_weight + self.weights[index], count + 1, selected)
            selected.pop()
            
        # Try excluding current package (skip duplicates for efficiency)
        next_index = index + 1
        while next_index < len(self.weights) and self.weights[next_index] == self.weights[index]:
            next_index += 1
        self._backtrack(next_index, current_weight, count, selected)

class MetricsLogger:
    def __enter__(self):
        self.metrics = Counter()
        return self.metrics
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Main execution
package_weights = [7, 3, 5, 10, 2, 8, 3, 7, 1, 9, 4, 6]
truck_capacity = 25

with MetricsLogger() as metrics:
    optimizer = LoadOptimizer(truck_capacity)
    optimal_load_count = optimizer.load_packages(package_weights)
    metrics.update(package_weights)
    
    # Additional processing based on metrics
    heavy_items = sum(1 for w in package_weights if w > 7)
    light_items = sum(1 for w in package_weights if w <= 7)
    
    # Adjust optimal count based on weight distribution
    adjustment = 1 if heavy_items > light_items else -1 if heavy_items < light_items else 0
    optimal_load_count = optimal_load_count + adjustment if optimal_load_count > 0 else 0

print(f"Result: {optimal_load_count}")