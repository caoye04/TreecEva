from collections import Counter

def calculate_final_score(temp_data, limits):
    # Filter temperatures above threshold using list comprehension
    high_temps = [t for t in temp_data if t > limits['critical']]
    
    # Count occurrences of each temperature
    temp_counts = Counter(high_temps)
    
    # Calculate base score using sum and conditional expression
    base_score = sum([v * (k // 10) for k, v in temp_counts.items()])
    
    # Apply multiplier based on whether any extreme values exist
    multiplier = 1.5 if any(t > limits['extreme'] for t in high_temps) else 1.0
    
    # Final adjustment using slicing: consider only first 3 high temp entries
    sliced_contribution = sum([temp_counts[t] for t in sorted(temp_counts.keys())[:3]])
    
    result = base_score * multiplier + sliced_contribution
    return result

# Simulated sensor data
temperatures = [23, 35, 35, 47, 48, 51, 51, 51, 63, 77, 88, 95]
thresholds = {'critical': 30, 'extreme': 90}

result = calculate_final_score(temperatures, thresholds)
print(f"Result: {result}")