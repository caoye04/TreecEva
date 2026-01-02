def analyze_efficiency(data, config):
    # Irrelevant helper function (dead code path)
    temp = 0
    for k in config:
        temp += len(k) * data.get(k, 0)
    return temp * 0.5


def validate_integrity(checksums):
    # Distractor function with misleading intermediate logic
    total = 0
    for val in checksums:
        if val % 3 == 0 and val % 5 != 0:
            total += val ** 2
    return total - 100


def transform_metrics(raw):
    # Real transformation used later
    transformed = {}
    for k, v in raw.items():
        if 'latency' in k:
            transformed[k] = round(1000 / (v + 1), 3)
        elif 'throughput' in k:
            transformed[k] = v * 1.25
    return transformed


def compute_weighted_sum(vals):
    # Unused but plausible-looking computation
    weights = [0.1, 0.2, 0.3, 0.4][:len(vals)]
    return sum(v * w for v, w in zip(vals, weights))


def evaluate_performance(met, benches):
    # Core logic buried in distractions
    base = 0
    bonus = 0
    penalties = 0

    # Relevant dictionary operations and conditional expressions
    latency_keys = [k for k in met if 'latency' in k]
    throughput_keys = [k for k in met if 'throughput' in k]

    for key in latency_keys:
        score = met[key]
        # Only entries with 'critical_' prefix matter
        if 'critical_' in key:
            base += score * 2
            if score < 50:
                bonus += 10

    for key in throughput_keys:
        score = met[key]
        base += score // 4
        if score > 200:
            bonus += 5

    # Modular arithmetic red herring
    cyclic_mod = (len(benches) * bonus) % 7
    if cyclic_mod > 3:
        penalties -= 5

    # Real conditional logic determining final result
    adjustment = 1.1 if 'stress_test' in benches else 0.9
    
    # Decoy dictionary usage
    decoy_map = {i: i*3 + 2 for i in range(15)}
    decoy_sum = sum(v for v in decoy_map.values() if v % 4 == 0)

    # Actual answer derivation
    raw_final = (base + bonus - penalties) * adjustment
    final_score = int(round(raw_final))

    # Dead code: never accessed
    debug_trace = {'steps': [], 'flags': set()}
    if raw_final < 0:
        debug_trace['flags'].add('NEG')

    return final_score

# Main execution block
if __name__ == '__main__':
    # Input setup with mixed relevance
    metrics = {
        'latency_critical_p99': 45,
        'latency_normal_p95': 80,
        'throughput_critical': 220,
        'throughput_background': 150,
        'power_draw_watts': 65,
        'thermal_throttle_count': 3
    }

    benchmarks = ['unit_test', 'integration_test', 'stress_test']

    # Irrelevant preprocessing
    processed_data = {k.upper(): v for k, v in metrics.items() if 'p' in k}
    extra_config = {k: len(k) for k in benchmarks}

    # Call distractor functions to mislead analysis
    dummy_1 = analyze_efficiency(metrics, benchmarks)
    dummy_2 = validate_integrity([15, 18, 20, 25])

    # Key statement: this determines the actual answer
    final_score = evaluate_performance(metrics, benchmarks)

    # Output must follow required format
    print(f"Target result: {final_score}")