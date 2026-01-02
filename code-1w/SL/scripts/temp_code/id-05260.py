import itertools

# Simulated sensor data processing pipeline with diagnostic checks
raw_readings = [0.8, 1.2, -0.5, 3.1, 2.7, -1.3, 0.9, 1.1]
timestamps = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]

def apply_filter(data, method='moving_avg'):
    # Irrelevant filtering methods (distractor)
    if method == 'median':
        return sorted(data)[len(data)//2]
    elif method == 'none':
        return data
    # Actual moving average filter
    filtered = []
    window = 3
    for i in range(len(data) - window + 1):
        filtered.append(sum(data[i:i+window]) / window)
    return filtered

def detect_anomalies(values):
    # Dead code path - never actually used in final logic
    thresholds = {'low': -1.0, 'high': 2.5}
    anomalies = []
    for v in values:
        if v < thresholds['low'] or v > thresholds['high']:
            anomalies.append(v)
    return anomalies

def generate_combinations(data):
    # Distractor: generates unused combinatorial data
    pairs = list(itertools.combinations(data, 2))
    sums = [a + b for a, b in pairs]
    return sums  # Never used

def compute_entropy(data):
    # Misleading intermediate calculation - looks important but unused
    from math import log2
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = -sum((count/total) * log2(count/total) for count in freq.values())
    return round(entropy, 4)

def shift_cipher(sequence, key=3):
    # Decoy function: operates on integers but irrelevant to main logic
    shifted = [(x * 7 + key) % 256 for x in range(len(sequence))]
    return shifted

def extract_peaks(signal, min_magnitude=1.0):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1] and abs(signal[i]) >= min_magnitude:
            peaks.append((i, signal[i]))
    return peaks

def validate_timing(stamps):
    # Unused validation logic (distractor)
    intervals = [stamps[i+1] - stamps[i] for i in range(len(stamps)-1)]
    return all(t == 1 for t in intervals)

def reconstruct_phase(readings):
    # Complex transformation that feeds into actual computation
    adjusted = [r * 1.75 for r in readings]
    phased = []
    for i, val in enumerate(adjusted):
        phase_shift = (val ** 2) * ((-1) ** i)
        phased.append(phase_shift)
    return phased

def integrate_signal(phased_data):
    # Core relevant function: integrates signal using alternating signs
    integral = 0.0
    for j in range(len(phased_data)):
        if j % 2 == 0:
            integral += phased_data[j] * 0.9
        else:
            integral -= phased_data[j] * 0.4
    return round(integral, 6)

def analyze_signal(frames):
    # Main analysis function that combines multiple steps
    baseline = sum(frames) / len(frames)
    normalized = [f - baseline for f in frames]
    weighted = [n * (1.1 + i*0.05) for i, n in enumerate(normalized)]
    aggregate = sum(weighted)
    peak_info = extract_peaks(weighted, min_magnitude=0.5)
    peak_count_score = len(peak_info) * 100
    # Final diagnostic is based on integrated signal + peak adjustment
    integration_result = integrate_signal(frames)
    final_score = integration_result * 1000 + peak_count_score
    return int(final_score)

# Irrelevant preprocessing chain
filtered_readings = apply_filter(raw_readings, 'moving_avg')
entropy_value = compute_entropy(filtered_readings)  # Computed but unused
anomaly_list = detect_anomalies(raw_readings)  # Computed but unused
cipher_trace = shift_cipher(timestamps)  # Dead end
combinatorial_sums = generate_combinations(raw_readings[:4])  # Unused

# Relevant processing branch
phase_corrected = reconstruct_phase(filtered_readings)
processed_frames = [round(x, 3) for x in phase_corrected]

# Key execution point
final_diagnostic = analyze_signal(processed_frames)

# Output the target result
print(f"Target result: {final_diagnostic}")