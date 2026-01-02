from collections import defaultdict, Counter
import math

# Simulated sensor data acquisition
def acquire_signal(raw=False):
    base_readings = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    if raw:
        return [x * 10 + 7 for x in base_readings]
    return [x * 3 + 2 for x in base_readings]

# Irrelevant transformation - red herring
def encrypt_data(data):
    return [d ^ 255 for d in data[:5]]

# Signal conditioning with multiple distractions
def filter_noise(signal, threshold=50):
    filtered = []
    temp_buffer = []
    stats_log = defaultdict(int)
    
    for val in signal:
        stats_log['total'] += 1
        if val > 10 and val < 80:  # valid range
            stats_log['valid'] += 1
            temp_buffer.append(val)
        else:
            stats_log['discarded'] += 1
    
    # Apply moving average of window size 2
    smoothed = []
    for i in range(len(temp_buffer) - 1):
        smoothed.append((temp_buffer[i] + temp_buffer[i+1]) / 2)
    
    # Dead code path - never executed due to logic above
    if len(signal) > 100:
        fallback = sum(temp_buffer) / len(temp_buffer)
        smoothed.append(fallback)
    
    return smoothed, stats_log

# Misleading feature extraction
def extract_features(data):
    features = {}
    squared_sum = sum(x**2 for x in data)
    features['rms'] = math.sqrt(squared_sum / len(data))
    features['peak'] = max(data)
    features['entropy'] = 0.0
    count = Counter(data)
    for v in count.values():
        if v > 0:
            features['entropy'] -= (v/len(data)) * math.log2(v/len(data))
    return features

# Core processing with decoy functions around
processed_chunk = None
temporary_payload = None
validation_check = False

raw_data = acquire_signal(raw=False)
encrypted_mirror = encrypt_data(raw_data)  # unused later

filtered_signal, diagnostics = filter_noise(raw_data)

# Linear search for anomaly pattern - rarely triggered
anomaly_found = False
for i in range(len(filtered_signal) - 2):
    if (filtered_signal[i] > filtered_signal[i+1] > filtered_signal[i+2]):
        anomaly_found = True
        break

if not anomaly_found:
    processed_chunk = [x for x in filtered_signal if x > 10]
else:
    processed_chunk = filtered_signal

# Decoy state tracking
status_flags = [False] * 5
status_flags[2] = True
status_flags[3] = any(x > 100 for x in raw_data)  # always false

# Unused intermediate calculation
aggregate_score = sum(processed_chunk) * 0.95
normalization_factor = math.log(len(processed_chunk) + 1)

# Actual analysis function buried among distractions
def analyze_signal(chunk):
    result_map = {}
    total_power = 0
    phase_shift = 0
    
    for i, val in enumerate(chunk):
        if i % 2 == 0:
            total_power += val * math.sin(i + 1)
        else:
            total_power -= val * math.cos(i + 1)
        
        # Bit manipulation as distraction
        shifted = int(val) ^ 0xFF
        phase_shift += (shifted >> 4) & 0x0F
    
    # Final diagnostic derived from mixed operations
    stability_index = len(chunk) ** 2
    noise_component = phase_shift % 17
    
    # Key computation - deterministic but obscured
    final_diagnostic = int(total_power) + stability_index - noise_component
    
    # Early return trap - condition never met
    if total_power < 0:
        return -1
        
    return final_diagnostic

# Critical execution point
final_diagnostic = analyze_signal(processed_chunk)

# Output required format
print(f"Result: {final_diagnostic}")