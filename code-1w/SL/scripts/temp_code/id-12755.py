from collections import defaultdict, Counter

# Simulated sensor data aggregation for a health monitoring system
def collect_telemetry():
    raw_signals = [127, 83, 194, 65, 201, 72, 188, 91]
    signal_map = defaultdict(int)
    for idx, val in enumerate(raw_signals):
        signal_map[f'sensor_{idx % 4}'] += val

    # Irrelevant transformation (distractor)
    normalized = [x / max(raw_signals) for x in raw_signals]
    stats_cache = {'mean': sum(raw_signals) / len(raw_signals), 'peak': max(raw_signals)}

    return dict(signal_map)

# Signal filtering based on adaptive thresholds (partially relevant)
def apply_filter(data, mode='aggressive'):
    filtered = {}
    baseline = sum(data.values()) / len(data)
    for k, v in data.items():
        if mode == 'aggressive' and v > baseline * 1.1:
            filtered[k] = int(v * 0.85)
        elif mode == 'conservative':
            filtered[k] = v
    # Dead code path (distractor)
    if mode == 'experimental':
        return {k: v ^ 3 for k, v in data.items()}
    return filtered if filtered else data

# Auxiliary function with misleading intermediate result
def compute_rolling_average(data_list, window=3):
    averages = []
    for i in range(len(data_list) - window + 1):
        avg = sum(data_list[i:i+window]) / window
        averages.append(round(avg))
    return averages  # Not used in main logic

# Core diagnostic processor
def evaluate_risk_level(signal_sum, criticality_index):
    if signal_sum < 300:
        return 'LOW'
    elif criticality_index > 7:
        return 'CRITICAL'
    else:
        return 'ELEVATED'

# Main metric processor with red herrings
def process_metrics(data, config):
    # Step 1: Extract and transform relevant signals
    values = list(data.values())
    total_power = sum(x ** 2 for x in values) // 100  # Energy-like metric

    # Step 2: Compute auxiliary indices (some irrelevant)
    entropy_proxy = 0
    for v in values:
        if v > 0:
            entropy_proxy += v * (v.bit_length())  # Artificial complexity

    # Step 3: Determine activation pattern
    pattern_count = Counter(values)
    dominant_freq = pattern_count.most_common(1)[0][1]

    # Step 4: Apply configuration-based adjustment
    adjustment_factor = config.get('sensitivity', 1.0) * config.get('gain', 1.0)
    adjusted_entropy = entropy_proxy * adjustment_factor

    # Step 5: Evaluate risk through multiple indirections
    risk_flag = evaluate_risk_level(total_power, int(adjusted_entropy % 10))

    # Step 6: Generate diagnostic score (key computation)
    base_score = (total_power // 5) + (dominant_freq * 17)
    
    # Distractor: unused complex calculation
    temporal_weight = sum(i * v for i, v in enumerate(values)) / (sum(values) or 1)
    decay_correction = [v / (i + 1) for i, v in enumerate(reversed(values))]

    # Step 7: Conditional override logic (misleading)
    if config.get('override_safety', False):
        base_score = max(base_score, 999)

    # Step 8: Final nonlinear transformation
    final_diagnostic = (base_score ^ 42) + (int(adjusted_entropy) % 25)

    # Irrelevant logging (distractor)
    log_entry = f"Diag={final_diagnostic}, TempW={temporal_weight:.2f}"
    debug_stack = [{'level': 'TRACE', 'value': d} for d in decay_correction]

    return final_diagnostic

# --- Execution Flow ---
if __name__ == '__main__':
    # Initialize system telemetry
    telemetry_data = collect_telemetry()
    
    # Build configuration map (only some keys are used)
    threshold_map = {
        'sensitivity': 1.3,
        'gain': 0.85,
        'override_safety': False,
        'buffer_size': 256,
        'timeout_ms': 1500,
        'calibration': [0.98, 1.02, 1.01]
    }
    
    # Apply preprocessing filter
    processed_input = apply_filter(telemetry_data, mode='aggressive')
    
    # Simulate secondary channel (unused)
    aux_signals = [x * 0.75 for x in [120, 88, 190, 60]]
    rolling_stats = compute_rolling_average(aux_signals + [100, 110])
    
    # Critical execution point
    final_diagnostic = process_metrics(processed_input, threshold_map)
    
    # Output target result
    print(f"Result: {final_diagnostic}")