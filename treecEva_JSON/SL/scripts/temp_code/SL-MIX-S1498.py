class FuelTracker:
    def __init__(self):
        self.consumption_log = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def log_consumption(self, amount):
        self.consumption_log.append(amount)

# Recursive route optimizer with backtracking
def optimize_route(stops, index, current_fuel, tracker):
    # Early termination conditions
    if index >= len(stops):
        return current_fuel
    
    if current_fuel > 100:  # Pruning paths with excessive fuel
        return float('inf')
    
    # Backtracking with two possible optimizations
    original_fuel = current_fuel
    
    # Option 1: Standard path
    standard_fuel = optimize_route(stops, index + 1, current_fuel + stops[index], tracker)
    
    # Option 2: Optimized path (only if beneficial)
    if stops[index] > 5:
        optimized_increment = stops[index] // 2
        optimized_fuel = optimize_route(stops, index + 1, current_fuel + optimized_increment, tracker)
    else:
        optimized_fuel = float('inf')
    
    # Choose better option
    chosen_fuel = min(standard_fuel, optimized_fuel)
    
    # Log only if this path leads to solution
    if chosen_fuel != float('inf') and index == len(stops) - 1:
        tracker.log_consumption(chosen_fuel)
    
    return chosen_fuel

# Dictionary comprehension for route data
route_segments = {f'stop_{i}': val for i, val in enumerate([12, 8, 15, 6, 20, 4, 18])}
segment_values = list(route_segments.values())

# Merge with baseline metrics
efficiency_metrics = {'baseline': 25}
efficiency_metrics = efficiency_metrics | {'optimized': 0}  # Dictionary merging

# Execute optimization with context manager
with FuelTracker() as fuel_tracker:
    optimized_fuel_tally = optimize_route(segment_values, 0, 0, fuel_tracker)
    if fuel_tracker.consumption_log:
        optimized_fuel_tally = sum(fuel_tracker.consumption_log)

print(f"Result: {optimized_fuel_tally}")