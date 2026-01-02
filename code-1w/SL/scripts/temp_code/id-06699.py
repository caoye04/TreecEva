import itertools

def analyze_readings(readings):
    # Irrelevant transformation (distractor)
    normalized = [r * 0.98 + 2 for r in readings]
    filtered = [r for r in readings if r > 50]  # Only original readings used
    return sum(filtered) // len(filtered) if filtered else 0

def compute_entropy(data):
    # Dead code path - never used in final computation
    from math import log
    total = sum(data)
    if total == 0:
        return 0.0
    probabilities = [d / total for d in data]
    entropy = -sum(p * log(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def detect_anomalies(seq, limit):
    # Unused anomaly detector (red herring)
    anomalies = []
    for i in range(1, len(seq)):
        if abs(seq[i] - seq[i-1]) > limit:
            anomalies.append(i)
    return anomalies

def aggregate_signals(signals):
    # Decoy aggregation function with complex logic but no impact
    grouped = {}
    for idx, val in enumerate(signals):
        key = idx % 4
        grouped.setdefault(key, []).append(val)
    
    processed = {}
    for k, v in grouped.items():
        processed[k] = (sum(v) / len(v)) * (k + 1)
    
    return {k: round(v, 2) for k, v in processed.items()}

def extract_critical(signal_stream):
    # Relevant but obfuscated intermediate step
    pivot = len(signal_stream) // 2
    left_half = signal_stream[:pivot]
    right_half = signal_stream[pivot:]
    
    # Misleading comment: "Use right half for calibration"
    # Actually, only left half contributes to result
    adjustment = sum(left_half) % 7
    return adjustment * 2

def process_metrics(data, thresh):
    # Core logic hidden among distractions
    base_score = 0
    
    # Real computation begins
    valid_entries = [x for x in data if isinstance(x, dict) and 'level' in x]
    levels = [entry['level'] for entry in valid_entries]
    
    if not levels:
        return -1
    
    avg_level = sum(levels) / len(levels)
    
    # Conditional expression (required feature)
    penalty = 15 if avg_level < thresh else 5
    
    # Bit manipulation red herring
    masked = [l ^ 3 for l in levels]  # Never used
    
    # Real contribution: count of high-risk entries
    high_risk_count = sum(1 for l in levels if l > 85)
    
    # Lambda function usage (required feature)
    scale_factor = lambda x: x * 1.75 if x > 1 else 1.0
    
    # Itertools basic usage - grouping consecutive values above threshold
    sorted_levels = sorted([l for l in levels if l > thresh], reverse=True)
    grouped_streaks = [list(group) for k, group in itertools.groupby(sorted_levels, key=lambda x: x > 75)]
    longest_streak = max(len(g) for g in grouped_streaks) if grouped_streaks else 0
    
    # Final formula combines multiple concepts
    base_score += int(avg_level)
    base_score -= penalty
    base_score += high_risk_count * 12
    base_score += extract_critical(levels)  # Uses extracted logic
    base_score += int(scale_factor(longest_streak))
    
    # Final irrelevant transformation (misleading)
    diagnostic_code = base_score ^ 0xFF  # Looks important, unused
    
    return base_score  # Actual return value

# Main execution
if __name__ == '__main__':
    # Simulated health monitoring data stream
    raw_signal = [68, 72, 71, 69, 75, 88, 91, 87, 76, 73]
    
    # Irrelevant preprocessing chain
    smoothed = [int((a + b + c) / 3) for a, b, c in zip(raw_signal, raw_signal[1:], raw_signal[2:])]
    enhanced = [x + 5 if x < 70 else x - 3 for x in smoothed]
    
    # Real input structure
    health_data = [
        {'id': 'A1', 'level': 68, 'type': 'vital'},
        {'id': 'B2', 'level': 72, 'type': 'vital'},
        {'id': 'C3', 'level': 95, 'level': 88},  # Duplicate key (intentional, last wins)
        {'level': 55},  # Missing id
        {'level': 91},
        {'level': 45},  # Below threshold
        {'level': 87},
        {'extra': 'ignored'}
    ]
    
    # Multiple decoy variables
    entropy_metric = compute_entropy(smoothed)
    anomaly_positions = detect_anomalies(enhanced, 10)
    aggregated_signals = aggregate_signals(raw_signal)
    baseline_ref = analyze_readings(raw_signal)
    
    threshold = 60
    final_diagnostic = process_metrics(health_data, threshold)
    
    # Print required result
    print(f"Result: {final_diagnostic}")