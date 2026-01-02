from collections import defaultdict, Counter

# Simulated quantum sensor array diagnostics
def preprocess_readings(raw_readings):
    processed = []
    noise_floor = 0.003
    for idx, val in enumerate(raw_readings):
        if abs(val) < noise_floor:
            adjusted = 0.0
        else:
            adjusted = round(val * (1 + 0.1 * (idx % 3)), 4)
        processed.append(adjusted)
    return processed

def compute_coherence_score(seq):
    score = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            score += 1
        elif seq[i] < seq[i-1]:
            score -= 1
    return score

def detect_anomalies(readings):
    anomalies = []
    threshold = 2.5
    for i, v in enumerate(readings):
        if abs(v) > threshold:
            anomalies.append(i)
    return anomalies if anomalies else [0]

def rolling_average(data, window=3):
    smoothed = []
    padding = [data[0]] * (window // 2)
    extended = padding + data + padding
    for i in range(len(data)):
        window_vals = extended[i:i+window]
        avg = sum(window_vals) / window
        smoothed.append(round(avg, 4))
    return smoothed

def analyze_system_state(sensor_data, factor):
    # Core analysis logic
    calibrated = [x * factor for x in sensor_data]
    
    # Distractor: irrelevant transformation
    decoy_map = defaultdict(int)
    for x in calibrated:
        decoy_map[int(x) % 7] += 1
    
    # More distractors
    temp_stats = {'max': max(calibrated), 'min': min(calibrated)}
    temp_stats['range'] = temp_stats['max'] - temp_stats['min']
    temp_stats['mid'] = (temp_stats['max'] + temp_stats['min']) / 2
    
    # Real computation path
    shifted = [x - temp_stats['mid'] for x in calibrated]
    rectified = [abs(x) for x in shifted]
    
    # Use of enumerate and zip
    indexed_energy = [(i, e**2) for i, e in enumerate(rectified)]
    energy_values = [e for _, e in indexed_energy]
    
    averaged = rolling_average(energy_values, 2)
    
    # Another decoy function call with side effect
    def decoy_transform(arr):
        return [a ^ int(a) for a in arr]  # no-op effectively
    
    decoy_result = decoy_transform([1.1, 2.2, 3.3])
    
    # Critical computation
    coherence = compute_coherence_score(averaged)
    anomaly_indices = detect_anomalies(averaged)
    primary_index = anomaly_indices[0]
    
    # Final diagnostic calculation
    final_diagnostic = int((coherence * factor) + primary_index - sum(energy_values[:3]))
    
    # Red herring: unused complex structure
    debug_snapshot = {
        'timestamp': 1698765432,
        'readings_count': len(sensor_data),
        'checksum': sum(int(x*100) for x in sensor_data) % 1000,
        'decoy_metric': Counter(decoy_map).total()
    }
    
    return final_diagnostic

# Irrelevant global constants
MAX_BUFFER_SIZE = 1024
PROTOCOL_VERSION = "QX-9"
ACTIVE_CHANNELS = [1, 1, 0, 1, 1]

# Simulated input data
base_readings = [0.12, -0.45, 1.67, 2.89, -1.23, 0.67, 3.44, -2.11, 1.34, 0.88]
quantum_readings = preprocess_readings(base_readings)
calibration_factor = 1.75

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_readings, calibration_factor)

print(f"Result: {final_diagnostic}")