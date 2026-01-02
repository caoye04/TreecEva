import itertools

# Simulated system telemetry data with mixed signal types
def generate_signals():
    base_values = [i * 2.5 for i in range(10)]
    offset = sum([x for x in base_values if x > 10]) / len(base_values)
    return [x + offset for x in base_values]

# Irrelevant auxiliary function – dead code path (distractor)
def calculate_redundancy_score(data):
    return sum(d ** 2 for d in data if d < 5) * 0.75

# Signal filter using lambda abstraction (relevant)
adaptive_filter = lambda signals, threshold: list(filter(lambda x: x > threshold, signals))

# Data enrichment with extraneous transformations (distractors)
def enrich_logs(raw_data):
    timestamps = list(range(len(raw_data)))
    labels = ['OK' if i % 2 == 0 else 'FLAG' for i in range(len(raw_data))]
    metadata_map = {t: {'label': l, 'seq_id': i} for i, (t, l) in enumerate(zip(timestamps, labels))}
    
    # Misleading intermediate computation (red herring)
    phantom_sum = sum((i * t) for i, t in enumerate(timestamps)) + 999
    
    # Actual payload augmentation
    entries = []
    for idx, val in enumerate(raw_data):
        entry = {
            'value': val,
            'timestamp': timestamps[idx],
            'status': labels[idx]
        }
        entries.append(entry)
    
    return entries

# Core processing chain (relevant logic)
def aggregate_anomalies(entries, limit):
    anomalies = []
    running_total = 0
    
    for e in entries:
        if e['status'] == 'FLAG' and e['value'] > limit:
            running_total += e['value'] * 0.1
            anomalies.append(running_total)
    
    # Dead branch - never executed due to data generation logic (misleading)
    if len(anomalies) == 0 and limit < 0:
        anomalies.append(-9999)
        
    return anomalies

# Higher-order reducer with itertools (relevant)
def reduce_with_window(data, window_size=3):
    grouped = [data[i:i+window_size] for i in range(0, len(data), window_size)]
    reduced = []
    for group in grouped:
        if len(group) == window_size:
            reduced.append(sum(group) / len(group))
        else:
            # This path is taken – contributes to result
            reduced.append(sum(g for g in group))
    return reduced

# Decoy function that looks important but is unused (distractor)
def compute_entropy(values):
    from math import log
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probs)

# Main diagnostic processor (critical path)
def process_metrics(logs, threshold):
    # Step 1: extract numeric values
    values = [entry['value'] for entry in logs]
    
    # Step 2: apply adaptive filter
    filtered = adaptive_filter(values, threshold)
    
    # Step 3: detect anomalies above dynamic floor
    anomaly_triggers = [v for v in filtered if v > threshold * 1.2]
    
    # Step 4: accumulate incremental flags
    accumulator = 0
    for a in anomaly_triggers:
        accumulator += a * 0.05
    
    # Step 5: simulate multi-stage integration
    temp_result = accumulator * 2.5
    
    # Step 6: apply windowed reduction via itertools-inspired grouping
    expanded = [temp_result + i*0.1 for i in range(5)]
    chunked = reduce_with_window(expanded, 2)
    
    # Step 7: final projection
    projection = sum(chunked) / len(chunked)
    
    # Step 8: normalization against baseline
    baseline_shift = sum(generate_signals()[::3]) * 0.01
    final_score = projection - baseline_shift
    
    return round(final_score, 6)

# Orchestration block
if __name__ == '__main__':
    # Generate raw signal input
    raw_signals = generate_signals()
    
    # Enrich into log format (includes distractor fields)
    log_entries = enrich_logs(raw_signals)
    
    # Define operational threshold
    system_threshold = 15.0
    
    # Dead variable – no effect on output (red herring)
    calibration_cycle = calculate_redundancy_score(raw_signals)
    
    # Critical execution point
    final_diagnostic = process_metrics(log_entries, system_threshold)
    
    # Output target result
    print(f"Result: {final_diagnostic}")