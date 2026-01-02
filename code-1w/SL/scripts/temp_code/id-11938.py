from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def fetch_sensor_readings():
    return [145, 278, 314, 489, 503, 672, 731, 886, 945, 1050]

def apply_noise_filter(raw_data):
    filtered = []
    for val in raw_data:
        if val % 2 == 0:
            filtered.append(val // 2)
        else:
            filtered.append(val * 3 + 1)
    return filtered

def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def generate_checksum(sequence):
    # Irrelevant checksum function (decoy)
    chk = 0
    for num in sequence:
        chk = (chk ^ num) * 13 % 97
    return chk

def deprecated_normalization(arr):
    # Dead code path — never called
    return [round((x - min(arr)) / (max(arr) - min(arr)), 4) for x in arr]

def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def transform_signal(peaks):
    transformed = []
    for p in peaks:
        transformed.append((p ^ 255) % 1000)  # Bitwise XOR and modulo
    return transformed

def rolling_window_avg(data, window_size=3):
    # Unused distractor function
    averages = []
    for i in range(len(data) - window_size + 1):
        avg = sum(data[i:i+window_size]) / window_size
        averages.append(round(avg, 4))
    return averages

def detect_anomalies(values, limit=500):
    anomalies = []
    temp_log = []
    for v in values:
        temp_log.append(v * 2 + 10)  # Red herring computation
        if v > limit:
            anomalies.append(v)
    return anomalies

def shift_register_encode(data_stream):
    # Complex but irrelevant encoding (misleading intermediate result)
    register = 0b1101
    encoded = []
    for item in data_stream:
        register = (register ^ item) & 0b1111
        encoded.append(register << 2)
    return encoded

def analyze_pattern(dataset, threshold):
    # Core logic hidden among distractions
    base_sum = sum(dataset)
    mod_adjusted = base_sum % 987
    inverted = 10000 - mod_adjusted
    score = inverted * 2
    if score > threshold:
        score -= threshold * 0.5
    return int(score)

def main():
    # Entry point with multiple red herrings
    raw_readings = fetch_sensor_readings()
    
    # Irrelevant preprocessing steps
    noise_filtered = apply_noise_filter(raw_readings)
    entropy_value = compute_entropy(noise_filtered)
    
    # Generate unused statistical features
    mean_val = sum(noise_filtered) / len(noise_filtered)
    variance = sum((x - mean_val) ** 2 for x in noise_filtered) / len(noise_filtered)
    std_dev = math.sqrt(variance)
    
    # Peak extraction (partially relevant)
    signal_peaks = extract_peaks(noise_filtered)
    
    # Transform peaks into final data form
    transformed_data = transform_signal(signal_peaks)
    
    # Unused anomaly detection (distractor)
    anomalies = detect_anomalies(transformed_data, limit=400)
    
    # Fake checksum and encoding (dead computations)
    fake_checksum = generate_checksum(transformed_data)
    encoded_stream = shift_register_encode(transformed_data)
    
    # Threshold derived from entropy (red herring dependency)
    key_threshold = int(entropy_value * 100)  # Actually used, but seems suspicious
    
    # CRITICAL STATEMENT: This is where the answer is determined
    final_diagnostic = analyze_pattern(transformed_data, key_threshold)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    # Additional irrelevant logs
    debug_log = defaultdict(int)
    for x in transformed_data:
        debug_log[x % 5] += 1
    
    return final_diagnostic

if __name__ == "__main__":
    main()