def analyze_sequence(data):
    # Irrelevant transformation: character counting in hex representation
    hex_str = ''.join(format(x, 'x') for x in data)
    char_count = {c: hex_str.count(c) for c in set(hex_str)}

    # Distractor: unused recursive function for summing squares
    def sum_squares_recursive(arr):
        if not arr:
            return 0
        return arr[0]**2 + sum_squares_recursive(arr[1:])

    # Real logic begins: filter and transform based on conditions
    filtered = [x for x in data if x > 0 and (x % 2) == 1]  # Keep positive odds
    shifted = [(x << 1) + 1 for x in filtered]  # Bit manipulation: left shift and add 1

    # Decoy structure: complex but unused data aggregation
    stats = {
        'max': max(shifted, default=0),
        'min': min(shifted, default=0),
        'range': max(shifted, default=0) - min(shifted, default=0),
        'count_map': {i: v for i, v in enumerate(shifted)}
    }

    # Actual relevant computation chain
    cumulative = 0
    for i, val in enumerate(shifted):
        if i % 2 == 0:
            cumulative += val * (i + 1)
        else:
            cumulative -= val // (i + 1)

    return cumulative


def process_timestamps(times):
    # Misleading time-based logic (never used)
    avg_gap = sum(times[i+1] - times[i] for i in range(len(times)-1)) / (len(times)-1) if len(times) > 1 else 0
    normalized = [t / (avg_gap + 1) for t in times]
    return [round(n) for n in normalized]


def evaluate_performance(metrics, base):
    # Core logic hidden among distractions
    adjustment = 0
    for k, v in metrics.items():
        if 'score' in k:
            adjustment += v * 0.1
        elif 'flag' in k:
            adjustment -= 5 if v else 0

    # Critical slicing operation
    values = list(metrics.values())
    slice_sum = sum(values[1:4]) if len(values) >= 4 else 0

    # Key use of zip and enumerate together
    pairs = list(zip(values, base))
    correlation = 0
    for idx, (v, b) in enumerate(pairs):
        if idx % 2 == 0:
            correlation += (v - b)
        else:
            correlation -= (v + b) // 2

    # Final calculation
    raw = metrics['initial_score'] + slice_sum + correlation + adjustment
    return int(raw)

# Main execution flow
if __name__ == '__main__':
    # Input data with red herring elements
    sensor_data = [3, -2, 7, 0, 5, 8, 1]
    timestamps = [120, 245, 379, 501, 632]

    # Unused recursion result
    dummy_sum = analyze_sequence([1, 2, 3])

    # Real data path
    processed_value = analyze_sequence(sensor_data)

    # Build metric dictionary with decoys
    performance_metrics = {
        'initial_score': processed_value,
        'temporal_flag': False,
        'calibration_score': 42,
        'stability_score': 18,
        'consistency_flag': True,
        'debug_mode': True,
        'final_adjustment': 7
    }

    baseline_ref = [10, 20, 30, 40, 50]

    # Dead code: unused conditional branch
    if len(performance_metrics) > 10:
        extra_comp = [x * 2 for x in baseline_ref if x < 35]
        baseline_ref.extend(extra_comp)

    # Critical statement
    final_score = evaluate_performance(performance_metrics, baseline_ref)

    print(f"Result: {final_score}")