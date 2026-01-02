import math

# Simulated sensor data processing with embedded logic chain
def collect_samples():
    raw = [i * 0.1 for i in range(50)]
    offset = 2.5
    return [math.sin(x + offset) + 0.5 * math.cos(2 * x) for x in raw]

# Irrelevant helper - distractor
def smooth(data):
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        smoothed.append(sum(data[i-1:i+2]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Unused transformation - dead path
transform_log = lambda x: math.log(x + 10) if x > -10 else 0

# Core signal processor
def process_noise_floor(signal):
    floor = sum(1 for x in signal if abs(x) < 0.3)
    threshold = len(signal) * 0.4
    return floor > threshold

# Decoy analysis function
def evaluate_coherence(data):
    pairs = [(data[i], data[i+1]) for i in range(len(data)-1)]
    coherent = 0
    for a, b in pairs:
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            coherent += 1
    ratio = coherent / len(pairs)
    # This function is called but result ignored
    return ratio > 0.65

# Real preprocessing step
def extract_features(raw_signal):
    positive_peaks = [x for x in raw_signal if x > 0.7]
    negative_troughs = [x for x in raw_signal if x < -0.7]
    peak_count = len(positive_peaks)
    trough_count = len(negative_troughs)
    
    # Distractor variables
    avg_magnitude = sum(abs(x) for x in raw_signal) / len(raw_signal)
    zero_crossings = sum(1 for i in range(1, len(raw_signal)) if raw_signal[i-1] * raw_signal[i] < 0)
    
    # Actual relevant calculation
    balance_score = abs(peak_count - trough_count) * 2
    return {
        'balance': balance_score,
        'peaks': peak_count,
        'troughs': trough_count,
        'magnitude': avg_magnitude,
        'crossings': zero_crossings
    }

# String-based identifier mapping - uses string methods
def get_device_class(serial_tag):
    tag_upper = serial_tag.upper()
    if 'X9' in tag_upper:
        return 3
    elif 'Z' in tag_upper and tag_upper.endswith('NR'):
        return 1
    else:
        return 2

# Set operations for anomaly detection
def detect_anomalies(timestamps):
    expected = set(range(100, 200, 2))
    actual = set(ts % 200 for ts in timestamps)
    missing = expected - actual
    extra = actual - expected
    return len(missing) < 10 and len(extra) < 15

# Main analysis with multiple concepts
processed_data = []
def analyze_signal(data_dict):
    # Unrelated intermediate check
    temp_status = ''.join(['A' if v > 1 else 'B' for k, v in data_dict.items() if isinstance(v, (int, float))])
    flag_indicators = set(temp_status.lower())
    
    # Key logic branch
    if data_dict['balance'] < 8:
        base = 400
        adjustment = data_dict['peaks'] * 15
    else:
        base = 200
        adjustment = data_dict['troughs'] * 10
    
    # Secondary condition using string result
    device_code = get_device_class('SN-X9-776-NR')
    if device_code == 3:
        base += 50
    
    # Tertiary influence
    time_stamps = list(range(100, 160))
    if detect_anomalies(time_stamps):
        adjustment += 25
    
    # Red herring computation
    shadow_value = 0
    for i in range(5):
        shadow_value = (shadow_value * 31 + i) % 1000
    
    # Final composition
    critical_factor = base + adjustment
    scaling = math.sqrt(1 + data_dict['crossings'] / 50)
    final_score = critical_factor * scaling
    
    # The actual target variable
    final_diagnostic = int(round(final_score))
    return final_diagnostic

# Execution flow
samples = collect_samples()
evaluate_coherence(samples)  # Called but not used - misleading call
features = extract_features(samples)
processed_data = features
final_diagnostic = analyze_signal(processed_data)
print(f"Target result: {final_diagnostic}")