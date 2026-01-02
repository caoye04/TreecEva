from collections import defaultdict, Counter

# Simulated network packet analysis system
def analyze_packets(packets):
    stats = defaultdict(int)
    temporal_marks = []
    cumulative_shift = 0

    for pkt in packets:
        size = len(pkt['data'])
        delay = pkt['delay']
        flags = pkt['flags']

        # Relevant computation branch
        if size > 500 and delay < 100:
            stats['large_low_delay'] += 1
            phase = (size // 100) ^ int(delay)
            cumulative_shift ^= phase & 0xFF

        # Distractor: irrelevant timing heuristics
        timestamp = pkt.get('ts', 0)
        jitter_estimate = abs(delay - 50) * 1.5 if timestamp else 0
        if jitter_estimate > 20:
            stats['jitter_alerts'] += 1

        # Red herring: unused transformation
        encrypted_ref = ''.join([chr((ord(c) + 3) % 97 + 32) for c in pkt['data'][:10]])
        temporal_marks.append(len(encrypted_ref))

    return stats, cumulative_shift

# Legacy diagnostic function (dead code path)
def legacy_diagnostic(trace_log):
    warnings = 0
    for entry in trace_log:
        if 'ERR' in entry:
            warnings += 1
    return warnings  # Never called

# Core evaluation logic
def compute_efficiency(records):
    efficiency_map = {}
    total_weight = 0.0

    for r in records:
        raw_value = r['value']
        quality = r['quality']
        age = r['age']

        adjusted = raw_value * (0.95 ** age)
        if quality == 'high':
            adjusted *= 1.2
        elif quality == 'low':
            adjusted *= 0.8

        # Meaningful intermediate used later
        normalized = round(adjusted / 4.0, 3)
        efficiency_map[r['id']] = normalized
        total_weight += normalized

    # Return distractor-heavy structure
    return {
        'map': efficiency_map,
        'sum': total_weight,
        'meta': {'version': '2.1', 'valid': True}
    }

# Main performance evaluator
def evaluate_performance(metrics):
    result_set = []
    debug_flags = []
    shift_accumulator = 0

    # Real data processing
    for m in metrics:
        category = m['cat']
        baseline = m['base']
        readings = m['readings']

        # Key calculation chain
        base_modified = baseline << 2
        reading_sum = sum(r['val'] for r in readings)
        composite = base_modified + reading_sum

        # Conditional expression with side effect
        status_flag = 1 if composite > 5000 else -1
        debug_flags.append(status_flag)

        # Bit manipulation relevant to final answer
        temp_key = composite ^ 0xAAAA
        temp_key = (temp_key >> 4) | (temp_key << 12) & 0xFFFF
        shift_accumulator += temp_key

        # Decoy statistical analysis
        counts = Counter([r['type'] for r in readings])
        entropy_proxy = 0
        for k, v in counts.items():
            if v > 2:
                entropy_proxy += v ** 0.5

        # Unused but plausible result
        result_set.append({
            'id': m['id'],
            'score': composite * 0.1,
            'entropy': round(entropy_proxy, 4)
        })

    # Final computation that determines answer
    raw_final = shift_accumulator ^ 0x5555
    adjustment = len(debug_flags) * 17
    final_score = (raw_final + adjustment) % 100000

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Irrelevant helper (distractor)
def format_timestamp(ts):
    hours = (ts // 3600) % 24
    mins = (ts // 60) % 60
    secs = ts % 60
    return f"{hours:02}:{mins:02}:{secs:02}"

# Setup realistic input data
packet_data = [
    {'data': 'X' * 600, 'delay': 80, 'flags': 0x01, 'ts': 12345},
    {'data': 'Y' * 400, 'delay': 200, 'flags': 0x02},
    {'data': 'Z' * 700, 'delay': 60, 'flags': 0x04}
]

record_list = [
    {'id': 1, 'value': 150, 'quality': 'high', 'age': 2},
    {'id': 2, 'value': 200, 'quality': 'medium', 'age': 1},
    {'id': 3, 'value': 100, 'quality': 'low', 'age': 3}
]

metric_data = [
    {
        'id': 'A1',
        'cat': 'throughput',
        'base': 1200,
        'readings': [
            {'val': 450, 'type': 'peak'},
            {'val': 320, 'type': 'avg'},
            {'val': 180, 'type': 'peak'},
            {'val': 250, 'type': 'avg'}
        ]
    },
    {
        'id': 'A2',
        'cat': 'latency',
        'base': 800,
        'readings': [
            {'val': 600, 'type': 'avg'},
            {'val': 400, 'type': 'peak'},
            {'val': 300, 'type': 'avg'}
        ]
    }
]

# Execute core analysis
packet_stats, shift_out = analyze_packets(packet_data)
efficiency_result = compute_efficiency(record_list)
final_score = evaluate_performance(metric_data)