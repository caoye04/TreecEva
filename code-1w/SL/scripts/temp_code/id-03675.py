from itertools import combinations

# Simulate sensor data calibration with noise filtering and weighted aggregation
def preprocess_entry(raw_value, correction_factor):
    if raw_value < 0:
        raw_value = abs(raw_value)
    corrected = raw_value * correction_factor
    normalized = corrected / (corrected + 10)  # dampen high values
    return round(normalized, 4)

def generate_weight_combinations(n):
    # Generates dummy weight patterns – not used in final logic but adds distraction
    all_weights = []
    for r in range(1, min(n+1, 4)):
        all_weights.extend(combinations(range(1, n+1), r))
    return all_weights

def calculate_stability_index(entries):
    diffs = [abs(entries[i] - entries[i-1]) for i in range(1, len(entries))]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    stability = 1 / (1 + avg_diff)
    return round(stability, 4)

def calculate_final_score(data_entries, weights):
    # Preprocess each entry with fixed correction factor
    processed = [preprocess_entry(v, 1.25) for v in data_entries]
    
    # Irrelevant computation: analyze stability but don't use it directly
    stability = calculate_stability_index(processed)
    temp_adjustment = 0
    if stability > 0.5:
        temp_adjustment = 0.05 * stability
    
    # Actual scoring uses weighted sum – only first three weights are used
    weighted_sum = 0
    for i in range(min(len(processed), len(weights))):
        weighted_sum += processed[i] * weights[i]
    
    # Apply artificial cap and scale
    capped_sum = min(weighted_sum, 3.8)
    
    # Secondary adjustment using unused portion of weights (distractor)
    unused_weights_sum = sum(w for w in weights[len(processed):])
    phantom_impact = unused_weights_sum * 0.01  # never actually applied
    
    # Final nonlinear transformation
    final_score = (capped_sum ** 1.1) + 0.1 * len(data_entries)
    
    # Key execution point: final_score computed here
    return round(final_score, 4)

# Main execution block
if __name__ == "__main__":
    raw_data = [12, -8, 15, 23, 7]
    calibration_weights = [0.3, 0.5, 0.4, 0.6, 0.2, 0.9, 1.1]
    
    # Dummy call to distract – result not used
    _ = generate_weight_combinations(5)
    
    # Noise threshold calculation (dead code path)
    max_noise_level = max(raw_data) / 100
    safety_margin = max_noise_level * 0.2
    
    # Core computation
    final_score = calculate_final_score(raw_data, calibration_weights)
    
    # Output target result
    print(f"Target result: {final_score}")