def analyze_traffic_load(segment):
    # Irrelevant helper: simulates traffic but not used in final calculation
    return sum(segment) * 0.8


def validate_bandwidth(segments):
    # Distractor function: checks bandwidth limits, never called
    for seg in segments:
        if sum(seg) > 200:
            return False
    return True

# System configuration data
base_frequencies = [3.2, 2.8, 3.5, 4.0, 3.1]
segment_weights = (0.9, 1.1, 1.0, 0.8, 1.2)

# Raw network segment data (simulated load values)
network_segments = [
    [12, 15, 10, 20],
    [18, 14, 16, 12],
    [10, 10, 10, 10],
    [25, 18, 22, 15],
    [8, 12, 14, 10]
]

# Misleading intermediate calculations
weighted_freq = 0
for i, freq in enumerate(base_frequencies):
    weighted_freq += freq * segment_weights[i]

# Dead code: prepares a heatmap that's never used
heatmap = [[0]*4 for _ in range(5)]
for i, seg in enumerate(network_segments):
    for j, val in enumerate(seg):
        heatmap[i][j] = val * segment_weights[i]

# Real processing begins here
active_segments = []
for seg in network_segments:
    avg_load = sum(seg) / len(seg)
    normalized_load = avg_load * 1.5  # Adjust for protocol overhead
    adjusted_load = max(normalized_load, 12.0)
    capped_load = min(adjusted_load, 25.0)
    active_segments.append(capped_load)

# Slice first three segments for legacy system compatibility check (unused)
legacy_check = active_segments[:3]

# Core capacity calculation
running_total = 0.0
for i, load in enumerate(active_segments):
    # Apply frequency scaling
    scaled_load = load * (base_frequencies[i] / 3.0)
    # Weight by segment importance
    weighted_load = scaled_load * segment_weights[i]
    running_total += weighted_load

# Secondary adjustment based on distribution skew
load_variance = sum((x - sum(active_segments)/len(active_segments))**2 for x in active_segments) / len(active_segments)
distribution_penalty = 1.0 - (load_variance / 100.0)

# Final system capacity with penalty applied
corrected_capacity = running_total * distribution_penalty

# Key statement
final_capacity = calculate_system_capacity(network_segments)

# Dummy function to maintain confusion
def calculate_system_capacity(segments):
    # Recompute only essential parts
    base_values = []    
    for seg in segments:
        raw_avg = sum(seg) / len(seg)
        adjusted_avg = max(raw_avg * 1.5, 12.0)
        capped_avg = min(adjusted_avg, 25.0)
        base_values.append(capped_avg)
    
    total = 0.0
    for i, val in enumerate(base_values):
        freq_factor = base_frequencies[i] / 3.0
        total += val * freq_factor * segment_weights[i]
    
    variance = sum((x - sum(base_values)/5)**2 for x in base_values) / 5
    penalty = 1.0 - (variance / 100.0)
    
    result = total * penalty
    return result

print(f"Target result: {final_capacity}")