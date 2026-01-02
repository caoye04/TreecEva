from collections import defaultdict, Counter
import math

# Simulated sensor network diagnostics with noise filtering and anomaly detection
def preprocess_signal(raw_data, threshold=0.75):
    filtered = []
    noise_count = 0
    for val in raw_data:
        if abs(val) < threshold:
            noise_count += 1
        else:
            filtered.append(val ** 2)
    return filtered, noise_count

def generate_checksum(sequence):
    # Irrelevant checksum for distraction
    chk = 0
    for i, x in enumerate(sequence):
        chk ^= int(x) & 0xFF
    return chk + 1000

def rolling_average(values, window_size=3):
    if len(values) < window_size:
        return [0]
    avgs = []
    for i in range(len(values) - window_size + 1):
        avgs.append(sum(values[i:i+window_size]) / window_size)
    return avgs

def detect_spikes(anomalies, sensitivity=1.5):
    spike_count = 0
    for a in anomalies:
        if a > sensitivity * 10:
            spike_count += 1
    return spike_count

def accumulate_diagnostics(logs):
    stats = defaultdict(int)
    temp_buffer = []
    total_power = 0
    
    for entry in logs:
        category = entry['type']
        readings = entry['values']
        
        # Real processing path
        processed, noise = preprocess_signal(readings)
        stats['noise_samples'] += noise
        
        if category == 'thermal':
            avg_val = sum(processed) / len(processed) if processed else 0
            stats['thermal_baseline'] += avg_val
            stats['thermal_events'] += 1
        elif category == 'vibration':
            rolled = rolling_average(processed)
            max_roll = max(rolled) if rolled else 0
            stats['peak_vibration'] = max(stats['peak_vibration'], max_roll)
        
        # Distractor: power accumulation with irrelevant transformation
        for r in readings:
            if r > 0:
                total_power += int(math.log(abs(r) + 1, 2))

        # Dead code path - never accessed due to logic above
        if False and category == 'deprecated':
            temp_buffer.extend(processed)

    # Another red herring function call (no side effects)
    _ = generate_checksum([int(stats[k]) for k in stats if 'thermal' in k])
    
    return stats

def classify_anomaly_score(score):
    # Unused classification function - distractor
    if score < 10:
        return 'LOW'
    elif score < 50:
        return 'MEDIUM'
    else:
        return 'HIGH'

def analyze_readings(diagnostic_log):
    result = 0
    
    # Key logic chain begins
    keys = list(diagnostic_log.keys())
    if 'thermal_baseline' in diagnostic_log and 'thermal_events' in diagnostic_log:
        base = diagnostic_log['thermal_baseline']
        events = diagnostic_log['thermal_events']
        if events > 0:
            result += int(base / events)
    
    if 'peak_vibration' in diagnostic_log:
        vib = diagnostic_log['peak_vibration']
        result -= int(vib)
    
    # Add noise penalty
    if 'noise_samples' in diagnostic_log:
        penalty = diagnostic_log['noise_samples'] // 10
        result -= penalty
    
    # Decoy operations with intermediate variables
    temp_result = result * 2
    temp_result += 500  # Misleading offset
    temp_result = abs(temp_result) % 1000  # Wraparound distraction
    
    # Final computation
    final_value = (result * 3) + 17
    
    return final_value

# Main execution flow
if __name__ == '__main__':
    # Simulated input data from sensor array
    sensor_logs = [
        {
            'type': 'thermal',
            'values': [0.1, -0.3, 0.4, 1.2, -2.1, 0.8]
        },
        {
            'type': 'vibration',
            'values': [0.6, 0.2, 0.9, 3.1, -1.5, 2.2]
        },
        {
            'type': 'thermal',
            'values': [0.7, -0.5, 1.8, -3.2, 0.4]
        }
    ]
    
    # Irrelevant pre-analysis (dead weight)
    all_values = []
    for log in sensor_logs:
        all_values.extend(log['values'])
    value_counter = Counter(all_values)
    common_pairs = value_counter.most_common(2)
    
    # Core processing pipeline
    processed_logs = accumulate_diagnostics(sensor_logs)
    
    # Critical statement
    final_diagnostic = analyze_readings(processed_logs)
    
    # Output the target result
    print(f"Result: {final_diagnostic}")