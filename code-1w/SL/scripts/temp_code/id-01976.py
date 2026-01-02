import itertools

# Simulated sensor data processing with red herrings and multiple transformations
def collect_sensor_readings():
    raw_signals = [1.2, 3.7, 2.5, 8.1, 4.3, 9.0, 6.4, 7.2]
    offset_correction = 0.8
    corrected = [x - offset_correction for x in raw_signals]
    return corrected

# Irrelevant diagnostic function (decoy)
def compute_health_score(data):
    if len(data) == 0:
        return 0
    return sum(x ** 0.5 for x in data if x > 5) * 1.5

# Another decoy: network latency simulation (unused)
def simulate_propagation_delay(nodes):
    delay_map = {}
    for i, node in enumerate(nodes):
        delay_map[node] = (i * 1.7) % 3.3
    return delay_map

# Core transformation: apply windowed filter and extract peaks
def preprocess_stream(signal):
    window_size = 3
    smoothed = []
    for i in range(len(signal) - window_size + 1):
        window = signal[i:i+window_size]
        avg = sum(window) / window_size
        smoothed.append(round(avg, 2))
    # Extract rising edges
    rising_edges = []
    for i in range(1, len(smoothed)):
        if smoothed[i] > smoothed[i-1] + 0.5:
            rising_edges.append(i)
    return smoothed, rising_edges

# Misleading utility: checksum calculation (not used in final path)
def calculate_frame_checksum(sequence):
    checksum = 0
    for val in sequence:
        checksum ^= int(val * 10)  # bitwise distraction
    return checksum % 100

# Key pattern analysis using itertools and slicing
def analyze_pattern(processed, pattern_key):
    # Use of itertools: group consecutive indices
    grouped = [list(group) for k, group in itertools.groupby(pattern_key, lambda x: x - pattern_key.index(x))]
    flat_groups = [item for group in grouped for item in group]
    
    # Slicing operation: analyze every second element from midpoint
    mid = len(flat_groups) // 2
    sliced_view = flat_groups[mid:mid+4]  # focus on central slice
    
    # Actual logic contribution: product of differences
    if len(sliced_view) < 2:
        return 0
    product = 1
    for i in range(1, len(sliced_view)):
        diff = abs(sliced_view[i] - sliced_view[i-1])
        product *= (diff + 1)
    return product

# Dead code path: thermal calibration (never called)
def calibrate_thermal_drift(samples):
    baseline = samples[0]
    drift_adjusted = [s - baseline * 0.05 for s in samples]
    return drift_adjusted

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect and correct sensor data
    readings = collect_sensor_readings()
    
    # Step 2: Preprocess to detect signal trends (produces two outputs)
    filtered_data, detected_peaks = preprocess_stream(readings)
    
    # Step 3: Generate auxiliary key sequence using peak positions
    extended_peaks = detected_peaks + [p + 10 for p in detected_peaks]
    key_sequence = [x for x in extended_peaks if x % 2 == 1]  # keep only odd-valued indices
    
    # Step 4: Transform main data via cumulative operations (relevant)
    transformed_data = []
    running_total = 0
    for val in filtered_data:
        running_total += val * 1.1
        transformed_data.append(running_total)
    
    # Step 5: Apply masking based on dummy condition (partially dead)
    mask_threshold = 5.5
    masked_data = [x for x in transformed_data if x > mask_threshold]  # used in decoy only
    
    # Step 6: Compute irrelevant health score (red herring)
    health_metric = compute_health_score(masked_data)
    
    # Step 7: Final analysis on core pattern (ACTUAL ANSWER PATH)
    final_diagnostic = analyze_pattern(transformed_data, key_sequence)
    
    # Print result
    print(f"Result: {final_diagnostic}")