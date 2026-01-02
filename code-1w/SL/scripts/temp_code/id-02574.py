from itertools import combinations
import math

def analyze_variance(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance

def generate_frequency_map(sequence):
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = sum(freq_map.values())
    normalized = {k: v / total for k, v in freq_map.items()}
    return normalized

def detect_equilibrium(frequencies, threshold=0.05):
    values = list(frequencies.values())
    variance = analyze_variance(values)
    
    # Distractor: irrelevant combination analysis
    combo_count = 0
    for r in range(2, 4):
        for _ in combinations(values, r):
            combo_count += 1
    
    # Irrelevant smoothing simulation
    smoothed = [v + 0.01 for v in values]
    smooth_variance = analyze_variance(smoothed)
    
    # Actual equilibrium logic
    if variance < threshold:
        base_score = 100 * (1 - variance / threshold)
    else:
        base_score = 50 * (threshold / variance)
    
    # Distractor: unused adjustment path
    adjustment_factor = 1.0
    if len(values) > 3:
        adjustment_factor = 0.9
    elif len(values) == 2:
        adjustment_factor = 1.1  # Never applied due to order
    
    final_score = base_score  # adjustment_factor intentionally omitted
    
    # Additional red herring: slicing and reversing with no effect
    reversed_slice = values[::-1][1:]
    temp_sum = sum(reversed_slice[:3]) if len(reversed_slice) >= 3 else 0
    
    return int(final_score)

# Main execution
raw_sequence = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
frequencies = generate_frequency_map(raw_sequence)

# Unused distractor variables
aggregate_weight = sum(f * f for f in frequencies.values())
diagonal_pairs = list(combinations(frequencies.keys(), 2))
entropy_proxy = -sum(p * math.log(p) for p in frequencies.values() if p > 0)

# Key computation
equilibrium_score = detect_equilibrium(frequencies, threshold=0.05)

# Print result
print(f"Result: {equilibrium_score}")