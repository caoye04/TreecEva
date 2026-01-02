from collections import defaultdict, Counter
import itertools

# Simulated sensor data stream
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 21.9, 20.4, 27.3]
humidity_readings = [45, 50, 52, 48, 55, 60, 62, 58]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1010, 1008, 1014]

# Irrelevant backup data (distractor)
backup_temps = [x + 5 for x in temperature_readings]
shadow_copy = humidity_readings.copy()

# Thresholds for anomaly detection
thresholds = {
    'temp_high': 25.0,
    'temp_low': 21.0,
    'humidity_high': 58,
    'pressure_trend_window': 3
}

# Misleading auxiliary variables (dead computations)
baseline_avg = sum(temperature_readings[:4]) / 4
adjustment_factor = 1.05
normal_range = (baseline_avg * 0.95, baseline_avg * 1.05)
calibration_offset = 0.7  # unused

# Simulate log entries with metadata
log_data = []
for i in range(len(temperature_readings)):
    entry = {
        'timestamp': f'2023-07-01T12:{i:02}:00',
        'temp': temperature_readings[i],
        'humidity': humidity_readings[i],
        'pressure': pressure_readings[i],
        'sensor_id': f'S{i+1}',
        'status': 'OK'
    }
    
    # Conditional expression for status (partially relevant)
    if entry['temp'] > thresholds['temp_high'] or entry['temp'] < thresholds['temp_low']:
        entry['status'] = 'ALERT'
    
    log_data.append(entry)

# Dead code path - never called (distraction)
def legacy_calibrate(data):
    return [x * 0.99 for x in data]

# Unused helper that looks important (distractor)
def compute_rolling_entropy(seq, window=3):
    entropy_vals = []
    for i in range(len(seq) - window + 1):
        window_data = seq[i:i+window]
        freq = Counter(window_data)
        total = len(window_data)
        entropy = -sum((count/total) * (count/total).__log__() for count in freq.values())
    return entropy_vals

# Relevant processing function with distractors embedded
def analyze_pressure_trend(logs, window_size):
    pressures = [entry['pressure'] for entry in logs]
    trends = []
    for i in range(len(pressures) - window_size + 1):
        window = pressures[i:i+window_size]
        trend = 'rising' if window[-1] > window[0] else 'falling' if window[-1] < window[0] else 'stable'
        trends.append(trend)
    
    # Distractor computation: complex but unused result
    change_pairs = list(itertools.combinations([pressures[i+1] - pressures[i] for i in range(len(pressures)-1)], 2))
    net_volatility = sum(abs(a) + abs(b) for a, b in change_pairs) if change_pairs else 0
    
    return trends.count('rising')

# Another irrelevant utility (red herring)
def generate_synthetic_data(count):
    return [{'sim_temp': 22 + (i % 5)} for i in range(count)]

# Main diagnostic processor
def process_metrics(logs, config):
    # Extract statuses
    statuses = [entry['status'] for entry in logs]
    alert_count = statuses.count('ALERT')
    
    # Compute humidity mode (most frequent)
    humidity_mode = Counter([entry['humidity'] for entry in logs]).most_common(1)[0][0]
    
    # Determine pressure trend significance
    rising_trends = analyze_pressure_trend(logs, config['pressure_trend_window'])
    
    # Fake complexity: nested conditional expressions with one key outcome
    humidity_flag = 10 if humidity_mode >= config['humidity_high'] else 5 if humidity_mode > 50 else 0
    temp_alert_penalty = alert_count * 15
    trend_multiplier = 2 if rising_trends >= 2 else 1
    
    # Secondary distraction: bit manipulation on unrelated index pattern
    indices = [i for i, x in enumerate(logs) if x['temp'] > config['temp_high']]
    packed_flags = 0
    for idx in indices:
        packed_flags |= (1 << idx)  # looks cryptic but only final magnitude matters
    flag_magnitude = bin(packed_flags).count('1')
    
    # Dead calculation using backup data (irrelevant)
    if len(backup_temps) > 5:
        smoothed = [backup_temps[i] + backup_temps[i+1] for i in range(0, len(backup_temps)-1, 2)]
        adjustment = sum(smoothed) / len(smoothed) * 0.01
    else:
        adjustment = 0
    
    # Core logic disguised among distractions
    base_score = 50
    anomaly_deduction = temp_alert_penalty + flag_magnitude * 7
    environmental_bonus = (30 if humidity_flag > 0 else 10) + (20 if trend_multiplier == 2 else 5)
    
    # Final diagnostic computed from mixed relevant and filtered signals
    final_diagnostic = base_score - anomaly_deduction + environmental_bonus
    
    # Irrelevant transformation (distractor)
    normalized_diag = round(final_diagnostic / 10) * 10
    
    return int(final_diagnostic)

# Execution point of interest
final_diagnostic = process_metrics(log_data, thresholds)
print(f"Result: {final_diagnostic}")