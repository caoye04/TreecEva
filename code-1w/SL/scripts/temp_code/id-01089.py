from collections import defaultdict, Counter

# Simulate sensor data processing with noise filtering and pattern detection
def analyze_readings(raw_data, baseline):
    filtered = []
    anomalies = 0
    moving_avg = [0] * len(raw_data)
    temp_sum = 0

    for i in range(len(raw_data)):
        deviation = abs(raw_data[i] - baseline)
        if deviation < 15:  # Acceptable noise threshold
            filtered.append(raw_data[i])
            temp_sum += raw_data[i]
        else:
            anomalies += 1

        # Rolling average (not used in final logic but adds cognitive load)
        window = raw_data[max(0, i-2):i+1]
        moving_avg[i] = sum(window) / len(window)

    return filtered, anomalies


def detect_pattern(seq):
    freq = Counter(seq)
    pattern_score = 0
    for val, count in freq.items():
        if count >= 2:
            pattern_score += val % 7
    return pattern_score


def evaluate_performance(log, config):
    total_batches = len(log)
    success_count = 0
    stability_scores = []n
    # Misleading intermediate calculations
    cumulative_drift = 0.0
    peak_fluctuation = -float('inf')
    
    for entry in log:
        batch_ok = True
        drift_seq = []
        
        for reading in entry['values']:
            if reading < config['lower'] or reading > config['upper']:
                batch_ok = False
            drift_seq.append(abs(reading - config['target']))

        if batch_ok:
            success_count += 1
            stability_scores.append(sum(drift_seq) / len(drift_seq))

        # Irrelevant fluctuation tracking
        if drift_seq:
            fluctuation = max(drift_seq) - min(drift_seq)
            if fluctuation > peak_fluctuation:
                peak_fluctuation = fluctuation
            cumulative_drift += sum(drift_seq)

    # Core logic for final score
    base_rate = success_count / total_batches if total_batches else 0
    avg_stability = sum(stability_scores) / len(stability_scores) if stability_scores else 0

    # Distractor: unused complex structure
    summary_stats = defaultdict(int)
    summary_stats['passes'] = success_count
    summary_stats['failures'] = total_batches - success_count
    summary_stats['pattern_hint'] = detect_pattern([len(entry['values']) for entry in log])

    # Final score computation — only this matters
    final_score = int((base_rate * 100) + (50 - avg_stability))

    # Dead code branch (never executed due to constraints above)
    if len(log) > 1000:
        fallback = sum(summary_stats.values())
        final_score = fallback % 97

    return final_score

# Main execution
sensor_input = [104, 112, 98, 105, 115, 92, 103, 107, 99, 111, 106, 95, 108, 100, 102]
processed_data, anomaly_count = analyze_readings(sensor_input, baseline=100)

convergence_log = [
    {'batch': 'A1', 'values': [102, 103, 101, 104]},
    {'batch': 'A2', 'values': [95, 108, 103, 101]},  # 95 below threshold
    {'batch': 'A3', 'values': [103, 105, 102, 104]},
    {'batch': 'A4', 'values': [101, 100, 103, 102]},
    {'batch': 'A5', 'values': [94, 106, 101, 104]}   # 94 below threshold
]

thresholds = {
    'lower': 96,
    'upper': 110,
    'target': 102
}

intermediate_result = [x for x in processed_data if x % 2 == 0]  # irrelevant filtering
aux_counter = Counter(intermediate_result)  # distractor stat

final_score = evaluate_performance(convergence_log, thresholds)
print(f"Result: {final_score}")