from collections import defaultdict, Counter

# Simulate sensor data with noise and metadata
def preprocess_sensor_data(raw_readings):
    cleaned_data = []
    error_count = 0
    temporal_gaps = []

    for i, reading in enumerate(raw_readings):
        if not isinstance(reading, dict) or 'value' not in reading:
            error_count += 1
            continue
        
        raw_value = reading['value']
        timestamp = reading.get('ts', i)
        
        # Irrelevant transformation (distractor)
        normalized = (raw_value - 25.0) / 10.0 if raw_value > 0 else raw_value
        
        # Actual relevant processing
        if 10 <= raw_value <= 90:  # Valid range
            adjusted = raw_value * 1.08 + 2.3
            if i > 0:
                gap = timestamp - raw_readings[i-1].get('ts', i-1)
                temporal_gaps.append(gap)
            cleaned_data.append({'index': i, 'adjusted': adjusted, 'raw': raw_value})

    # Distractor computation: never used later
    avg_gap = sum(temporal_gaps) / len(temporal_gaps) if temporal_gaps else 0
    gap_variance = sum((g - avg_gap) ** 2 for g in temporal_gaps) / len(temporal_gaps) if temporal_gaps else 0

    return cleaned_data

# Analyze patterns in processed data
def analyze_trends(data_points):
    trend_stats = defaultdict(int)
    values = [pt['adjusted'] for pt in data_points]

    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_stats['increasing'] += 1
        elif values[i] < values[i-1]:
            trend_stats['decreasing'] += 1
        else:
            trend_stats['stable'] += 1

    # Red herring: complex but unused structure
    detailed_log = []
    for idx, (a, b) in enumerate(zip(values, values[1:])):
        change_type = 'positive' if b > a else 'negative' if b < a else 'no_change'
        magnitude = abs(b - a)
        detailed_log.append(f"{change_type}:{magnitude:.2f}")

    # Another distractor: character frequency in fake log tags
    char_freq = Counter(''.join(detailed_log).replace('.', '').replace(':', ''))
    rare_chars = [ch for ch, cnt in char_freq.items() if cnt < 2]

    return trend_stats

# Compute final diagnostic score
def compute_final_score(data_summary):
    base_score = 50
    
    # Weighted contributions
    inc = data_summary.get('increasing', 0)
    dec = data_summary.get('decreasing', 0)
    stable = data_summary.get('stable', 0)
    total_transitions = inc + dec + stable
    
    if total_transitions == 0:
        return base_score
    
    # Core logic: stability boosts score
    stability_factor = stable / total_transitions
    volatility_penalty = (abs(inc - dec) / total_transitions) * 15
    
    # Hidden key calculation
    adjustment = int(stability_factor * 40) - int(volatility_penalty)
    final_score = base_score + adjustment
    
    # Dead code branch (never executed due to logic above)
    if total_transitions < 0:
        fallback = sum(len(key) * val for key, val in data_summary.items())
        final_score = max(final_score, fallback)
    
    return final_score

# Main execution flow
if __name__ == "__main__":
    raw_input = [
        {'value': 20, 'ts': 100},
        {'value': 35, 'ts': 105},
        {'value': 36, 'ts': 110},
        {'value': 36, 'ts': 115},
        {'value': 42, 'ts': 120},
        {'value': 41, 'ts': 125},
        {'value': 41, 'ts': 130},
        {'value': 55, 'ts': 135}
    ]
    
    # Step 1: Preprocess
    processed_data = preprocess_sensor_data(raw_input)
    
    # Step 2: Analyze trends (key intermediate result)
    trend_analysis = analyze_trends(processed_data)
    
    # Step 3: Compute final score (target point)
    final_score = compute_final_score(trend_analysis)
    
    # Output result
    print(f"Result: {final_score}")