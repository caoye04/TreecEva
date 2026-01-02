import math

# Simulated system performance metrics (some are red herrings)
def collect_metrics():
    raw_data = {
        'latency_ms': 120,
        'throughput_ops': 450,
        'error_rate': 0.03,
        'cpu_load': 78.5,
        'mem_usage_mb': 2048,
        'disk_io_ops': 320,  # irrelevant metric
        'network_latency_ms': 45,  # misleading duplicate
        'redundant_flag': True,
        'temporal_factor': 1.05
    }

    # Distractor transformation: unused path
    if raw_data['redundant_flag']:
        adjusted = {}
        for k, v in raw_data.items():
            if 'ms' in k:
                adjusted[k] = v * 1.1
            elif isinstance(v, float) and k != 'error_rate':
                adjusted[k] = v * 0.95
        adjusted['computed_junk'] = sum([raw_data['cpu_load'], raw_data['mem_usage_mb']]) / 100

    # Actual normalized metrics used in calculation
    metrics = {
        'response_time': 1000 / (raw_data['latency_ms'] + 1),
        'scale': math.log(raw_data['throughput_ops']),
        'reliability': 1 - raw_data['error_rate'],
        'efficiency': (100 - raw_data['cpu_load']) / 100,
        'stability_factor': raw_data['temporal_factor']
    }

    # Dead code branch - never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print("Debug:", metrics)
        metrics['fake_correction'] = 0.0

    return metrics


def apply_weights(data_dict):
    # Multiple weight sets defined - only one used
    weights_v1 = {'response_time': 0.3, 'scale': 0.25, 'reliability': 0.2, 'efficiency': 0.15, 'stability_factor': 0.1}
    weights_v2 = {'response_time': 0.1, 'scale': 0.4, 'reliability': 0.3, 'efficiency': 0.1, 'stability_factor': 0.1}
    weights_v3 = {'response_time': 0.25, 'scale': 0.3, 'reliability': 0.25, 'efficiency': 0.15, 'stability_factor': 0.05}  # decoy

    # Correct weights used
    active_weights = weights_v1

    # Irrelevant dictionary operation
    inverse_map = {v: k for k, v in active_weights.items()}
    sorted_keys = sorted(inverse_map.keys())

    weighted_sum = 0.0
    for key in data_dict:
        if key in active_weights:
            weighted_sum += data_dict[key] * active_weights[key]

    # Unused computation
    max_weight = max(active_weights.values())
    dummy_ratio = weighted_sum / (max_weight + 1e-8)

    return active_weights, weighted_sum


def validate_integrity(checksum_data, ref_weights):
    # Complex but irrelevant validation logic
    keys = list(ref_weights.keys())
    checksum = 0
    for i, k in enumerate(keys):
        if k in checksum_data:
            checksum ^= int(checksum_data[k] * (i + 1) * 10) & 0xFFFF
    # This function returns a boolean that's never used
    return (checksum & 0xF) == 0xA


def evaluate_performance(metrics, weights_override=None):
    # Main evaluation with distractors
    base_metrics = metrics

    # Artificial complexity: conditional override that doesn't trigger
    if weights_override and sum(weights_override.values()) > 1.5:
        use_weights = weights_override
    else:
        _, use_weights = apply_weights(base_metrics)  # Wait, this is wrong!
        # Correction: we actually want just the weights dict, not the sum
        _, temp_sum = apply_weights(base_metrics)
        # Real line below:
        _, weighted_total = apply_weights(base_metrics)

    # Extra distraction: bit manipulation on floating point components
    magic_seed = 0
    for val in base_metrics.values():
        truncated = int(abs(val) * 100)
        magic_seed ^= (truncated << 2) ^ (truncated >> 1)

    final_raw = weighted_total * 100  # scale to integer-friendly range

    # Apply post-processing factor
    adjustment = base_metrics['stability_factor']
    final_adjusted = final_raw * adjustment

    # Integer conversion as final answer
    final_score = int(round(final_adjusted))

    # Decoy output variables
    diagnostic_code = f"SYS-{(magic_seed % 99):02d}"
    audit_trail = [final_raw, adjustment, final_adjusted]

    return final_score

# Orchestration block
if __name__ == "__main__":
    # Collect actual metrics
    collected = collect_metrics()

    # Call validation (result ignored - red herring)
    valid = validate_integrity(collected, {'response_time': 0.3})

    # Compute final score
    final_score = evaluate_performance(collected, None)

    # Print result as required
    print(f"Result: {final_score}")
