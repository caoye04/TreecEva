from itertools import combinations

def analyze_system_efficiency(values, weights):
    # Irrelevant helper: computes weighted sum (not used in final result)
    weighted = sum(v * w for v, w in zip(values, weights))
    return weighted / len(values) if values else 0

def generate_diagnostic_pairs(data):
    # Creates pairs but only some are used later
    return list(combinations(data, 2))

def calculate_entropy(seq):
    # Unused complexity: calculates entropy of a sequence
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

def analyze_stability(metrics, thresholds):
    # Core logic begins
    temp_buffer = []
    for m in metrics:
        if m > thresholds[0]:
            temp_buffer.append(m * 1.1)
        elif m < thresholds[1]:
            temp_buffer.append(m * 0.9)
        else:
            temp_buffer.append(m)
    
    # Secondary adjustment based on trend
    adjusted = []
    for i, val in enumerate(temp_buffer):
        if i > 0 and temp_buffer[i] < temp_buffer[i-1]:
            adjusted.append(val * 1.05)
        else:
            adjusted.append(val * 0.98)
    
    # Tertiary filtering: only values above baseline survive
    baseline = sum(metrics) / len(metrics)
    filtered = [v for v in adjusted if v > baseline]
    
    # Distractor: unused aggregation
    peak = max(adjusted) if adjusted else 0
    avg_filtered = sum(filtered) / len(filtered) if filtered else 0
    
    # Final score computation (this is the answer)
    stability_factor = 0.9
    equilibrium_score = int(avg_filtered * stability_factor)
    
    # Dead code path (never reached in normal execution)
    if False:
        fallback = analyze_system_efficiency(metrics, [1]*len(metrics))
        equilibrium_score = int(fallback)
    
    return equilibrium_score

# Main execution
metrics = [12, 15, 10, 18, 14, 16, 11]
thresholds = [13, 11]

# Unused variables and red herrings
weights = [0.2, 0.1, 0.15, 0.25, 0.1, 0.1, 0.1]
diag_pairs = generate_diagnostic_pairs(metrics)
system_efficiency = analyze_system_efficiency(metrics, weights)
entropy_value = calculate_entropy([1, 2, 2, 3, 3, 3])

# Key statement
equilibrium_score = analyze_stability(metrics, thresholds)

print(f"Result: {equilibrium_score}")