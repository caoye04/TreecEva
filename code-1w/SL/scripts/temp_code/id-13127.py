from itertools import combinations

def evaluate_pair_stability(pair):
    a, b = pair
    return (a * b) / (a + b) if (a + b) != 0 else 0

def compute_aggregate(elements, threshold=2):
    valid_pairs = []
    for pair in combinations(elements, 2):
        stability = evaluate_pair_stability(pair)
        if stability > threshold:
            valid_pairs.append(stability)
    
    total_harmonic_score = sum(valid_pairs)
    outlier_count = sum(1 for x in elements if x < 0)  # Irrelevant metric (distractor)
    max_pair_value = max(valid_pairs) if valid_pairs else 0  # Another derived metric
    
    return total_harmonic_score

# Main execution
sensor_readings = [3, 4, 5, 8]
total_harmonic_score = compute_aggregate(sensor_readings)
Result: total_harmonic_score