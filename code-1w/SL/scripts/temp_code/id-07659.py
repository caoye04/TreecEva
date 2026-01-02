import itertools

# Simulated sensor array data from a distributed environmental monitoring system
def collect_sensor_readings():
    base_values = [23.4, 19.5, 27.8, 20.1, 31.2, 18.7, 24.3]
    adjustments = [0.3, -0.2, 0.5, 0.0, -0.4, 0.1, 0.2]
    return [base + adj for base, adj in zip(base_values, adjustments)]

# Legacy function - unused but looks relevant (red herring)
def legacy_normalization(data):
    mean_val = sum(data) / len(data)
    return [round((x - mean_val) / mean_val * 100, 2) for x in data]

# Irrelevant transformation chain (distractor)
def transform_coordinates(locations):
    lat_offset = 0.001
    lon_offset = -0.002
    adjusted = []
    for loc in locations:
        lat, lon = loc
        lat += lat_offset
        lon += lon_offset
        adjusted.append((round(lat, 4), round(lon, 4)))
        lat_offset *= -1.1
        lon_offset *= 1.1
    return adjusted

# Unused recursive checksum (dead code path)
def recursive_checksum(seq, index=0, acc=0):
    if index >= len(seq):
        return acc % 1000
    acc = (acc * 31 + seq[index]) % 10000
    return recursive_checksum(seq, index + 1, acc)

# Core logic disguised among distractions
def evaluate_stability_index(readings):
    filtered = [r for r in readings if 20.0 <= r <= 25.0]  # only stable-range sensors
    if not filtered:
        return 0.0
    avg_stable = sum(filtered) / len(filtered)
    variance = sum((r - avg_stable) ** 2 for r in readings) / len(readings)
    return round(avg_stable - variance * 0.5, 3)

# Complex conditional processing with decoy branches
def compute_thermal_gradient(temps):
    if len(temps) < 3:
        return 0
    
    # Decoy branch - never taken due to input size
    if any(t < 0 for t in temps):
        gradient = sum(temps[i+1] - temps[i] for i in range(len(temps)-1))
        return abs(gradient) * 100
    
    # Real computation
    sorted_temps = sorted(temps)
    q1 = sorted_temps[len(sorted_temps)//4]
    q3 = sorted_temps[3*len(sorted_temps)//4]
    iqr = q3 - q1
    return round(iqr * 1.5, 3)

# Main processing pipeline with multiple abstractions
def process_metrics(indicators, limits):
    # Step 1: Filter indicators within threshold bounds
    valid_pairs = [(val, th) for val, th in zip(indicators, limits) if val <= th * 1.1]
    
    # Step 2: Compute weighted contribution (only some elements count)
    weights = [0.8, 1.2, 0.9, 1.1, 1.0, 0.85, 0.95]
    contributions = []
    for i, (val, th) in enumerate(valid_pairs):
        if i % 2 == 0:  # Only even-indexed valid pairs contribute
            norm_val = val / th
            contributions.append(norm_val * weights[i])
    
    # Step 3: Aggregate using statistical transform
    if not contributions:
        base_score = 0.0
    else:
        base_score = sum(contributions) / len(contributions)
    
    # Step 4: Apply nonlinear correction based on dispersion
    squared_diffs = [(c - base_score) ** 2 for c in contributions]
    if squared_diffs:
        dispersion = (sum(squared_diffs) / len(squared_diffs)) ** 0.5
        final_adjustment = base_score * (1 - min(dispersion * 0.3, 0.25))
    else:
        final_adjustment = base_score
    
    # Step 5: Final mapping to diagnostic range (0-100 scale)
    return int(round(final_adjustment * 50))

# Orphaned utility function (irrelevant)
def generate_report_header(title, version='v1'):
    timestamp = "2023-11-05T10:30:00Z"
    header_lines = [
        f"=== {title.upper()} ===",
        f"Version: {version}",
        f"Generated: {timestamp}"
    ]
    return '\n'.join(header_lines)

# Simulate real-world deployment context
if __name__ == "__main__":
    # Primary data collection
    raw_readings = collect_sensor_readings()
    
    # Irrelevant coordinate grid (distractor)
    sensor_locations = [(34.0522, -118.2437), (40.7128, -74.0060), (47.6062, -122.3321),
                        (33.4484, -112.0740), (39.9526, -75.1652), (30.2672, -97.7431),
                        (38.9072, -77.0369)]
    adjusted_coords = transform_coordinates(sensor_locations)
    
    # Compute several intermediate metrics (some used, some not)
    stability_index = evaluate_stability_index(raw_readings)
    thermal_behavior = compute_thermal_gradient(raw_readings)
    
    # These look important but are discarded
    dummy_sequence = [ord(c) % 25 for c in "checkpoint"]
    legacy_normalized = legacy_normalization(raw_readings)
    checksum_value = recursive_checksum(dummy_sequence)  # Dead call
    
    # Key variables for final computation
    health_indicators = [
        stability_index * 2,           # derived from stable sensors
        thermal_behavior * 0.7,         # thermal pattern weight
        raw_readings[0],               # primary reference node
        raw_readings[2],               # secondary hotspot
        sum(raw_readings) / len(raw_readings),  # system average
        stability_index * 1.5,          # amplified stability
        thermal_behavior * 1.2          # extended thermal impact
    ]
    
    thresholds = [10.0, 25.0, 25.0, 30.0, 26.0, 12.0, 35.0]
    
    # Critical statement containing the answer
    final_diagnostic = process_metrics(health_indicators, thresholds)
    
    # Additional irrelevant output formatting (misleading)
    report_title = "Environmental Stability Diagnostic"
    header = generate_report_header(report_title, version='v2.1')
    
    # Output the target result as required
    print(f"Result: {final_diagnostic}")