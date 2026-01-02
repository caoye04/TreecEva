from collections import defaultdict, Counter
import math

# Simulated sensor data processing for industrial monitoring system
def collect_diagnostics():
    raw_readings = [189, 203, 198, 211, 195, 208, 197, 212, 201, 187]
    timestamps = list(range(1000, 1010))
    statuses = ['OK', 'WARNING', 'OK', 'CRITICAL', 'OK', 'WARNING', 'OK', 'CRITICAL', 'OK', 'OK']
    
    # Irrelevant transformation (distractor)
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)), 3) for x in raw_readings]
    
    # Relevant mapping
    diagnostics = []
    for i in range(len(raw_readings)):
        diagnostics.append({
            'value': raw_readings[i],
            'time': timestamps[i],
            'status': statuses[i]
        })
    
    return diagnostics

# Decoy function - looks important but unused
def analyze_trend(data):
    if not data:
        return 0
    diffs = [data[i+1] - data[i] for i in range(len(data)-1)]
    trend_score = sum(1 for d in diffs if d > 0) - sum(1 for d in diffs if d < 0)
    return abs(trend_score) * 1.5

# Real processing pipeline
def filter_critical_events(logs):
    critical_only = [entry for entry in logs if entry['status'] == 'CRITICAL']
    warning_only = [entry for entry in logs if entry['status'] == 'WARNING']  # unused
    
    # Distractor: complex but irrelevant calculation
    avg_gap = 0
    times = [entry['time'] for entry in logs]
    if len(times) > 1:
        gaps = [times[i+1] - times[i] for i in range(len(times)-1)]
        avg_gap = sum(gaps) / len(gaps)
    
    return critical_only

def compute_anomaly_weight(events):
    if not events:
        return 0.0
    
    # Real logic: weighted sum based on value magnitude
    weights = []
    for e in events:
        base_weight = e['value'] / 100.0
        time_component = (e['time'] % 100) * 0.01  # negligible influence
        weights.append(base_weight + time_component)
    
    return sum(weights)

def adjust_for_redundancy(anomalies):
    # Simulate duplicate detection using bit flags (overkill but plausible)
    seen_values = set()
    unique_count = 0
    for a in anomalies:
        val = a['value']
        flag = val ^ 0xFF  # bitwise red herring
        masked = (val & 0xF0) >> 4  # extract high nibble
        if val not in seen_values:
            seen_values.add(val)
            unique_count += 1
    return unique_count * 10

def generate_summary_stats(diagnostics):
    # Collect various stats, many irrelevant
    summary = defaultdict(int)
    status_count = Counter([d['status'] for d in diagnostics])
    
    summary['total'] = len(diagnostics)
    summary['ok_count'] = status_count['OK']
    summary['warning_count'] = status_count['WARNING']
    summary['critical_count'] = status_count['CRITICAL']
    
    values = [d['value'] for d in diagnostics]
    summary['mean_value'] = sum(values) / len(values)
    summary['peak_value'] = max(values)
    
    # Distractor: unused complex stat
    variance = sum((x - summary['mean_value'])**2 for x in values) / len(values)
    summary['std_dev'] = math.sqrt(variance)
    
    # Real use: only critical count matters later
    return summary

def evaluate_performance(metrics, threshold):
    # Core decision logic buried in distractions
    base = metrics['critical_count'] * 100
    
    # Multiple paths that look influential but aren't
    bonus = 0
    if metrics['mean_value'] > threshold:
        bonus += 25
        if metrics['peak_value'] > 210:
            bonus *= 1.2  # dead branch due to logic
    
    penalty = 0
    # This block appears relevant but condition never triggers
    fake_counter = 0
    for i in range(5):
        fake_counter += i * 2
        if fake_counter > 100:  # unreachable
            penalty += 10
    
    # Real penalty: hardcoded adjustment
    adjusted_base = base - 17
    
    # Final obfuscation via unnecessary function call
    multiplier = determine_scaling_factor(threshold)
    final = adjusted_base * multiplier
    
    return int(final)

def determine_scaling_factor(base):
    # Looks adaptive but returns constant
    candidates = [0.8, 0.9, 1.0, 1.1]
    selection_index = (base // 10) % 4
    # But actually always returns 1.0 due to base_threshold value
    return candidates[selection_index] if 0 <= selection_index < len(candidates) else 1.0

# Orchestration with decoy calls
def main_pipeline():
    # Step 1: collect data
    diagnostics_log = collect_diagnostics()
    
    # Step 2: extract critical events (used)
    critical_events = filter_critical_events(diagnostics_log)
    
    # Step 3: compute weight (partially used)
    anomaly_weight = compute_anomaly_weight(critical_events)
    
    # Step 4: count unique (unused result - red herring)
    uniqueness_score = adjust_for_redundancy(critical_events)
    
    # Step 5: generate full metrics (key step)
    metric_data = generate_summary_stats(diagnostics_log)
    
    # Step 6: apply evaluation (target statement)
    base_threshold = 200
    final_score = evaluate_performance(metric_data, base_threshold)
    
    # Distractor: unused derived values
    efficiency_ratio = anomaly_weight / (final_score + 1) if final_score != -1 else 0
    diagnostic_depth = len(diagnostics_log) // 2 + 3
    
    # Only this output matters
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main_pipeline()