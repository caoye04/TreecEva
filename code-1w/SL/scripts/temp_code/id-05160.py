def analyze_distribution(data, threshold=100):
    count_high = 0
    cumulative = 0
    temp_vals = []

    for val in data:
        if val > threshold:
            count_high += 1
            cumulative += val
        temp_vals.append(val * 0.1)  # Irrelevant transformation

    avg_high = cumulative / count_high if count_high > 0 else 0
    return avg_high, set(temp_vals)


def calculate_entropy(values):
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            prob = v / total
            entropy -= prob * (prob ** 0.5)  # Simplified pseudo-entropy
    return entropy

# Simulate sensor readings over time
readings = [23, 85, 102, 45, 133, 78, 201, 67]

# Extract high-frequency events
high_freq, normalized_set = analyze_distribution(readings, threshold=90)

# Fictitious calibration offset (not used in final result)
calibration_factor = sum(r ** 0.2 for r in readings if r < 80)

duplicates_removed = list(set(readings))
duplicates_removed.sort()

# Incoming and outgoing flow simulation
incoming = [x for x in duplicates_removed if x > high_freq - 50]
outgoing = [x // 2 for x in duplicates_removed if x % 2 == 0]

# Misleading statistical summary
summary_stats = {
    'max_in': max(incoming) if incoming else 0,
    'min_out': min(outgoing) if outgoing else 0,
    'range': len(range(min(outgoing), max(incoming))) if outgoing and incoming else 0
}

# Core computation: net flow calculation
net_flow = calculate_net_flow(incoming, outgoing)

# Red herring: unused complex structure
structure_map = {i: {'val': v, 'squared': v**2, 'root': v**0.5} for i, v in enumerate(incoming)}

# Final output
print(f"Result: {net_flow}")

def calculate_net_flow(in_list, out_list):
    base_flow = sum(in_list)
    adjustment = 0
    
    for item in out_list:
        if item > 50:
            adjustment += item * 0.8
        elif item > 20:
            adjustment += item * 0.4
        else:
            adjustment += item * 0.1
    
    # Apply non-linear correction factor based on length parity
    if len(in_list) % 2 == 0:
        correction = 1.1
    else:
        correction = 0.9
    
    result = (base_flow - adjustment) * correction
    
    # Dead code branch - never executed due to data
    if len(out_list) > 20:
        result *= 0.95  # This does not run
    
    return int(result)

# Reorder function definition to create slight confusion (but valid in Python)
incoming = [x for x in duplicates_removed if x > high_freq - 50]
outgoing = [x // 2 for x in duplicates_removed if x % 2 == 0]