from itertools import combinations

# Simulated sensor data processing (non-quantum, non-sensor themed)
def preprocess_readings(raw_values):
    filtered = [x for x in raw_values if x > 0]
    normalized = [round(x / sum(filtered), 4) for x in filtered]
    return normalized

def generate_pairs(values):
    # Irrelevant helper: generates pairs but only used for distraction
    return list(combinations(values, 2))

def validate_monotonic(sequence):
    # Dead code path - never actually used
    return all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))

def calculate_baseline(reference):
    # Semi-relevant: used in intermediate step but not final result
    base = 0
    for val in reference:
        if val > 0.1:
            base += val * 2
    return round(base, 4)

def calculate_final_score(stream):
    processed = preprocess_readings(stream)
    
    # Distraction: pair generation with no impact on result
    _ = generate_pairs(processed)
    
    # Key computation branch
    total = 0
    weights = [1, 2, 1, 3]  # weighting pattern
    for i, val in enumerate(processed):
        if i % 2 == 0:
            total += val * weights[i % len(weights)]
        else:
            total -= val * 0.5
    
    # Secondary adjustment
    adjustment = 0
    for val in processed:
        if val < 0.05:
            adjustment += val
    
    # Final transformation
    final = int((total - adjustment) * 1000)
    
    # Unused diagnostic variables (distractors)
    avg_val = sum(processed) / len(processed)
    peak = max(processed)
    
    return final

# Main execution
data_stream = [15, 30, -5, 45, 10, 0, 60]
baseline_diagnostic = calculate_baseline(preprocess_readings(data_stream))
final_score = calculate_final_score(data_stream)
print(f"Target result: {final_score}")