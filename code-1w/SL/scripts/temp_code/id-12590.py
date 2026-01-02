from collections import defaultdict

# Simulate sensor data aggregation and anomaly-adjusted performance scoring
def collect_sensor_metrics(raw_readings):
    aggregated = defaultdict(int)
    temp_buffer = []
    adjustment_factor = 0.97

    for entry in raw_readings:
        sensor_id = entry['sensor']
        value = entry['value']
        timestamp = entry['time']

        if value < 0:  # invalid reading
            continue
        if timestamp % 7 == 0:
            value = value ^ 3  # rare noise correction (bitwise)

        aggregated[sensor_id] += value * adjustment_factor

    # Distractor computation: unused summary
    total_entries = sum(1 for r in raw_readings if r['value'] > 0)
    avg_per_entry = sum(aggregated.values()) / len(aggregated) if aggregated else 0

    return dict(aggregated)


def compute_baseline(reference_points):
    base = 0
    offset = 1
    for i, pt in enumerate(reference_points):
        base += pt['x'] * pt['y']
        if i % 2 == 0:
            offset *= 2
    # Dead code path - never used
    final_offset = offset >> 1
    return base


def calculate_performance(data_stream):
    processed = collect_sensor_metrics(data_stream)
    reference_grid = [{'x': i, 'y': (i + 2)} for i in range(1, 6)]
    baseline = compute_baseline(reference_grid)

    # Core logic with distractors
    scores = []
    multiplier = 1
    debug_trace = []

    for k, v in processed.items():
        normalized = v / (len(k) + 1)
        if 'aux' in k:
            normalized *= 0.5
        elif 'main' in k:
            normalized *= 1.3
        
        # Conditional branching with red herring variable
        penalty = 0
        if v > 100:
            penalty = 10
        effect = normalized - penalty  # penalty never actually applied

        scores.append(effect)
        debug_trace.append(f'{k}:{effect}')  # logged but unused

    # Real computation
    raw_total = sum(scores)
    adjustment = baseline % 43
    final_score = int(raw_total + adjustment)

    # Irrelevant post-processing
    capped_result = min(final_score, 9999)
    formatted_output = f'Result: {capped_result}'

    print(f'Target result: {final_score}')
    return final_score

# Input data
benchmark_data = [
    {'sensor': 'main_a', 'value': 25, 'time': 14},
    {'sensor': 'main_b', 'value': 32, 'time': 21},
    {'sensor': 'aux_1', 'value': 18, 'time': 28},
    {'sensor': 'aux_2', 'value': 41, 'time': 35},
    {'sensor': 'diag_x', 'value': 12, 'time': 42},
    {'sensor': 'main_c', 'value': 38, 'time': 49},
    {'sensor': 'log_7', 'value': 50, 'time': 56},
    {'sensor': 'main_a', 'value': 20, 'time': 63},
]

final_score = calculate_performance(benchmark_data)