from itertools import combinations

def analyze_component(data, threshold):
    count = 0
    temp_sum = 0
    for val in data:
        if val > threshold:
            count += 1
            temp_sum += val
    return count, temp_sum

def validate_entry(record):
    # Irrelevant validation logic (not used in final result)
    if not record.get('active'):
        return False
    if record.get('version', 0) < 2:
        return False
    return True

def calculate_performance(results):
    raw_values = [r['score'] for r in results]
    
    # Distractor: filtering irrelevant entries (none actually filtered)
    filtered_entries = [r for r in results if r['score'] >= 0]
    sorted_vals = sorted(raw_values)
    
    # Semi-relevant operation: compute quartiles (only median used)
    mid = len(sorted_vals) // 2
    median = sorted_vals[mid] if len(sorted_vals) % 2 == 1 else (sorted_vals[mid-1] + sorted_vals[mid]) / 2
    
    # Generate unnecessary combinations (distraction)
    combo_count = 0
    for combo in combinations(sorted_vals[:4], 2):
        combo_count += 1  # This just counts pairs, unused later
    
    # Key computation begins
    base_score = sum(raw_values) / len(raw_values)
    adjustment = 0
    
    # Conditional adjustment based on median
    if median > 75:
        adjustment += 12.5
    elif median > 60:
        adjustment += 5.0
    else:
        adjustment -= 3.5
    
    # Use dictionary operations to apply multipliers
    multipliers = {'A': 1.1, 'B': 1.05, 'C': 1.0, 'D': 0.9}
    category = results[0]['category']
    multiplier = multipliers.get(category, 1.0)
    
    # Accumulate final score through multiple steps
    intermediate = (base_score + adjustment) * multiplier
    penalty = 0
    
    # Another distraction: analyze_component called but only one return value used
    count_above, _ = analyze_component(raw_values, threshold=80)
    if count_above >= 3:
        penalty = 8.0
    
    final_score = intermediate - penalty
    
    # Red herring variable
    debug_info = {
        'count_above_80': count_above,
        'total_entries': len(raw_values),
        'computed_median': median
    }
    
    return final_score

# Main execution
benchmark_results = [
    {'score': 85, 'category': 'A', 'active': True, 'version': 3},
    {'score': 92, 'category': 'A', 'active': True, 'version': 3},
    {'score': 78, 'category': 'A', 'active': True, 'version': 3},
    {'score': 96, 'category': 'A', 'active': True, 'version': 3},
    {'score': 88, 'category': 'A', 'active': True, 'version': 3},
    {'score': 73, 'category': 'A', 'active': True, 'version': 3},
    {'score': 81, 'category': 'A', 'active': True, 'version': 3}
]

# Execution point of interest
final_score = calculate_performance(benchmark_results)
Result: {final_score}