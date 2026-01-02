from collections import defaultdict
from itertools import combinations

def analyze_growth_cycles(data, min_cycle=3):
    cycle_count = defaultdict(int)
    total_entries = len(data)
    temp_sum = 0
    
    for i in range(total_entries - min_cycle + 1):
        window = data[i:i+min_cycle]
        avg = sum(window) / min_cycle
        if avg > 8:
            cycle_count[min_cycle] += 1
        temp_sum += avg  
    
    # Distractor: unused computation
    squared_devs = [(x - sum(data)/len(data))**2 for x in data]
    variance_estimate = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    
    return dict(cycle_count)

def calculate_optimal_yield(dataset, threshold):
    growth_map = {}
    adjustment_factor = 0.85
    debug_logs = []
    
    for idx, value in enumerate(dataset):
        if value >= threshold:
            adjusted_value = value * adjustment_factor
            growth_map[idx] = adjusted_value ** 0.5
        else:
            growth_map[idx] = value / 2
    
    # Semi-relevant: tracks high performers but not used directly
    high_performers = [k for k, v in growth_map.items() if v > 4.0]
    
    # Core logic for yield calculation
    base_yield = sum(growth_map.values())
    penalty = 0
    
    # Additional distraction: complex condition that rarely triggers
    for a, b in combinations(growth_map.keys(), 2):
        if abs(a - b) == 1 and dataset[a] > 10 and dataset[b] > 10:
            penalty += 0.5
    
    final_yield = base_yield - penalty
    
    # Irrelevant list comprehension
    _ = [i**2 for i in range(len(dataset)//2)]
    
    return final_yield

# Simulated sensor readings from agricultural plots
harvest_data = [5, 12, 14, 6, 10, 13, 11, 7, 9]
threshold = 9

# Call analysis function (distractor)
analyze_growth_cycles(harvest_data)

# Key execution point
final_yield = calculate_optimal_yield(harvest_data, threshold)

print(f"Result: {final_yield}")