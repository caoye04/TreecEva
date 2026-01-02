import itertools

# Simulated system diagnostics with mixed data types
def collect_diagnostics():
    base_values = [3, 7, 2, 8, 5]
    offsets = (1, -1, 0)
    computed = []
    temp_accumulator = 0

    for i in range(len(base_values)):
        shifted = base_values[i] + offsets[i % 3]
        if shifted > 5:
            computed.append(shifted * 2)
        else:
            computed.append(shifted - 1)
    
    # Irrelevant transformation chain (distractor)
    flipped = [x for x in reversed(computed)]
    reshaped = [[flipped[i], flipped[i+1]] for i in range(0, len(flipped)-1, 2)]
    flat_copy = list(itertools.chain.from_iterable(reshaped))
    checksum = sum(flat_copy) % 97

    # Relevant derived metric
    magnitude = sum(computed) / len(computed)

    return computed, magnitude, checksum


def evaluate_thresholds(metrics):
    raw_data, avg_val, check = metrics
    
    # Dead code path (distractor)
    if check < 0:
        normalization = [x / 100 for x in raw_data]
    else:
        normalization = raw_data  # No actual scaling

    # Semi-relevant filtering
    filtered = [x for x in normalization if x >= avg_val]
    
    # Extra string processing (distractor)
    label_set = {'A', 'B', 'C'}
    status_flags = set(''.join([f'F{x}' for x in filtered]).upper().split('F')[1:])
    active_flags = {s for s in status_flags if s.isdigit()}

    # Actual logic contribution
    flag_count = len(active_flags)
    peak = max(filtered) if filtered else 0

    return peak, flag_count, raw_data

def generate_context(features):
    peak_metric, count, sequence = features
    
    # String manipulation chain (mostly irrelevant)
    tag = "SYS_" + "_".join(str(int(x)) for x in sequence[:3]).zfill(2)
    clean_tag = tag.lower().replace("sys", "core").strip("_")
    parts = clean_tag.split("_")
    token = ''.join(p[0] for p in parts if p).upper()
    
    # Dummy dictionary construction (distractor)
    metadata_map = {k: v for k, v in zip(parts, itertools.cycle([True, False]))}
    validity = all(metadata_map.values())

    # Only this affects output
    adjustment = 3 if token.startswith("C") else 5

    return adjustment, peak_metric, count

def process_metrics(summary, config_flags):
    adj, peak, flag_num = summary
    mode_flag = config_flags.get('strict_mode', False)
    override = config_flags.get('bypass_limit', None)
    
    # Complex conditional expression
    base = peak * adj
    if mode_flag and override is not None:
        applied = base // override
    elif not mode_flag:
        applied = base + flag_num * 2
    else:
        applied = base - 7

    # Final computation with red herring
    history_log = [base, applied]
    snapshot = ':'.join(f'{h:.0f}' for h in history_log)
    entropy = hash(snapshot) % 1000  # Unused

    final_score = applied + 10
    return final_score

# Main execution flow
diag_output = collect_diagnostics()
eval_features = evaluate_thresholds(diag_output)
context_params = generate_context(eval_features)

flags = {
    'strict_mode': False,
    'bypass_limit': None,
    'debug_trace': True,
    'buffer_size': 256
}

final_score = process_metrics(context_params, flags)
print(f"Target result: {final_score}")