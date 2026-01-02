def sensor_diagnostic(raw_data, config):
    baseline = sum(raw_data) / len(raw_data) if raw_data else 0
    adjusted = [x - baseline + config.get('offset', 0) for x in raw_data]

    # Irrelevant transformation - dead path
    temp_analysis = [abs(x) ** 0.5 for x in adjusted if x > 0]
    temp_result = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0

    # Distractor: complex but unused filter
    filtered_noise = list(filter(lambda x: x % 2 == 1, [int(x) for x in adjusted]))
    noise_floor = max(filtered_noise) if filtered_noise else 0

    # Real processing begins
    processed = [round(x * config['gain'], 3) for x in adjusted]
    magnitude = sum(abs(x) for x in processed)
    peak = max(abs(x) for x in processed)

    # Conditional expression chain with red herring
    status_flag = 'nominal' if magnitude < 100 else 'elevated' if magnitude < 500 else 'critical'
    decay_factor = 0.9 if status_flag == 'nominal' else 0.6 if status_flag == 'elevated' else 0.3

    # Unused diagnostic path (distractor)
    historical_trend = [processed[i] - processed[i-1] for i in range(1, len(processed))] if len(processed) > 1 else []
    trend_slope = sum(historical_trend) / len(historical_trend) if historical_trend else 0

    # Bitwise manipulation decoy
    signature = 0
    for x in processed:
        truncated = int(abs(x)) & 0xFF
        signature ^= truncated
        signature = (signature << 1) | (signature >> 7)
    signature &= 0xFF

    return {
        'data': processed,
        'peak': peak,
        'status': status_flag,
        'decay': decay_factor,
        'meta': {
            'baseline': baseline,
            'temp_result': temp_result,
            'noise_floor': noise_floor,
            'trend_slope': trend_slope,
            'checksum': signature
        }
    }


def analyze_readings(readings, limits):
    if not readings:
        return -1

    # Extract real signal features
    high_signal = len([x for x in readings if abs(x) > limits['threshold_high']])
    mid_signal = len([x for x in readings if limits['threshold_low'] <= abs(x) <= limits['threshold_high']])
    
    # Complex conditional expression with weighted impact
    impact_score = (
        3 * high_signal + 
        1.5 * mid_signal + 
        (5 if max(readings) > 50 else 0) +
        (10 if min(readings) < -50 else 0)
    )

    # Distractor: elaborate unused classification
    categories = ['A', 'B', 'C', 'D']
    class_bins = {cat: 0 for cat in categories}
    for val in readings:
        if val > 40: class_bins['A'] += 1
        elif val > 20: class_bins['B'] += 1
        elif val > 0: class_bins['C'] += 1
        else: class_bins['D'] += 1
    
    # Secondary distraction: entropy-like calculation
    total = sum(class_bins.values())
    entropy = 0
    for count in class_bins.values():
        if count > 0 and total > 0:
            prob = count / total
            entropy -= prob * __import__('math').log(prob, 2)

    # Real decision logic
    severity = 'low'
    if impact_score >= 40:
        severity = 'critical'
    elif impact_score >= 20:
        severity = 'high'
    elif impact_score >= 10:
        severity = 'medium'

    # Final computation - only this matters
    scaling = 2.5 if severity == 'critical' else 1.8 if severity == 'high' else 1.2
    final_diagnostic = round(impact_score * scaling, 4)

    # Dead assignment - looks important but unused
    final_diagnostic += sum(class_bins[categories[i]] * (i+1) for i in range(4)) * 0.01

    return final_diagnostic

# Main execution
config = {'offset': 2.5, 'gain': 1.8}
thresholds = {'threshold_low': 15, 'threshold_high': 50}
raw_input = [12, -8, 45, 23, -67, 34, 11, -19, 52, -33]

# Execute pipeline
diagnostics = sensor_diagnostic(raw_input, config)
processed = diagnostics['data']
final_diagnostic = analyze_readings(processed, thresholds)

Result: {final_diagnostic}