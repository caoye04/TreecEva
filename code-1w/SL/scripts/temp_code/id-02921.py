def analyze_system_performance(raw_data, threshold=0.85):
    # Irrelevant preprocessing block (distractor)
    normalized = [x / max(raw_data) for x in raw_data if x > 0]
    outliers = list(filter(lambda x: x > threshold, normalized))
    baseline = sum(normalized) / len(normalized) if normalized else 0

    # Dead code path - never executed due to condition (red herring)
    if len(outliers) > 100:
        correction_factor = 1.5
        adjusted = [x * correction_factor for x in normalized]
    else:
        pass  # Simulate complex logic that does nothing

    # Real computation begins: parse log severity levels
    log_entries = [
        {'timestamp': i, 'level': 'ERROR' if x < 0.1 else 'INFO', 'payload': x}
        for i, x in enumerate(normalized)
    ]

    # Complex data transformation with distractors
    stats = {
        'error_count': len([e for e in log_entries if e['level'] == 'ERROR']),
        'info_count': len([e for e in log_entries if e['level'] == 'INFO']),
        'weighted_sum': sum(e['payload'] * (2 if e['level'] == 'ERROR' else 1) for e in log_entries)
    }

    # Misleading metric calculation (not used later)
    phantom_score = (stats['error_count'] * 1000) / (len(log_entries) or 1)
    temp_adjustment = round(phantom_score ** 0.5, 4) if phantom_score > 5 else 0

    # System state simulation with decoy values
    system_state = {
        'status': 'STANDBY',
        'load': 0.67,
        'version': 'v2.3.1',
        'flags': ['INIT', 'ACTIVE', 'VERBOSE'],
        'cache_hit_rate': temp_adjustment  # Distractor assignment
    }

    # Conditional expression influencing actual logic
    mode_flag = 'strict' if system_state['load'] > 0.6 else 'relaxed'

    # Key function with nested logic and distractors
    def process_metrics(entries, state):
        # Unused intermediate transformations
        timestamps = [entry['timestamp'] for entry in entries]
        levels = [entry['level'] for entry in entries]
        payloads = [entry['payload'] for entry in entries]

        # Enumerate used with zip (required Python feature)
        indexed_ratios = []
        for i, (ts, pl) in enumerate(zip(timestamps, payloads)):
            ratio = (pl + i) / (ts + 1) if ts != -1 else 0
            indexed_ratios.append((i, ratio))

        # Redundant sorting (does not affect final result)
        sorted_ratios = sorted(indexed_ratios, key=lambda x: x[1], reverse=True)

        # Decoy aggregation
        decoy_total = sum(r for _, r in sorted_ratios[:3]) if sorted_ratios else 0
        ignore_threshold = decoy_total * 0.1

        # Actual core logic: count error payloads above dynamic threshold
        dynamic_limit = 0.15 if mode_flag == 'strict' else 0.2
        relevant_errors = [
            p for p in payloads
            if p < dynamic_limit and log_entries[payloads.index(p)]['level'] == 'ERROR'
        ]

        # Final computation using only a subset of data
        base_value = sum(relevant_errors)
        multiplier = len(relevant_errors) + (1 if 'VERBOSE' in state['flags'] else 0)
        checksum = int(base_value * 1000) % 97

        # Critical answer computation
        result = int((base_value * multiplier) * 100) + checksum
        return result

    # Execution point of interest
    final_diagnostic = process_metrics(log_entries, system_state)
    print(f"Result: {final_diagnostic}")