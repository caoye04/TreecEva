import itertools

# Simulated health monitoring system with multiple sensor inputs and diagnostic logic

def analyze_rhythm(pattern):
    # Irrelevant helper: analyzes heart rhythm (not used in final result)
    if len(pattern) < 3:
        return False
    return all(a < b for a, b in zip(pattern, pattern[1:]))


def compute_entropy(seq):
    # Distractor function: computes Shannon entropy (unused in critical path)
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * (p).bit_length()  # Simplified log approximation
    return round(entropy, 4)

# Sensor data initialization (some are red herrings)
sensor_ids = ['S1', 'S2', 'S3', 'S4']
signal_noise = [0.12, 0.34, 0.08, 0.21]
baseline_offsets = {'S1': 10, 'S2': 15, 'S3': 8, 'S4': 12}

temp_readings = [36.5, 37.1, 38.2, 39.0]  # Celsius
diastolic = [80, 85, 90, 95]
systolic = [120, 130, 140, 150]

# Bitmask simulation for error flags (partially relevant)
error_flags = [0b1010, 0b0101, 0b1100, 0b0011]
active_sensors = [True, True, False, True]  # S3 is inactive

# Core diagnostic indicators (used in answer)
heart_rates = [72, 75, 78, 81]
respiration_rates = [16, 18, 20, 22]

# Threshold configuration (critical for decision logic)
thresholds = {
    'hr_high': 77,
    'rr_high': 19,
    'temp_high': 38.0
}

# Construct health indicators using dictionary and filtering (core logic)
health_indicators = {}
for i, sid in enumerate(sensor_ids):
    if not active_sensors[i]:  # Skip inactive sensor
        continue
    
    # Real-time metric aggregation
    metrics = {
        'rate': heart_rates[i],
        'resp': respiration_rates[i],
        'temp': temp_readings[i],
        'noise': signal_noise[i]
    }
    
    # Flag conditions (some flags are distractions)
    flags = 0
    if metrics['rate'] > thresholds['hr_high']:
        flags |= 0b0001
    if metrics['resp'] > thresholds['rr_high']:
        flags |= 0b0010
    if metrics['temp'] > thresholds['temp_high']:
        flags |= 0b0100
    if metrics['noise'] > 0.20:
        flags |= 0b1000  # Irrelevant flag for noise
    
    metrics['alert_code'] = flags
    health_indicators[sid] = metrics

# Dead code path: unused transformation
transformed = list(itertools.starmap(lambda x, y: x + y, zip(diastolic, systolic)))

# Unused set operation (distractor)
over_threshold = set()
for hr in heart_rates:
    if hr > thresholds['hr_high']:
        over_threshold.add(hr)

# Critical processing function
def process_metrics(indicators, config):
    # Uses set operations and bit manipulation
    critical_count = 0
    temp_alerts = []
    rate_codes = set()
    
    for sid, data in indicators.items():
        # Extract alert bits
        code = data['alert_code']
        has_rate_alert = code & 0b0001
        has_resp_alert = code & 0b0010
        has_temp_alert = code & 0b0100
        
        # Only rate and resp matter; temp is distraction
        if has_rate_alert and has_resp_alert:
            critical_count += 1
        
        # Collect temp codes even though unused later
        if has_temp_alert:
            temp_alerts.append(data['temp'])
        
        # Track unique rate alert codes (XOR accumulation - red herring)
        rate_xor = 0
        for b in range(4):
            if code & (1 << b):
                rate_xor ^= (1 << b)
        rate_codes.add(rate_xor)
    
    # Real computation: combine critical count with XOR of valid sensor IDs
    sensor_id_numeric = sum(ord(c) for c in ''.join(indicators.keys()))
    id_checksum = sensor_id_numeric ^ (sensor_id_numeric >> 4)
    
    # Final result depends only on critical_count and id_checksum
    # All above distractors do not affect outcome
    intermediate = critical_count * 1000
    final_value = intermediate + (id_checksum % 1000)
    
    # Decoy calculation (never used)
    if temp_alerts:
        avg_temp_alert = sum(temp_alerts) / len(temp_alerts)
        final_value -= int(avg_temp_alert)
    
    return final_value

# Execute core logic
final_diagnostic = process_metrics(health_indicators, thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")