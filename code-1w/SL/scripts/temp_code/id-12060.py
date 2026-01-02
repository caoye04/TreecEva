from collections import defaultdict, Counter

# Simulated sensor array data with noise and redundant readings
data_stream = [
    (1, 'temp', 36.5), (2, 'hr', 78), (3, 'temp', 37.0), (4, 'spo2', 98),
    (5, 'hr', 80), (6, 'temp', 36.8), (7, 'hr', 82), (8, 'temp', 37.2),
    (9, 'spo2', 97), (10, 'hr', 79), (11, 'temp', 36.9), (12, 'hr', 81)
]

# Irrelevant mapping - red herring for mode analysis
symptom_map = {'fever': 'temp', 'tachycardia': 'hr', 'hypoxia': 'spo2'}
severity_weights = defaultdict(lambda: 1.0)
severity_weights['fever'] = 1.3
severity_weights['tachycardia'] = 1.2

# Decoy function - never used but looks important
def analyze_trend(readings):
    if not readings:
        return 0.0
    base = readings[0][2]
    final = readings[-1][2]
    return round(final - base, 2)

# Unused statistical helper - distractor
def calculate_entropy(values):
    from math import log
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Misleading intermediate processing chain
raw_temps = [v for i, t, v in data_stream if t == 'temp']
avg_temp = sum(raw_temps) / len(raw_temps)
deviations = [abs(t - avg_temp) for t in raw_temps]
temp_anomaly_flag = any(d > 0.3 for d in deviations)

# Dummy transformation on heart rate - irrelevant to final result
heart_rates = [v for i, t, v in data_stream if t == 'hr']
doubled_bpm = [hr * 2 for hr in heart_rates]  # Distraction
rate_changes = [heart_rates[i+1] - heart_rates[i] for i in range(len(heart_rates)-1)]
stable_rhythm = all(abs(delta) <= 3 for delta in rate_changes)

# Actual relevant logic buried among distractions
filtered_data = []
for idx, typ, val in data_stream:
    if typ == 'temp' and val >= 36.8:
        filtered_data.append(('high', val))
    elif typ == 'hr' and val >= 80:
        filtered_data.append(('elevated', val))

# Key function containing conditional logic and dictionary use
def process_readings(readings):
    stats = defaultdict(int)
    score_map = {'high': 3, 'elevated': 2}
    
    for category, value in readings:
        stats[category] += score_map[category]
    
    # Complex conditional expression with nested logic
    base_score = stats['high'] * 10 + stats['elevated'] * 5
    adjustment = sum(1 for c, v in readings if v > 80) if 'elevated' in stats else -2
    
    # Secondary correction based on pattern matching
    sequence = [c for c, v in readings]
    if sequence.count('high') >= 2 and sequence.count('elevated') >= 1:
        adjustment += 4
    
    # Final computation with bitwise twist
    raw_result = base_score + adjustment
    masked = raw_result ^ 15  # Bit manipulation distraction
    normalized = masked & 1023  # Keep within bounds
    
    # Critical execution point
    final_diagnostic = normalized - 50
    return final_diagnostic

# Dead code path - looks like calibration but unused
def calibrate_sensors(data):
    return [d for d in data if d[0] % 2 == 1]

calibration_test = calibrate_sensors(data_stream)

# Trigger the key statement
final_diagnostic = process_readings(filtered_data)
print(f"Result: {final_diagnostic}")