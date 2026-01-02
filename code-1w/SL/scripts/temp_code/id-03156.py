import math

# Simulated sensor array diagnostics with mixed computational paradigms
def collect_sensor_readings():
    raw_signals = [i * 1.5 + 2.7 for i in range(12)]
    offset = 0.3
    calibrated = [round(x + offset, 2) for x in raw_signals]
    return calibrated

# Irrelevant auxiliary function - dead code path (distractor)
def legacy_normalization(data):
    if not data:
        return []
    max_val = max(data)
    return [x / max_val for x in data]  # Unused in main logic

# Signal processing with bit manipulation red herring
def enhance_resolution(signal_list):
    amplified = []
    for val in signal_list:
        base = int(val * 100)
        # Bit manipulation distraction (appears important but only used once)
        processed = (base << 1) | 1  
        amplified.append(processed / 100.0)
    return amplified

# Decoy function using set operations (misleading relevance)
def detect_anomalies(readings):
    anomalies = set()
    history = set([round(x, 1) for x in readings])
    expected_range = set(range(5, 20))
    unexpected = history ^ expected_range  # Symmetric difference - irrelevant result
    for val in readings:
        if val > 15 and round(val) % 3 == 0:
            anomalies.add(round(val, 1))
    return anomalies  # Never actually used

# Threshold mapping with combinatorics distractor
def generate_threshold_map(levels=4):
    # Complex-looking but mostly irrelevant computation
    combos = []
    for i in range(levels):
        for j in range(i+1, levels):
            combos.append((i, j, math.sqrt(i**2 + j**2)))  # Unused combinations
    
    # Actual meaningful thresholds
    critical = {i: 5.0 + i*1.8 for i in range(levels)}
    # Add decoy keys
    critical['debug_mode'] = True
    critical['version'] = '2.1'
    return critical

# Core analysis logic obscured by context
def filter_noise(data, method='median'):
    size = len(data)
    sorted_data = sorted(data)
    if method == 'median':
        mid = size // 2
        median_val = sorted_data[mid] if size % 2 else (sorted_data[mid-1] + sorted_data[mid]) / 2
        return [x for x in data if x >= median_val - 1.5]  # Filtering operation
    return data

# Primary transformation with list comprehension and filtering
def integrate_channels(primary, secondary):
    # Simulate multi-channel fusion
    if len(primary) != len(secondary):
        padded = primary[:len(secondary)]
    else:
        padded = primary
    
    # Real processing step embedded among distractions
    gain_factor = 1.75
    combined = [p * gain_factor + s for p, s in zip(padded, secondary)]
    return [x for x in combined if x > 10]  # List comprehension filter

# Final diagnostic with multiple dependencies
def analyze_signal(dataset, thresholds):
    baseline = sum(dataset) / len(dataset)
    fluctuation = sum(abs(dataset[i] - dataset[i-1]) for i in range(1, len(dataset)))
    
    # Critical decision logic
    level_key = len(dataset) % 4
    activation_threshold = thresholds.get(level_key, 8.0)
    
    # Red herring: complex bit operation on float (converted to int)
    magic_seed = int(baseline) ^ int(fluctuation)
    adjustment = (magic_seed & 0b111) / 10.0  # Use only lower 3 bits
    
    # Determine final state
    if baseline + adjustment > activation_threshold:
        diagnostic_code = 1000 + int(fluctuation)
    else:
        diagnostic_code = 200 + int(baseline)
    
    return diagnostic_code

# Irrelevant sorting routine (distractor)
def sort_diagnostics(entries):
    entries_with_keys = [(entry, str(entry)[::-1]) for entry in entries]
    entries_with_keys.sort(key=lambda x: x[1])  # Sort by reversed string
    return [e[0] for e in entries_with_keys]

# Unused data structure transformation
complex_lookup = {
    'modes': ['A', 'B', 'C'],
    'calibration': {chr(65+i): i*0.5 for i in range(10)},
    'flags': [False, False, True]
}

# Main execution flow
sensor_data = collect_sensor_readings()  # Initial data collection
enhanced_data = enhance_resolution(sensor_data)  # Apply resolution boost
noise_filtered = filter_noise(enhanced_data)  # Remove low-level noise

# Generate secondary synthetic channel (for integration)
synthetic_reference = [math.sin(i * 0.5) * 4.0 for i in range(len(noise_filtered))]

# Apply integration
integrated_output = integrate_channels(noise_filtered, synthetic_reference)

# Generate threshold parameters (contains decoys)
threshold_config = generate_threshold_map(4)

# Detect anomalies - result discarded (dead call with side effect of misdirection)
detect_anomalies(integrated_output)

# Final analysis - key statement
final_diagnostic = analyze_signal(integrated_output, threshold_config)

print(f"Result: {final_diagnostic}")