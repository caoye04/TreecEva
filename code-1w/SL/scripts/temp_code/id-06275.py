def analyze_distribution(data, threshold=0.1):
    n = len(data)
    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1
    
    frequencies = {k: v/n for k, v in counts.items()}
    
    # Irrelevant transformation (distractor)
    normalized_offsets = [abs(v - 0.5) * 2 for v in frequencies.values()]
    offset_sum = sum(normalized_offsets)

    significant_items = {k: v for k, v in frequencies.items() if v > threshold}
    
    # Dummy calculation with no impact
    dummy_variance = sum((x - 1/n)**2 for x in frequencies.values())

    weights = []
    for i in range(n):
        if data[i] in significant_items:
            weights.append(frequencies[data[i]])
        else:
            weights.append(threshold / 2)
    
    # Slicing used here to take middle segment
    mid_section = weights[len(weights)//4 : 3*len(weights)//4]
    adjusted_weights = [w * 1.2 for w in mid_section]
    
    padding = [0.01] * (4 - len(adjusted_weights) % 4) if len(adjusted_weights) % 4 != 0 else []
    padded_weights = adjusted_weights + padding
    
    # Group into chunks of 4 (basic grouping)
    grouped = [padded_weights[i:i+4] for i in range(0, len(padded_weights), 4)]
    
    final_weights = []
    for group in grouped:
        if len(group) == 4:
            # Sum of squares as transformation
            transformed = sum(x**2 for x in group)
            final_weights.append(transformed)
    
    return final_weights


def calculate_entropy(weights):
    from math import log2
    entropy = 0.0
    total = sum(weights)
    for w in weights:
        p = w / total
        if p > 0:
            entropy -= p * log2(p)
    return round(entropy, 4)

# Main execution
raw_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]

# Distractor computation
shadow_copy = raw_data[::-1]
duplicate_counts = {x: shadow_copy.count(x) for x in set(shadow_copy)}

# Actual processing path
processed_weights = analyze_distribution(raw_data)

# Key statement
total_entropy = calculate_entropy(processed_weights)

# Additional irrelevant state tracking
tracking_log = []
for idx, val in enumerate(processed_weights):
    tracking_log.append(f"Item{idx}:{val:.3f}")

Result: {total_entropy}