import math

# Simulated bio-signal processing system
# Complex chain with heavy distractions and red herrings

def analyze_waveform(signal_data):
    if not signal_data:
        return 0
    
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(signal_data) for x in signal_data]
    filtered = [x for x in normalized if x > 0.1]
    envelope = sum(filtered) * 1.75

    # Misleading transformation chain
    temp_buffer = []
    for val in filtered:
        temp_buffer.append(math.sin(val * math.pi))
    
    # Decoy metric
    spectral_tilt = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0

    # Actual relevant logic buried here
    peak_count = 0
    for i in range(1, len(signal_data) - 1):
        if signal_data[i] > signal_data[i-1] and signal_data[i] > signal_data[i+1]:
            peak_count += 1

    return peak_count


def generate_checksum(sequence):
    # Complex-looking but irrelevant checksum
    checksum = 0
    for i, s in enumerate(sequence):
        checksum ^= (ord(s) << (i % 4))
    return checksum % 1000


def evaluate_stability(ratio_sequence):
    # Another misleading stability analysis (dead path)
    if len(ratio_sequence) < 2:
        return 0.0
    variance = sum((x - sum(ratio_sequence)/len(ratio_sequence))**2 for x in ratio_sequence)
    return round(variance, 3)


def compute_harmonic_weight(data):
    # Distractor: harmonic weighting with no impact
    total = 0.0
    for i, x in enumerate(data, 1):
        total += x / i if i % 2 == 0 else x * 0.5
    return total


def derive_entropy(values):
    # Red herring entropy calculation
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    entropy = 0.0
    n = len(values)
    for count in freq_map.values():
        p = count / n
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 4)


def process_metrics(signature, thresholds):
    base_score = 0
    
    # Key processing steps (buried in noise)
    critical_peaks = signature.get('peaks', [])
    avg_peak = sum(critical_peaks) / len(critical_peaks) if critical_peaks else 0
    
    # Conditional expression - required python feature
    adjustment_factor = 1.5 if avg_peak > thresholds['peak_threshold'] else 0.8
    
    # Real computation chain
    base_score += len(critical_peaks) * 17
    base_score += int(avg_peak * adjustment_factor)
    
    # Secondary metric
    rhythm_sequence = signature.get('rhythm', [])
    if rhythm_sequence:
        valid_intervals = [x for x in rhythm_sequence if x > 0]
        if valid_intervals:
            mean_interval = sum(valid_intervals) / len(valid_intervals)
            base_score += int(mean_interval / 5)

    # Tertiary influence
    mode_flag = signature.get('mode', 'A')
    multiplier = {'A': 2, 'B': 3, 'C': 1}.get(mode_flag, 1)
    
    # Final transformation using conditional expression
    final_value = base_score * multiplier if mode_flag != 'C' else base_score // 2
    
    return final_value

# --- Main Execution with Heavy Interference ---

# Irrelevant data structures (distractors)
data_log = [
    {'timestamp': 1678886400, 'type': 'calibration', 'value': 987},
    {'timestamp': 1678886500, 'type': 'noise_floor', 'value': 102},
    {'timestamp': 1678886600, 'type': 'sync_pulse', 'value': 450}
]

auxiliary_keys = ['X7G', 'K9P', 'M2Q']
key_weights = {k: (i+1)*113 for i, k in enumerate(auxiliary_keys)}
crypto_trace = [generate_checksum(k) for k in auxiliary_keys]

# Simulated sensor inputs (mix of real and fake)
raw_signal = [12, 8, 23, 45, 31, 76, 88, 65, 92, 77, 101, 89, 67, 112, 98]
rhythm_pattern = [120, 118, 122, 0, 119, 121]  # Zero is outlier

# Fake diagnostic metrics
diag_matrix = [[i*j + 2 for j in range(4)] for i in range(4)]
matrix_sum = sum(sum(row) for row in diag_matrix)
stability_index = evaluate_stability([1.2, 1.5, 1.3, 1.7, 1.4])
harmonic_load = compute_harmonic_weight([4, 8, 15, 16, 23, 42])

# Extract meaningful features from signal
peak_count = analyze_waveform(raw_signal)

# Construct health signature using real and irrelevant fields
health_signature = {
    'peaks': [p for p in raw_signal if p > 75],           # Relevant
    'rhythm': [r for r in rhythm_pattern if r > 0],        # Relevant
    'mode': 'A',                                          # Relevant
    'checksum': crypto_trace[0],                          # Distractor
    'entropy': derive_entropy(raw_signal),              # Distractor
    'buffer_size': matrix_sum,                           # Distractor
    'stability': stability_index                         # Distractor
}

# Threshold map (only one key matters)
threshold_map = {
    'peak_threshold': 80,
    'decay_limit': 0.75,
    'window_size': 5
}

# Critical execution point
final_diagnostic = process_metrics(health_signature, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")