import math

def analyze_throughput(data_stream):
    # Irrelevant helper function (dead code path)
    return sum(x ** 0.5 for x in data_stream if x > 10)

def validate_checksum(sequence):
    # Distractor: looks important but unused in critical path
    return sum(sequence) % 256 == sequence[-1]

def compute_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return round(entropy, 4)

def extract_signal_peaks(signal_data, threshold=0.75):
    peaks = []
    for i in range(1, len(signal_data) - 1):
        if signal_data[i] > threshold and signal_data[i] > signal_data[i-1] and signal_data[i] > signal_data[i+1]:
            peaks.append(i)
    return peaks[:3]  # Only top 3 peak indices

def transform_coordinates(grid_points):
    # Unused transformation logic — red herring
    transformed = []
    for x, y in grid_points:
        r = math.sqrt(x*x + y*y)
        theta = math.atan2(y, x)
        transformed.append((r, theta))
    return transformed

def slice_diagnostic_window(log_entries, window_size=8):
    # Slicing operation (required language feature)
    if len(log_entries) < window_size:
        return log_entries
    mid = len(log_entries) // 2
    return log_entries[mid - window_size//2 : mid + window_size//2]

def evaluate_stability_factor(readings):
    # Complex but partially irrelevant computation
    filtered = [x for x in readings if 50 < x < 150]
    base_avg = sum(filtered) / len(filtered) if filtered else 0
    variance = sum((x - base_avg) ** 2 for x in filtered) / len(filtered) if filtered else 0
    return base_avg * (1 + math.exp(-variance / 100))

def aggregate_metrics(slices, log):
    # Core logic begins here — key function with multiple steps
    
    # Step 1: Extract relevant diagnostic windows using slicing
    critical_segment = slice_diagnostic_window(log, 6)
    
    # Step 2: Compute entropy on a subset (slicing again)
    segment_subset = critical_segment[1:-1]  # Remove first and last
    entropy_score = compute_entropy(segment_subset)
    
    # Step 3: Analyze network slice utilization
    utilization_rates = []
    for s in slices:
        rate = s['load'] / s['capacity']
        utilization_rates.append(rate)
    
    # Step 4: Determine high-load slices
    overloaded = [u for u in utilization_rates if u > 0.8]
    overload_count = len(overloaded)
    
    # Step 5: Apply decay factor based on entropy
    decay_factor = math.cos(entropy_score)  # Can be negative
    adjusted_overload = overload_count * decay_factor
    
    # Step 6: Use bit manipulation to encode state (bitwise operation)
    state_flag = 0
    if overload_count > 2:
        state_flag |= 1 << 3
    if entropy_score > 1.5:
        state_flag |= 1 << 1
    if adjusted_overload > 1.0:
        state_flag |= 1
    
    # Step 7: Aggregate multiple metrics into final score
    raw_sum = sum(utilization_rates)
    peak_load = max(utilization_rates)
    stability_hint = evaluate_stability_factor([int(x*100) for x in utilization_rates])
    
    # Step 8: Final diagnostic calculation (key result)
    final_diagnostic = int((raw_sum * 100) + (peak_load * 50) - (overload_count * 20) + (state_flag * 5))
    
    # Irrelevant printing (distraction)
    print(f"Debug: Stability hint = {stability_hint}")
    
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    
    # Simulated network slices (dictionary usage)
    network_slices = [
        {'id': 'S1', 'load': 85, 'capacity': 100},
        {'id': 'S2', 'load': 95, 'capacity': 100},
        {'id': 'S3', 'load': 60, 'capacity': 100},
        {'id': 'S4', 'load': 88, 'capacity': 100},
        {'id': 'S5', 'load': 92, 'capacity': 100},
        {'id': 'S6', 'load': 70, 'capacity': 100},
    ]
    
    # Diagnostic log with numeric entries (simulated sensor readings)
    diagnostics_log = [120, 85, 90, 110, 95, 130, 105, 115, 100, 90, 80, 125]
    
    # Dead variables — misleading intermediate results
    checksum_valid = validate_checksum([1, 2, 3, 4, 10])  # Always False
    coordinate_grid = [(1,1), (2,3), (3,2), (4,4)]
    transformed_coords = transform_coordinates(coordinate_grid)
    
    # Signal analysis on unrelated data — distractor
    signal_input = [0.1, 0.8, 0.6, 0.9, 0.3, 0.75, 0.85]
    strong_peaks = extract_signal_peaks(signal_input, threshold=0.7)
    
    # Critical statement: this produces the answer
    final_diagnostic = aggregate_metrics(network_slices, diagnostics_log)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")