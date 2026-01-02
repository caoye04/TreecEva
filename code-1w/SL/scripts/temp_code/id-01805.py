from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings
def process_sensor_array(raw_data, config):
    temp_log = []
    error_flags = []
    mode_registry = defaultdict(int)
    diagnostic_trace = {}
    aggregate_stats = {'max_val': float('-inf'), 'min_val': float('inf'), 'sum_sq': 0}

    for idx, entry in enumerate(raw_data):
        # Real computation path begins
        if len(entry) < 3:
            continue

        # Distractor: irrelevant mode tracking
        mode_code = entry[0] % 7
        mode_registry[mode_code] += 1

        # Real transformation: extract and transform values
        val_a = (entry[1] >> 2) & 15
        val_b = entry[2] & 255
        transformed = (val_a * 17 + val_b) ^ config['key']
        temp_log.append(transformed)

        # Distractor: fake error detection
        if transformed > 2000:
            error_flags.append(idx)
        if transformed < 0:
            diagnostic_trace[idx] = 'NEG_X'

        # Real statistical accumulation
        aggregate_stats['sum_sq'] += transformed * 1.5
        if transformed > aggregate_stats['max_val']:
            aggregate_stats['max_val'] = transformed
        if transformed < aggregate_stats['min_val']:
            aggregate_stats['min_val'] = transformed

    # Distractor: unused aggregation
    flag_count = len(error_flags)
    sorted_modes = sorted(mode_registry.items(), key=lambda x: -x[1])

    # Real intermediate result
    base_entropy = int(aggregate_stats['sum_sq'] / 100) & 0xFFFF

    # Dead code path: never used later
    if base_entropy < 50:
        backup_repair = [x ^ 0xFF for x in temp_log]
        for item in backup_repair:
            pass  # useless loop

    # Real data restructuring
    histogram = Counter(temp_log)
    top_values = sorted(histogram.keys(), reverse=True)[:5]

    # Distractor: string manipulation unrelated to output
    signature_str = ''.join([chr((v % 26) + 97) for v in top_values if 0 <= (v % 26) + 97 <= 122])
    buffer_fragments = signature_str.split('a')

    # Real key derivation
    partial_key = 0
    for i, tv in enumerate(top_values):
        partial_key += tv * (i + 1)

    final_key = (partial_key ^ base_entropy) & 0xFFFF

    return final_key, aggregate_stats, temp_log

# Configuration with misleading parameters
config_params = {
    'key': 23,
    'threshold': 42,
    'timeout_ms': 999,
    'debug_mode': True,
    'retries': 3
}

# Simulated input data (deterministic)
sensor_input = [
    [123, 256, 100],
    [45, 192, 205],
    [67, 512, 150],
    [89, 384, 95],
    [101, 256, 300],
    [113, 128, 180],
    [125, 768, 140],
    [137, 640, 210]
]

# Main execution flow
result_key, stats, logs = process_sensor_array(sensor_input, config_params)

# State tracker with multiple decoy entries
state_tracker = {
    'init': 12345,
    'warmup': 67890,
    'calibration': 24680,
    'phase_1': 13579,
    'phase_2': 97531,
    'final': 86420
}

# Phases with irrelevant switching logic
current_status = 'active'
phase_sequence = ['init', 'warmup', 'calibration', 'phase_1', 'phase_2']
active_phase = 'phase_2'

# Misleading conditional block (dead logic)
if current_status == 'standby':
    adjustment = sum(state_tracker.values()) // len(state_tracker)
    result_key = result_key ^ adjustment

# Critical statement — answer depends on this
checksum = final_key ^ (state_tracker[active_phase] // 100)

# Irrelevant post-processing
shifted_logs = logs[::2]  # slicing - real but unused
reversed_logs = shifted_logs[::-1]
log_counter = Counter(reversed_logs)

# Another decoy function call
def validate_integrity(data_slice, ref_key):
    xor_sum = 0
    for d in data_slice:
        xor_sum ^= d
    return xor_sum == ref_key

# Unused validation
is_valid = validate_integrity(logs, 12345)

# Output the target result
print(f"Result: {checksum}")