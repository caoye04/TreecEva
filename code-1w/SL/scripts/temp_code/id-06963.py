import itertools

def analyze_sequence(data_stream):
    # Irrelevant helper function – never called
    cumulative = 0
    for val in data_stream:
        if val % 3 == 0:
            cumulative += val ** 2
        else:
            cumulative -= val
    return cumulative

def validate_checksum(chunk):
    # Dead code path – looks important but unused
    total = 0
    for i, b in enumerate(chunk):
        total ^= (b + i) * 3
    return total % 256

def main():
    # Simulated system telemetry
    sensor_ids = [101, 102, 103, 104]
    readings = [15.2, 18.7, 12.1, 19.3]
    timestamps = [1678886400, 1678886460, 1678886520, 1678886580]

    # Distractor: complex-looking but irrelevant data structure
    telemetry_grid = list(itertools.product(sensor_ids, ['OK', 'WARN']))
    grid_sum = sum(pair[0] for pair in telemetry_grid if 'WARN' in pair)

    # Real data used later
    log_entries = [
        {'id': 101, 'status': 'active', 'load': 0.45, 'errors': 2},
        {'id': 102, 'status': 'active', 'load': 0.78, 'errors': 1},
        {'id': 103, 'status': 'idle',   'load': 0.12, 'errors': 0},
        {'id': 104, 'status': 'active', 'load': 0.63, 'errors': 3}
    ]

    # Misleading intermediate computation
    baseline_score = 0
    for entry in log_entries:
        baseline_score += entry['load'] * 100
    baseline_score = int(baseline_score / len(log_entries))

    # Complex distractor with set operations and zip
    active_ids = {entry['id'] for entry in log_entries if entry['status'] == 'active'}
    expected_ids = {101, 102, 103, 104}
    missing = expected_ids - active_ids  # empty, but looks suspicious

    name_map = dict(zip(sensor_ids, ['Alpha', 'Beta', 'Gamma', 'Delta']))
    id_name_pairs = [(k, v) for k, v in name_map.items() if k in active_ids]

    # Bit manipulation red herring
    flag_packed = 0
    for shift in range(0, 8, 2):
        flag_packed |= (1 << shift)

    # Actual relevant flags
    system_flags = {
        'overload_threshold': 0.75,
        'critical_errors': 2,
        'grace_period': 30
    }

    # Decoy loop that accumulates nothing useful
    temp_buffer = []
    for _ in range(3):
        for combo in itertools.combinations_with_replacement([1, 2], 2):
            temp_buffer.append(sum(combo))

    # Key processing function (defined inside to obscure)
    def process_metrics(entries, config):
        overload_count = 0
        critical_count = 0
        total_load = 0.0

        for entry in entries:
            total_load += entry['load']
            if entry['load'] > config['overload_threshold']:
                overload_count += 1
            if entry['errors'] >= config['critical_errors']:
                critical_count += 1

        # Real logic hidden among distractions
        score_a = overload_count * 1000
        score_b = critical_count * 100
        base_index = int(total_load * 100)

        # Final diagnostic combines multiple factors
        result = base_index + score_a + score_b

        # Unused but plausible alternate path
        if overload_count == 0 and critical_count == 0:
            result = min(result, 5000)

        return result

    # Execution point of interest
    final_diagnostic = process_metrics(log_entries, system_flags)

    # Distractor: another unused transformation
    reshaped = list(itertools.chain.from_iterable(
        [(eid, load) for eid, load in zip(sensor_ids, readings) if load > 15.0]
    ))

    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()