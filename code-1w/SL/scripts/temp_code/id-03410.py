import math

# Simulated health monitoring system with diagnostic processing
def analyze_vital(vital, baseline, deviation_factor):
    if abs(vital - baseline) > deviation_factor * baseline:
        return 1
    return 0

# Irrelevant helper (decoy)
def encrypt_signal(x):
    return (x * 1103515245 + 12345) & 0x7FFFFFFF

# Data transformation function with distractors
def normalize_readings(readings):
    mean_val = sum(readings) / len(readings)
    std_dev = (sum((x - mean_val) ** 2 for x in readings) / len(readings)) ** 0.5
    normalized = [(x - mean_val) / std_dev for x in readings]
    
    # Dead code path - never used
    if len(normalized) > 100:
        bucketed = [int(x * 10) for x in normalized]
        histogram = {}
        for val in bucketed:
            histogram[val] = histogram.get(val, 0) + 1
    
    return normalized

# Unused complex structure (red herring)
class SignalProcessor:
    def __init__(self, window_size):
        self.window_size = window_size
        self.buffer = []
    
    def add_point(self, x):
        self.buffer.append(x)
        if len(self.buffer) > self.window_size:
            self.buffer.pop(0)

# Core diagnostic logic
def evaluate_stability(risk_scores):
    sorted_scores = sorted(risk_scores)
    midpoint = len(sorted_scores) // 2
    median_score = (sorted_scores[midpoint] + sorted_scores[~midpoint]) / 2
    stability_index = 1 / (1 + math.exp(-median_score))
    return int(stability_index * 100)

# Main processing with slicing and dictionary use
def process_metrics(data, limits):
    anomalies = 0
    recent_slice = data[-50:]  # Use only last 50 readings
    
    # Distractor: unused set operation
    unique_signatures = {hash(round(x, 2)) for x in data}
    signature_count = len(unique_signatures)
    
    # Relevant computation
    baselines = {'hr': 72, 'bp': 120, 'temp': 98.6}
    vital_map = {'heart_rate': 'hr', 'blood_pressure': 'bp', 'temperature': 'temp'}
    
    scores = []
    for entry in recent_slice:
        timestamp = entry[0]  # unused
        vitals = entry[1]
        
        # Bit manipulation decoy
        encoded_flag = 0
        if vitals.get('spo2', 100) < 95:
            encoded_flag |= (1 << 3)
        if vitals.get('hr', 0) > 100:
            encoded_flag |= (1 << 1)
        
        score = 0
        for k, v in vitals.items():
            if k in vital_map:
                base_key = vital_map[k]
                baseline = baselines[base_key]
                dev_factor = limits.get(base_key, 0.15)
                score += analyze_vital(v, baseline, dev_factor)
        
        # String splitting red herring (simulated log parsing)
        log_entry = "SYS:ALERT|CODE:0x1A|TIME:14:22"
        parts = log_entry.split('|')
        code_hex = parts[1].split(':')[1]  # '0x1A'
        alert_code = int(code_hex, 16)  # 26, unused
        
        scores.append(score)
    
    # Real logic path
    filtered_scores = [s for s in scores if s > 0]
    if not filtered_scores:
        filtered_scores = [0]
    
    avg_anomaly = sum(filtered_scores) / len(filtered_scores)
    stability = evaluate_stability(scores)
    
    # Final computation - answer derived here
    final_diagnostic = int(avg_anomaly * 100 + stability)
    
    # Decoy assignment
    final_diagnostic = final_diagnostic ^ 0x55
    final_diagnostic = final_diagnostic + 17
    
    return final_diagnostic

# Simulated dataset generation (deterministic)
raw_data = []
base_time = 1000
for i in range(200):
    t = base_time + i
    hr = 72 + 10 * math.sin(i / 10) + 3 * math.cos(i / 25)
    bp = 120 + 15 * math.sin(i / 12 + 1) + 5 * math.sin(i / 40)
    temp = 98.6 + 0.8 * math.sin(i / 8 + 2)
    spo2 = 98 - 2 * abs(math.sin(i / 18))
    
    reading = (t, {
        'heart_rate': round(hr, 1),
        'blood_pressure': round(bp, 1),
        'temperature': round(temp, 1),
        'spo2': round(spo2, 1)
    })
    raw_data.append(reading)

# Threshold settings for anomaly detection
threshold_config = {
    'hr': 0.18,
    'bp': 0.12,
    'temp': 0.08
}

# Normalize data (irrelevant to final result but looks important)
normalized_values = normalize_readings([x[1]['heart_rate'] for x in raw_data])

# Trigger main logic
final_diagnostic = process_metrics(raw_data, threshold_config)

# Output result
print(f"Target result: {final_diagnostic}")