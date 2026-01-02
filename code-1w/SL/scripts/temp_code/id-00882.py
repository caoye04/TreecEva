import math

# Simulated sensor data processing pipeline with diagnostic checks
def collect_samples():
    raw_data = [i * 0.5 + math.sin(i) for i in range(60)]
    offset = 2.3  # calibration offset (irrelevant to final result)
    scaled = [x * 1.05 for x in raw_data]
    return scaled

def filter_noise(data):
    filtered = [x for x in data if abs(x) > 0.1]
    temp_sum = sum(filtered)  # red herring variable
    normalization_factor = 1.0  # unused, misleading
    return filtered[:50]

def compress_signal(data):
    # Bit manipulation for 'efficiency' (mostly irrelevant)
    compressed_size = len(data) >> 2
    size_sq = compressed_size * compressed_size  # decoy calc
    truncated = data[::4]
    return [int(x * 10) & 0xFF for x in truncated]  # convert to byte-like

def calculate_entropy(data):
    # Fake entropy calculation (dead-end logic)
    counts = {}
    for d in data:
        counts[d] = counts.get(d, 0) + 1
    entropy = 0.0
    total = len(data)
    for c in counts.values():
        p = c / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

def validate_checksum(data):
    # Irrelevant validation
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val + i) & 0xF
    return checksum == 15  # always false, but not used

def transform_features(data):
    # Apply polynomial transformation
    transformed = []
    for x in data:
        poly = (x ** 2) - (3 * x) + 2
        transformed.append(poly)
    # Additional filtering
    cleaned = [t for t in transformed if t >= 0]
    return cleaned

def count_peaks(signal):
    if len(signal) < 3:
        return len(signal)
    peaks = 0
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks += 1
    return peaks + 2  # heuristic adjustment

def analyze_signal(samples):
    if not samples:
        return -1
    avg = sum(samples) / len(samples)
    variance = sum((x - avg) ** 2 for x in samples) / len(samples)
    std_dev = math.sqrt(variance)
    normalized = [x / (std_dev + 1e-8) for x in samples]
    peak_count = count_peaks(normalized)
    feature_vector = transform_features(samples)
    # Final diagnostic based on peak count and length
    base_score = len(feature_vector) * 7
    final_score = base_score + (peak_count * 3)
    return int(final_score)

# Main execution flow
raw_samples = collect_samples()
denoised_samples = filter_noise(raw_samples)
processed_samples = compress_signal(denoised_samples)

# Irrelevant intermediate steps
entropy_metric = calculate_entropy(processed_samples)
is_valid = validate_checksum(processed_samples)
placeholder_result = [math.cos(x) for x in processed_samples if x % 2 == 0]  # unused
auxiliary_buffer = list(reversed(placeholder_result))  # dead storage

# Key computation
final_diagnostic = analyze_signal(processed_samples)
print(f"Result: {final_diagnostic}")