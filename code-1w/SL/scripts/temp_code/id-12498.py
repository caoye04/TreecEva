from itertools import combinations

# Simulate sensor data quality assessment with scoring logic
def analyze_readings(readings):
    valid_count = sum(1 for r in readings if 0 <= r <= 100)
    total = len(readings)
    ratio = valid_count / total if total else 0
    
    # Distractor: entropy-like computation (not used in final score)
    entropy_proxy = 0
    freq_map = {}
    for r in readings:
        freq_map[r] = freq_map.get(r, 0) + 1
    for count in freq_map.values():
        if count > 0 and total > 0:
            p = count / total
            entropy_proxy -= p * __import__('math').log(p) if p > 0 else 0

    # Real signal: trend consistency
    increasing = sum(1 for i in range(1, len(readings)) if readings[i] > readings[i-1])
    decreasing = sum(1 for i in range(1, len(readings)) if readings[i] < readings[i-1])
    stable = sum(1 for i in range(1, len(readings)) if readings[i] == readings[i-1])
    trend_score = abs(increasing - decreasing)  # High difference means strong direction

    return ratio, trend_score, entropy_proxy  # entropy_proxy unused later


def validate_entry(entry):
    # Check format validity
    if not isinstance(entry, dict) or 'id' not in entry or 'values' not in entry:
        return False
    if not isinstance(entry['values'], list) or len(entry['values']) == 0:
        return False
    return all(isinstance(v, (int, float)) for v in entry['values'])


def calculate_stability_factor(trend_score, length):
    if length < 2:
        return 1.0
    max_possible_change = length - 1
    change_ratio = trend_score / max_possible_change
    return 0.5 + 0.5 * change_ratio  # Normalize to [0.5, 1.0]


def calculate_final_score(data, thresholds):
    cumulative_weight = 0.0
    total_confidence = 0.0
    anomaly_flags = []

    # Preprocess: filter valid entries
    valid_entries = [e for e in data if validate_entry(e)]

    # Distractor: collect all possible pairs (unused)
    all_ids = [e['id'] for e in valid_entries]
    pair_combinations = list(combinations(all_ids, 2))  # Computation without use
    pair_count = len(pair_combinations)

    base_multiplier = thresholds.get('base', 1.0)
    safety_margin = thresholds.get('margin', 0.1)

    intermediate_results = []

    for entry in valid_entries:
        readings = entry['values']
        validity_ratio, trend_score, _ = analyze_readings(readings)
        
        # Compute individual scores
        validity_score = validity_ratio * 100
        stability_factor = calculate_stability_factor(trend_score, len(readings))
        
        # Conditional expression for dynamic weighting
        weight = 1.2 if validity_ratio > 0.8 else (0.8 if validity_ratio > 0.6 else 0.5)
        
        # Score contribution
        contribution = (validity_score * stability_factor * weight)
        total_confidence += contribution
        cumulative_weight += weight
        
        # Flag anomalies
        is_anomalous = (validity_ratio < 0.5) or (len(readings) > 1 and trend_score / (len(readings)-1) > 0.9)
        anomaly_flags.append(is_anomalous)

        intermediate_results.append({
            'entry_id': entry['id'],
            'score': contribution,
            'validity': validity_ratio,
            'stable': stability_factor > 0.7
        })

    # Distractor: process intermediates in a way that doesn't affect output
    flagged_count = sum(1 for f in anomaly_flags if f)
    suppression_factor = 0.95 if flagged_count > 2 else 1.0

    # Final aggregation
    final_score = (total_confidence / cumulative_weight) if cumulative_weight else 0
    
    # Apply ceiling cap (real effect)
    if final_score > thresholds.get('cap', 95.0):
        final_score = thresholds['cap']

    # Irrelevant transformation
    final_score_str = f"{final_score:.3f}"
    final_score_ceil = __import__('math').ceil(final_score)

    # But we return original
    return final_score

# Main execution
if __name__ == "__main__":
    data = [
        {'id': 'A01', 'values': [85, 87, 88, 90, 92, 95]},
        {'id': 'B02', 'values': [100, 95, 90, 85, 80, 75]},
        {'id': 'C03', 'values': [50, 50, 101, -5, 60]},  # Contains invalid
        {'id': 'D04', 'values': [70, 72, 73, 73, 74, 76]},
        {'id': 'E05', 'values': [60, 60, 60, 60]},      # Stable
        {'id': 'F06', 'values': [10, 90, 10, 90, 10, 90]}  # Oscillating
    ]

    thresholds = {
        'base': 1.0,
        'margin': 0.05,
        'cap': 94.5
    }

    # Key execution point
    final_score = calculate_final_score(data, thresholds)
    print(f"Result: {final_score}")