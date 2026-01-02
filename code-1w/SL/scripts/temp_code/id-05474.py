from collections import defaultdict, Counter
import math

# Simulated sensor log parser with diagnostic evaluation
def parse_log_entry(entry):
    parts = entry.split('|')
    timestamp = int(parts[0])
    sensor_id = parts[1]
    reading_str = parts[2]
    
    # Parse readings
    readings = [float(x) for x in reading_str.split(',')]
    avg_reading = sum(readings) / len(readings)
    peak = max(readings)
    stability = peak - avg_reading
    
    return {
        'timestamp': timestamp,
        'sensor': sensor_id,
        'average': avg_reading,
        'peak': peak,
        'stability': stability,
        'anomaly_flag': stability > 15.0
    }

def compute_entropy(values):
    """Irrelevant utility function - not used in main logic"""
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def validate_calibration(sequence):
    """Dead code path - never called"""
    base_pattern = [1, 2, 4, 8]
    return all(seq == exp << i for i, (seq, exp) in enumerate(zip(sequence, base_pattern)))

def rolling_average(data, window=3):
    """Distractor function: looks useful but unused"""
    if len(data) < window:
        return []
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]

def detect_spike_pattern(readings, threshold=25.0):
    """Partially used function - only called once with irrelevant data"""
    spikes = 0
    for i in range(1, len(readings)):
        if readings[i] > threshold and readings[i] > 1.8 * readings[i-1]:
            spikes += 1
    return spikes > 2

# Main processing pipeline
def process_metrics(log_entries, thresholds):
    parsed_logs = [parse_log_entry(entry) for entry in log_entries]
    
    # Group by sensor
    sensor_groups = defaultdict(list)
    for record in parsed_logs:
        sensor_groups[record['sensor']].append(record)
    
    # Compute aggregate statistics per sensor
    diagnostics = {}
    for sid, records in sensor_groups.items():
        sorted_records = sorted(records, key=lambda x: x['timestamp'])
        
        # Extract sequences
        averages = [r['average'] for r in sorted_records]
        peaks = [r['peak'] for r in sorted_records]
        stabilities = [r['stability'] for r in sorted_records]
        
        # Real-time anomaly detection
        critical_count = sum(1 for r in records if r['anomaly_flag'])
        high_peak_count = sum(1 for p in peaks if p > thresholds['peak_warn'])
        
        # Weighted health score
        stability_score = sum(stabilities) / len(stabilities)
        risk_factor = (critical_count * 3.5) + (high_peak_count * 1.2)
        
        # Hidden logic: answer derived from specific calculation
        baseline_ref = thresholds['base']
        adjustment = math.sin(math.radians(len(averages)))  # periodic mod
        normalized_risk = risk_factor / (baseline_ref + adjustment)
        
        # Distractor: complex but unused structure
        history_trace = []
        for i, (avg, pk) in enumerate(zip(averages, peaks)):
            history_trace.append({
                'index': i,
                'diff': pk - avg,
                'phase': math.cos(i * 0.5),
                'dummy_flag': i % 7 == 0
            })
        
        diagnostics[sid] = {
            'risk': risk_factor,
            'stability_metric': stability_score,
            'anomaly_events': critical_count,
            'trace_length': len(history_trace),
            'adjusted_risk': normalized_risk
        }
    
    # Final aggregation across sensors
    all_risks = [d['risk'] for d in diagnostics.values()]
    all_adjusted = [d['adjusted_risk'] for d in diagnostics.values()]
    total_anomalies = sum(d['anomaly_events'] for d in diagnostics.values())
    
    # Key computation - this determines the final answer
    raw_sum = sum(all_risks)
    adjustment_factor = len(all_adjusted) * 0.75
    penalty = total_anomalies ** 1.5
    
    # This is the actual answer variable
    final_diagnostic = int(raw_sum - adjustment_factor - penalty)
    
    # More red herrings
    spike_test_data = [5.0, 6.2, 24.1, 7.3, 8.9, 26.0, 4.1]
    false_spike_alert = detect_spike_pattern(spike_test_data, threshold=20.0)
    
    entropy_sample = [10, 20, 30, 40]
    entropy_value = compute_entropy(entropy_sample)
    
    return final_diagnostic

# Simulated input data
dummy_serial_sequence = [1, 2, 4, 8, 16]  # Unused but suggestive
is_valid = validate_calibration(dummy_serial_sequence)

log_data = [
    '1001|S1|12.1,13.4,11.8,14.0',
    '1002|S2|15.6,16.2,9.8,18.1',
    '1003|S1|20.3,22.1,18.9,24.0',
    '1004|S3|11.5,10.9,12.3,11.7',
    '1005|S2|25.6,19.8,27.3,26.9',
    '1006|S1|14.2,15.8,13.9,16.1',
    '1007|S3|18.4,19.1,17.6,20.3',
    '1008|S2|28.7,29.1,26.5,30.2'
]

system_thresholds = {
    'peak_warn': 25.0,
    'base': 8.0,
    'grace': 1.5
}

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_thresholds)
print(f"Result: {final_diagnostic}")