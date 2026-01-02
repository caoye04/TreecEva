def analyze_system_load(raw_data, config):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.05 for x in raw_data if x > 0]
    adjusted = [n - 0.5 for n in normalized]
    outliers = [val for val in adjusted if val > 90]
    
    # Real computation begins: extract critical timestamps
    timestamps = [entry.split(' ')[0] for entry in config['logs']]
    valid_times = []
    for ts in timestamps:
        parts = ts.split(':')
        hour = int(parts[0])
        minute = int(parts[1])
        second = int(parts[2])
        if hour % 2 == 0 and minute < 45:
            valid_times.append(hour + minute / 60 + second / 3600)
    
    # Misleading statistical block (dead path)
    mean_time = sum(valid_times) / len(valid_times) if valid_times else 0
    variance = sum((t - mean_time) ** 2 for t in valid_times) / len(valid_times) if valid_times else 0
    peak_window = max(valid_times) - min(valid_times) if valid_times else 0

    # Core logic disguised among distractions
    event_codes = []
    for log in config['logs']:
        message = log.split(' ', 1)[1]
        code = sum(ord(c) for c in message[:10]) % 17
        event_codes.append(code)
    
    # Actual metric calculation
    severity_scores = [abs(code - 8) * 1.5 for code in event_codes]
    aggregate_risk = sum(severity_scores) / len(severity_scores)

    # Decoy function call (never used)
    def calculate_fallback_score():
        return sum(adjusted) % 100
    
    # Conditional expression with slicing distraction
    status_flag = 'CRITICAL' if aggregate_risk > 7 else 'OK'
    recent_logs = config['logs'][-5:]
    recent_chars = ''.join(recent_logs)[:20]
    char_sum = sum(ord(c) % 10 for c in recent_chars)

    # Key red herring: complex but unused bit manipulation
    bit_analysis = 0
    for i in range(len(outliers)):
        bit_analysis ^= int(outliers[i])
        bit_analysis <<= 1
        if bit_analysis > 1000:
            bit_analysis >>= 3
    
    # Actual answer derivation
    base_metric = aggregate_risk * char_sum
    final_diagnostic = int(base_metric - (char_sum // 3))
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic


def process_metrics(log_entries, system_thresholds):
    # Simulate secondary path (not taken)
    if not log_entries:
        return -999
    
    # Real work: filter logs by threshold keywords
    filtered = [log for log in log_entries if any(t in log for t in system_thresholds)]
    scores = []
    for entry in filtered:
        words = entry.split(' ')
        # Use conditional expression and slicing
        score = sum(len(w) for w in words if w.isalpha())
        modifier = 0.8 if 'WARN' in words else 1.2
        scores.append(score * modifier)
    
    # Compute average, then apply non-linear transform
    avg_score = sum(scores) / len(scores) if scores else 0
    transformed = (avg_score ** 2) / 4.5
    
    # Unused backup logic (distraction)
    fallback_rank = 0
    for s in scores:
        fallback_rank += int(s) & 7
        fallback_rank -= fallback_rank % 4

    # Final result derived from main logic
    return int(transformed)

# Main execution with realistic data
if __name__ == '__main__':
    sensor_readings = [88.2, -1, 91.5, 87.0, 0, 93.1, 89.8]
    system_config = {
        'logs': [
            '12:30:45 SYS_OK: nominal operation',
            '13:15:22 ALERT: voltage fluctuation',
            '14:05:10 WARN: high temperature detected',
            '15:50:33 INFO: scheduled maintenance',
            '16:20:01 CRITICAL: overload condition'
        ],
        'version': '2.1.5',
        'active': True
    }
    thresholds = ['WARN', 'CRITICAL', 'ALERT']
    
    # Call to trigger real computation
    log_data = system_config['logs']
    final_diagnostic = process_metrics(log_data, thresholds)
    
    # Additional irrelevant transformations
    temp_array = [final_diagnostic + i for i in range(5)]
    shifted = temp_array[1:] + [temp_array[0]]
    checksum = sum(shifted[i] * (i+1) for i in range(len(shifted)))
    
    # Print final result as required
    print(f"Result: {final_diagnostic}")