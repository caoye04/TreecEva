import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [i * 0.5 + (i % 7) for i in range(100)]
    noise_floor = 2.3
    calibrated = [math.sin(x) * 10 + noise_floor for x in raw_readings]
    return calibrated

def apply_smoothing(data):
    smoothed = []
    for i in range(len(data)):
        if i == 0:
            smoothed.append(data[i])
        elif i == len(data) - 1:
            smoothed.append((data[i-1] + data[i]) / 2)
        else:
            avg = (data[i-1] + data[i] + data[i+1]) / 3
            smoothed.append(avg)
    return smoothed

def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def calculate_entropy(values):
    # Irrelevant distractor function - not used in final computation
    freq_map = {}
    for v in values:
        bucket = int(v * 10) % 100
        freq_map[bucket] = freq_map.get(bucket, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 4)

def validate_checksum(tag_str):
    # Distractor: string method usage, but unrelated to main logic
    if not isinstance(tag_str, str) or len(tag_str) == 0:
        return False
    checksum = 0
    for ch in tag_str:
        if ch.isalpha():
            checksum += ord(ch.lower()) - ord('a') + 1
    return checksum % 13 == 0

def normalize_signal(signal):
    min_val, max_val = min(signal), max(signal)
    if max_val == min_val:
        return [0.0] * len(signal)
    return [(x - min_val) / (max_val - min_val) for x in signal]

def filter_outliers(data, factor=1.5):
    # Interquartile range filtering
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound], lower_bound, upper_bound

def analyze_signal(data, thresh):
    # Core logic hidden among distractions
    magnitude = sum(abs(x) for x in data) / len(data)
    peak_count = 0
    for x in data:
        if abs(x) > thresh:
            peak_count += 1
    # Secondary metric
    variance = sum((x - magnitude) ** 2 for x in data) / len(data)
    score = magnitude * (peak_count + 1) / (math.sqrt(variance) + 1)
    return int(round(score * 100))

def main():
    # Irrelevant tag processing with string methods
    device_tag = "SENSOR-X9G7"
    tag_valid = validate_checksum(device_tag)
    version_info = device_tag.lower().replace('-', '').upper()
    version_check = version_info.endswith('X9G7')
    
    # Real data pipeline begins
    readings = collect_sensor_readings()
    smoothed = apply_smoothing(readings)
    normalized = normalize_signal(smoothed)
    filtered_data, lb, ub = filter_outliers(normalized, factor=1.8)
    
    # Red herring: entropy calculation on irrelevant data
    dummy_data = [math.cos(i * 0.1) for i in range(50)]
    dummy_entropy = calculate_entropy(dummy_data)
    
    # Unused peak extraction (dead path)
    potential_peaks = extract_peaks(filtered_data)
    peak_threshold = 0.85
    strong_peaks = [p for p in potential_peaks if p > peak_threshold]
    
    # Actual threshold for analysis
    threshold = 0.6
    final_diagnostic = analyze_signal(filtered_data, threshold)
    
    # Print required result
    print(f"Result: {final_diagnostic}")
    
    # Additional unused diagnostics
    if len(strong_peaks) > 5:
        adjustment = math.tanh(len(strong_peaks))
    else:
        adjustment = 0.0
    
    return final_diagnostic

if __name__ == "__main__":
    main()