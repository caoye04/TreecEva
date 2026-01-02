def analyze_temperature_trends(raw_readings):
    # Preprocess temperature data from sensor logs
    cleaned_readings = []
    outlier_count = 0
    total_adjustment = 0.0

    for reading in raw_readings:
        stripped = reading.strip()
        if stripped.startswith('T') and stripped.endswith('C'):
            try:
                temp_str = stripped[1:-1]
                if '.' in temp_str:
                    temp_val = float(temp_str)
                else:
                    temp_val = int(temp_str)
                if -50 <= temp_val <= 60:
                    cleaned_readings.append(temp_val)
                else:
                    outlier_count += 1
            except ValueError:
                continue

    # Irrelevant transformation: reverse string representations
    reversed_strings = [r[::-1] for r in raw_readings if isinstance(r, str)]
    dummy_sum = sum(len(s) for s in reversed_strings)  # Dead-end computation

    # Compute moving average over valid readings
    smoothed = []
    window_size = 3
    for i in range(len(cleaned_readings) - window_size + 1):
        window_avg = sum(cleaned_readings[i:i+window_size]) / window_size
        smoothed.append(round(window_avg, 2))

    # Simulate data confidence based on stability
    fluctuation = max(smoothed) - min(smoothed) if smoothed else 0
    stability_score = 100 - (fluctuation * 2)

    # Secondary irrelevant calculation: character frequency analysis
    all_chars = ''.join(raw_readings)
    char_freq = {c: all_chars.count(c) for c in set(all_chars)}
    rare_char_penalty = sum(1 for freq in char_freq.values() if freq < 2)

    return {
        'trends': smoothed,
        'stability': stability_score,
        'outliers_removed': outlier_count,
        'char_anomalies': rare_char_penalty
    }


def calculate_final_score(analysis_result):
    base_score = analysis_result['stability']
    outlier_penalty = analysis_result['outliers_removed'] * 1.5
    anomaly_deduction = analysis_result['char_anomalies'] * 0.7
    adjusted_score = base_score - outlier_penalty - anomaly_deduction
    
    # Apply non-linear boost if trend consistency is high
    trend_data = analysis_result['trends']
    if len(trend_data) > 1:
        increasing_trends = sum(1 for i in range(1, len(trend_data)) if trend_data[i] > trend_data[i-1])
        consistency_ratio = increasing_trends / (len(trend_data) - 1)
        if consistency_ratio > 0.7:
            adjusted_score *= 1.2
    
    return round(adjusted_score, 2)

# Main execution
sensor_logs = [
    'T23C', 'T24C', 'T25C', 'T26C', 'T24C',
    'T99C', 'T22C', 'T21C', 'T20C', 'T-1C',
    'TXYZC', 'T19C', 'T20C', 'T22C', 'T23C',
    'T25C', 'T26C', 'T27C', 'T28C', 'T29C'
]

processed_data = analyze_temperature_trends(sensor_logs)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")