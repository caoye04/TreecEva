def process_diagnostics(raw_data, config):
    # Irrelevant preprocessing block (red herring)
    temp_buffer = [x ** 0.5 for x in raw_data if x > 10]
    normalization_factor = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 1.0

    # Distractor: unused transformation path
    def transform_legacy(arr):
        return [a * 1.05 for a in arr if a % 2 == 0]
    legacy_output = transform_legacy(raw_data)  # Dead code path

    # Real signal extraction
    timing_log = []
    errors_observed = []
    severity_weights = {'timeout': 3, 'retry': 1, 'drop': 5}

    for idx, entry in enumerate(raw_data):
        if entry < 0:
            errors_observed.append('drop')
        elif 5 <= entry < 15:
            errors_observed.append('retry')
        elif entry >= 100:
            timing_log.append(entry * 0.1)
        else:
            # Complex condition with slicing distraction
            binary_rep = bin(entry)[2:]
            ones_count = binary_rep.count('1')
            if ones_count > 2:
                shifted = entry >> (ones_count % 3)
                timing_log.append(shifted / 2.5)

    # Misleading aggregation (not used)
    fake_average = sum([x for x in timing_log if x < 10]) / len(timing_log) if timing_log else 0

    # Character counting distractor
    log_string = "diagnostics_run_complete"
    char_freq = {c: log_string.count(c) for c in set(log_string)}
    entropy_proxy = sum(f * f for f in char_freq.values())  # Unused metric

    # Conditional expression with zip and enumerate (core feature usage)
    indexed_pairs = list(zip(enumerate(timing_log), enumerate(errors_observed)))
    adjustment_factor = 1.0
    for (i1, t_val), (i2, e_type) in indexed_pairs:
        if i1 == i2:  # Synchronization check
            if e_type == 'retry':
                adjustment_factor *= 0.9
            elif e_type == 'drop':
                adjustment_factor -= 0.1

    # Decoy function call (no side effects)
    def calculate_shadow_index(data):
        return sum(d ** 2 for d in data) % 7
    shadow_index = calculate_shadow_index(raw_data)  # Not used

    # Actual computation path
    def aggregate_metrics(times, errors):
        base_score = sum(times)
        penalty = 0
        for e in errors:
            penalty += severity_weights.get(e, 0)
        # Key result computed here
        return int(base_score - penalty) + len(errors)  # Final logic step

    final_diagnostic = aggregate_metrics(timing_log, errors_observed)
    
    # Output required format
    print(f"Target result: {final_diagnostic}")

# Input data with deterministic behavior
input_data = [12, -5, 100, 24, 8, 200, 3, 150]
config_params = {'mode': 'strict', 'threshold': 10}
process_diagnostics(input_data, config_params)