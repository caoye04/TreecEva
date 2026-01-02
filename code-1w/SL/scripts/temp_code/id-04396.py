import math

# Simulated sensor data aggregation (irrelevant preprocessing)
def fetch_raw_signals():
    return [0.85, 0.72, 0.93, 0.67, 0.76]

def normalize_signal(x):
    return (x - 0.5) * 2

# Irrelevant audio processing stubs (dead code path)
def analyze_audio_spectrum(signal):
    fft_bins = [math.sin(x * math.pi / 4) for x in range(8)]
    return sum(fft_bins[:3])  # Unused result

def decode_tone_sequence(seq):
    return ''.join([str(int(s * 10)) for s in seq])  # Never called

# Core system health monitoring logic
system_load = {
    'cpu': 0.88,
    'memory': 0.76,
    'disk_io': 0.44,
    'network_latency_ms': 120
}

data_snapshot = [
    {'sensor_id': 'S1', 'value': 23.5, 'threshold': 25.0},
    {'sensor_id': 'S2', 'value': 26.1, 'threshold': 25.0},
    {'sensor_id': 'S3', 'value': 22.0, 'threshold': 25.0},
    {'sensor_id': 'S4', 'value': 27.3, 'threshold': 25.0}
]

# Misleading intermediate calculations (distractors)
baseline_offset = 1.23
adjusted_readings = []
for entry in data_snapshot:
    adjusted_readings.append(entry['value'] + baseline_offset)

# Unused statistical analysis (red herring)
mean_adjusted = sum(adjusted_readings) / len(adjusted_readings)
variance = sum((x - mean_adjusted) ** 2 for x in adjusted_readings) / len(adjusted_readings)
std_deviation = math.sqrt(variance)

# Data transformation using lambda and slicing (required features)
extract_critical = lambda readings: [r['value'] for r in readings if r['value'] > r['threshold']]
critical_values = extract_critical(data_snapshot)

# String manipulation distractor (irrelevant to final result)
sensor_codes = ['S1', 'S2', 'S3', 'S4']
encoded_tag = '-'.join([code[1:] for code in sensor_codes])
version_hash = encoded_tag[::-1]  # Reversed string, unused later

# Complex conditional logic with nesting (3 levels deep)
def evaluate_stability(metrics, load_profile):
    risk_score = 0
    if metrics:
        if len(metrics) > 3:
            high_risk_count = 0
            for m in metrics:
                if m['value'] > m['threshold']:
                    deviation = m['value'] - m['threshold']
                    if deviation > 1.5:
                        risk_score += 3
                    elif deviation > 0.5:
                        risk_score += 2
                    else:
                        risk_score += 1
            if high_risk_count == 0:
                risk_score -= 1  # Adjustment not taken due to logic
    else:
        risk_score = 5
    
    # Additional load-based adjustment
    load_factor = 0
    if load_profile['cpu'] > 0.8:
        load_factor += 2
    if load_profile['memory'] > 0.7:
        load_factor += 1
    if load_profile['network_latency_ms'] > 100:
        load_factor += 2
        
    risk_score += load_factor
    return risk_score

# Decoy function that appears related but isn't used
def compute_fault_probability(readings, threshold=25.0):
    above_count = len([r for r in readings if r['value'] > threshold])
    probability = above_count / len(readings)
    return round(probability * 100, 2)

# Another red herring: bit manipulation with no impact
status_flag = 0b101010
masked_flag = status_flag & 0b111100
rotated_flag = ((masked_flag << 2) & 0b111111) | (masked_flag >> 4)

# Actual key computation chain
filtered_data = data_snapshot[1:3]  # Slicing operation (required)
analysis_weights = {
    'base': 1.0,
    'critical_penalty': 1.8,
    'load_multiplier': 1.4
}

# Final processing function combining multiple concepts
def process_metrics(sensor_data, sys_load):
    # Step 1: extract values above threshold
    exceeded = [s for s in sensor_data if s['value'] > s['threshold']]
    base_count = len(exceeded)
    
    # Step 2: calculate total excess
    total_excess = sum(s['value'] - s['threshold'] for s in exceeded)
    
    # Step 3: apply non-linear penalty
    penalty_factor = math.log(1 + total_excess)  # grows slowly
    
    # Step 4: integrate system load
    load_score = 0
    if sys_load['cpu'] > 0.85:
        load_score += 3
    if sys_load['memory'] > 0.75:
        load_score += 2
    
    # Step 5: combine all factors
    aggregated = (base_count * analysis_weights['base'] + 
                 penalty_factor * analysis_weights['critical_penalty']) * 
                (1 + load_score * 0.1) * analysis_weights['load_multiplier']
    
    # Step 6: apply floor cap
    if aggregated < 5.0:
        aggregated = 5.0
        
    return round(aggregated, 4)

# Execution point of interest
final_diagnostic = process_metrics(data_snapshot, system_load)

# Print required output
print(f"Result: {final_diagnostic}")