import math

# Simulated sensor array diagnostics with signal processing and red herrings
def collect_sensor_data():
    raw_values = [i * 1.5 + (i % 3) for i in range(18)]
    offset = 4.2
    adjusted = [v + offset for v in raw_values]
    return adjusted

def generate_frequency_grid(base_freq=2.1):
    # Irrelevant frequency grid generation (dead-end computation)
    grid = []
    for i in range(6):
        for j in range(6):
            grid.append(base_freq * (i + j) ** 1.1)
    return grid

def compute_entropy(signal):
    # Unused entropy calculation (distractor)
    total = sum(abs(x) for x in signal)
    if total == 0:
        return 0.0
    probs = [abs(x) / total for x in signal]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def validate_checksum(sequence):
    # Decoy validation not used in main logic
    chk = 0
    for idx, val in enumerate(sequence):
        chk ^= int(val) % 7
    return chk == 3

def filter_anomalies(data, sensitivity=0.85):
    mean_val = sum(data) / len(data)
    deviances = [(x - mean_val) ** 2 for x in data]
    variance = sum(deviances) / len(deviances)
    std_dev = math.sqrt(variance)
    lower = mean_val - sensitivity * std_dev
    upper = mean_val + sensitivity * std_dev
    filtered = [x for x in data if lower <= x <= upper]
    # Returns cleaned data but also computes irrelevant stats
    anomaly_count = len(data) - len(filtered)
    suppression_ratio = anomaly_count / len(data) if data else 0
    return filtered  # suppression_ratio is unused

def build_index_mapping(keys):
    # Distractor: builds a dictionary that's never used
    index_map = {}
    for idx, key in enumerate(keys):
        index_map[key] = idx * 2 + (idx % 4)
    return index_map

def calculate_phase_shift(elements, phase_base=0.5):
    # Complex-looking but irrelevant transformation
    shifts = []n    for i, e in enumerate(elements):
        shift = phase_base * math.sin(i * 0.4) * math.cos(e * 0.05)
        shifts.append(shift)
    return shifts

def analyze_signal_patterns(readings, config_map):
    # Core relevant logic begins here
    segment_size = config_map['window']
    tolerance = config_map['tolerance']
    
    # Break readings into windows using enumerate and zip
    segments = []
    for i in range(0, len(readings) - segment_size + 1, segment_size // 2):
        window = readings[i:i + segment_size]
        segments.append(window)
    
    # Compute rolling metrics
    coherence_scores = []
    for seg in segments:
        if len(seg) < 2:
            continue
        diffs = [seg[j+1] - seg[j] for j in range(len(seg)-1)]
        abs_diffs = [abs(d) for d in diffs]
        coherence = sum(1 for ad in abs_diffs if ad < tolerance) / len(abs_diffs)
        coherence_scores.append(coherence)
    
    # Final aggregation
    if not coherence_scores:
        return 0.0
    avg_coherence = sum(coherence_scores) / len(coherence_scores)
    
    # Key transformation to integer diagnostic code
    diagnostic_code = int(avg_coherence * 10000)
    
    # Injecting meaningful distractors below
    dummy_pairs = list(zip(readings[::3], readings[1::3]))  # Uses zip, not critical
    enumerated_deltas = []
    for idx, val in enumerate(segments[0] if segments else [0]):
        enumerated_deltas.append((idx, val * 0.1))  # Uses enumerate, irrelevant
    
    # Final result derived from core logic
    return diagnostic_code

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect real data
    collected_readings = collect_sensor_data()
    
    # Step 2: Generate several irrelevant structures
    freq_grid = generate_frequency_grid()
    entropy_metric = compute_entropy(collected_readings)
    checksum_valid = validate_checksum([int(x) for x in collected_readings[::4]])
    
    # Step 3: Filter data (this affects the final input)
    cleaned_readings = filter_anomalies(collected_readings, sensitivity=0.92)
    
    # Step 4: Build unused mappings
    keys = ['A', 'B', 'C', 'D']
    unused_map = build_index_mapping(keys)
    phase_shifts = calculate_phase_shift(cleaned_readings)
    
    # Step 5: Create configuration (only this matters now)
    threshold_map = {
        'window': 5,
        'tolerance': 1.75
    }
    
    # Step 6: Critical analysis call
    final_diagnostic = analyze_signal_patterns(cleaned_readings, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")