import itertools

# System diagnostics simulation with sensor fusion and error correction

def generate_calibration_sequence(base_offset):
    sequence = []
    for i in range(5):
        val = (i ** 2 + base_offset) % 7
        if val % 3 == 0:
            sequence.append(val + 2)
        else:
            sequence.append(val)
    return sequence

def detect_anomalies(data_stream):
    anomalies = []
    for i in range(1, len(data_stream)):
        if abs(data_stream[i] - data_stream[i-1]) > 2:
            anomalies.append(i)
    return set(anomalies)

def apply_filter(signal, kernel_size=3):
    smoothed = []
    pad = kernel_size // 2
    extended = [signal[0]] * pad + signal + [signal[-1]] * pad
    for i in range(len(signal)):
        window = extended[i:i + kernel_size]
        smoothed.append(sum(window) / len(window))
    return smoothed

def compute_entropy(values):
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def evaluate_stability(readings):
    if len(readings) < 2:
        return True
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return max(diffs) <= 1.5

# Irrelevant auxiliary function - dead code path (distractor)
def deprecated_normalization(vec):
    mag = sum(x**2 for x in vec) ** 0.5
    return [x/mag for x in vec] if mag else vec

# Another decoy: historical threshold logic not used in main flow
def get_legacy_threshold(version):
    thresholds = {1: 0.8, 2: 0.75, 3: 0.9}
    return thresholds.get(version, 0.85)

# Misleading intermediate diagnostic flag (red herring)
potential_drift_detected = False
baseline_reference = [1, 1, 2, 3, 5]

# Primary processing pipeline
base_offset = 11
raw_sequence = generate_calibration_sequence(base_offset)

# Apply filter to smooth noise (relevant step)
filtered_sequence = apply_filter(raw_sequence)

# Detect jump anomalies in raw signal (used later)
anomaly_positions = detect_anomalies(raw_sequence)

# Simulate fault injection flags based on position parity (mixed relevance)
fault_flags = {idx for idx in range(len(raw_sequence)) if idx % 2 == 1}
fault_flags = fault_flags.union(anomaly_positions)  # Combine fault sources

# Compute auxiliary metrics for logging (distractor computation)
metric_snapshot = {
    'length': len(filtered_sequence),
    'mean': sum(filtered_sequence) / len(filtered_sequence),
    'peak': max(filtered_sequence),
    'entropy': compute_entropy([round(x) for x in filtered_sequence])
}

# Unused health score (red herring)
system_health_score = 100 - len(anomaly_positions) * 10

# Conditional branch with early return possibility (not triggered)
if len(anomaly_positions) > 10:
    final_diagnostic = -1
else:
    # Main logic: process metrics using set operations and transformations
    def process_metrics(seq, faults):
        # Round filtered values to integers
        int_seq = [round(x) for x in seq]
        
        # Create paired sliding windows using itertools
        pairs = list(itertools.pairwise(int_seq))
        
        # Count directional transitions
        increases = sum(1 for a, b in pairs if b > a)
        decreases = sum(1 for a, b in pairs if b < a)
        
        # Use set difference to isolate fault-affected positions
        valid_indices = set(range(len(int_seq))) - faults
        valid_values = {int_seq[i] for i in valid_indices}
        
        # Compute diagnostic signature
        base_score = sum(valid_values)
        adjustment = increases - decreases
        
        # Apply non-linear transformation on adjustment if certain condition
        if len(valid_values) in {3, 4}:
            adjustment = abs(adjustment) ** 2 * (-1 if adjustment < 0 else 1)
        
        # Final diagnostic calculation
        result = base_score * 3 + adjustment
        
        # Dead code branch (never reached due to structure)
        if result < 0:
            result = abs(result) + 100  # This logic is irrelevant
            
        return result

    # Execute critical statement
    final_diagnostic = process_metrics(filtered_sequence, fault_flags)

# Log unused stability check (distractor)
stability_status = evaluate_stability(filtered_sequence)

# Print target result
print(f"Result: {final_diagnostic}")