from collections import defaultdict

def calculate_optimal_rate(entries):
    totals = defaultdict(float)
    counts = defaultdict(int)

    # Process each entry to compute category aggregates
    for entry in entries:
        category = entry['type']
        totals[category] += entry['value']
        counts[category] += 1

    # Compute average per category using lambda
    averages = {k: totals[k] / counts[k] for k in totals}
    
    # Determine optimal rate as the maximum average
    max_avg = max(averages.values())
    min_avg = min(averages.values())
    avg_of_extremes = (max_avg + min_avg) / 2
    
    scaling_factor = 0.9
    optimal_rate = round(avg_of_extremes * scaling_factor, 3)
    
    return optimal_rate

# Input data representing transaction values by type
data = [
    {'type': 'A', 'value': 150},
    {'type': 'B', 'value': 200},
    {'type': 'A', 'value': 250},
    {'type': 'C', 'value': 100},
    {'type': 'B', 'value': 300},
    {'type': 'C', 'value': 120}
]

result = calculate_optimal_rate(data)
print(f'Result: {result}')