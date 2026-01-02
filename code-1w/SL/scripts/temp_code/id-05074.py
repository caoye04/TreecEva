def analyze_readings(readings):
    # Irrelevant transformation: converts to percentage but not used in final logic
    normalized = [r * 0.01 for r in readings if r > 0]
    filtered = [r for r in readings if 50 <= r <= 150]  # Only valid physiological range
    return sum(filtered) // len(filtered) if filtered else 0

# Simulated sensor data from multiple sources
temp_readings = [98, 102, 110, 45, 120, 130, 140, 60]
humidity_readings = [30, 35, 40, 45, 50, 55, 60]  # Unused red herring

# Primary health metrics
def compute_stability_index(data):
    if len(data) < 3:
        return 0
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    avg_diff = sum(diffs) / len(diffs)
    return int(100 - avg_diff)  # Higher is more stable

# Bit manipulation for error detection (simulated)
def detect_anomalies(values):
    checksum = 0
    for v in values:
        checksum ^= v  # XOR into checksum
    return bin(checksum).count('1') % 2  # Parity check, result unused

# Decoy function that looks important but isn't called in critical path
def legacy_calibrate(x):
    return (x << 2) + (x >> 1)

# Main processing pipeline
def process_metrics(data, limits):
    baseline = analyze_readings(data)
    
    # Distractor variables
    temp_offset = 0.75
    adjustment_factor = 1.05
    shadow_buffer = [x * adjustment_factor for x in data]  # Computed but unused
    
    # Real logic begins: stability analysis
    stability = compute_stability_index(data)
    
    # Set operations simulating diagnostic flags
    high_values = {x for x in data if x > limits['upper']}
    low_values = {x for x in data if x < limits['lower']}
    critical_set = high_values | low_values  # Union of extremes
    
    # Misleading conditional block (executes but doesn't affect output)
    if len(critical_set) > 2:
        fallback_mode = True
        recovery_attempt = len(data) // 2

    # Key logic: only stability and baseline matter
    score_modifier = -5 if detect_anomalies(data) else 0  # Calls but adds no real effect due to fixed parity
    
    # Sorting used for median calculation
    sorted_data = sorted(data)
    mid = len(sorted_data) // 2
    median_value = (sorted_data[mid] + sorted_data[~mid]) // 2  # Bitwise not for symmetry
    
    # Final computation chain
    raw_diagnostic = baseline + stability
    adjusted_diagnostic = raw_diagnostic * 0.9
    final_diagnostic = int(adjusted_diagnostic) + score_modifier
    
    # Dead code path - never executed under current logic
    if False:
        final_diagnostic = max(final_diagnostic, 50)
    
    return final_diagnostic

# Configuration dictionary with plausible decoys
thresholds = {
    'upper': 135,
    'lower': 70,
    'tolerance': 5.0,
    'gain': 1.2
}

# Actual sensor input used in computation
health_data = [95, 98, 101, 103, 100, 97, 102, 99]

# Trigger key statement
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")