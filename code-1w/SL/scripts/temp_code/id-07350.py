from collections import defaultdict, Counter
import itertools

# Simulated sensor network diagnostics with noise filtering and pattern detection

def collect_raw_readings():
    # Real data source (simplified)
    return [107, 110, 115, 113, 98, 122, 119, 104, 108, 111, 114, 117, 120]

def apply_noise_filter(data):
    filtered = []
    for i in range(1, len(data) - 1):
        smoothed = (data[i-1] + data[i] + data[i+1]) / 3
        filtered.append(round(smoothed))
    return filtered

def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def generate_frequency_map(data):
    # Irrelevant helper - distractor function
    freq_map = defaultdict(int)
    for item in data:
        freq_map[item] += 1
    return freq_map

def detect_anomalies(readings):
    # Unused anomaly detection - dead code path
    anomalies = []
    baseline = sum(readings) / len(readings)
    for val in readings:
        if abs(val - baseline) > 2 * (max(readings) - min(readings)) / 4:
            anomalies.append(val)
    return anomalies

def compress_signal(data):
    # Misleading transformation - not used in final chain
    return [data[i] for i in range(0, len(data), 2)]

def calculate_entropy(data):
    # Decoy statistical measure
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p).bit_length()  # Fake entropy
    return round(entropy, 3)

def validate_calibration(signal):
    # Red herring validation check
    checksum = sum(x * (i + 1) for i, x in enumerate(signal[:5]))
    return checksum % 107

def analyze_readings(peaks):
    # Core logic: find dominant peak frequency using combinatorics
    if not peaks:
        return 0
    
    # Use itertools to generate all possible peak triplets
    triplet_combinations = list(itertools.combinations(peaks, 3))
    
    # Compute geometric mean of each triplet
    geom_means = []
    for combo in triplet_combinations:
        product = combo[0] * combo[1] * combo[2]
        geom_mean = round(product ** (1/3))
        geom_means.append(geom_mean)
    
    # Find most frequent geometric mean (mode)
    freq_count = Counter(geom_means)
    most_common_mean, count = freq_count.most_common(1)[0]
    
    # Apply secondary filter: must appear at least 2 times
    if count < 2:
        primary_diagnostic = 0
    else:
        primary_diagnostic = most_common_mean * len(triplet_combinations) // (count + 1)
    
    # Final adjustment based on control sequence
    control_sequence = [x for x in range(len(peaks), 0, -1)]
    adjustment_factor = sum(control_sequence) // len(control_sequence)
    
    final_diagnostic = primary_diagnostic + adjustment_factor
    
    # Critical print for result extraction
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution flow
raw_data = collect_raw_readings()
processed_signals = apply_noise_filter(raw_data)

# Irrelevant intermediate transformations
frequency_profile = generate_frequency_map(processed_signals)
entropy_score = calculate_entropy(processed_signals)
signal_checksum = validate_calibration(processed_signals)
compressed_stream = compress_signal(processed_signals)

# Actual relevant operations
detected_peaks = extract_peaks(processed_signals)
final_diagnostic = analyze_readings(detected_peaks)