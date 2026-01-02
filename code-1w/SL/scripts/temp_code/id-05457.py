from itertools import combinations

def calculate_final_score(metrics):
    base = metrics['accuracy'] * 100
    penalty = 0
    
    # Apply complexity penalty based on feature interactions
    if len(metrics['features']) > 3:
        combos = list(combinations(metrics['features'], 3))
        penalty += len(combos) * 0.5
    
    # Conditional adjustment using boolean logic
    has_high_precision = metrics['precision'] > 0.85
    has_low_latency = metrics.get('latency', 100) < 50
    
    if has_high_precision and has_low_latency:
        base += 10
    
    adjusted_score = base - penalty
    return round(adjusted_score, 2)

# Simulated model evaluation data
data_map = {
    'accuracy': 0.92,
    'precision': 0.87,
    'latency': 45,
    'features': ['f1', 'f2', 'f3', 'f4', 'f5']
}

# Irrelevant auxiliary variable (minimal distraction)
temp_result = sum([1 for x in range(3)])

final_score = calculate_final_score(data_map)
print(f"Result: {final_score}")