def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    adjustment = 0.0

    # Preprocess phase: extract and clean string-based metrics
    cleaned_metrics = []
    for entry in data:
        metric_str = entry['metric'].strip().lower()
        if metric_str.startswith('perf'):
            raw_value = float(entry['value'])
            normalized = raw_value / 100.0
            cleaned_metrics.append(normalized)

    # Secondary irrelevant pass: simulate audit logging (distractor)
    log_entries = []
    for val in cleaned_metrics:
        status_flag = "A" if val > 0.7 else "B"
        log_entry = f"LOG-{status_flag}: {val:.3f}"
        log_entries.append(log_entry)  # Unused in final calculation

    # Core logic: compute weighted score with conditional adjustments
    total = 0.0
    bonus_applied = False
    count = 0
    
    for val in cleaned_metrics:
        adjusted_val = val * base_multiplier
        if adjusted_val > 0.8 and not bonus_applied:
            adjustment += 5.0
            bonus_applied = True
        elif adjusted_val < 0.4:
            adjustment -= 2.0
        total += adjusted_val
        count += 1

    average = total / count if count > 0 else 0.0

    # Simulate tuple unpacking for configuration (relevant structure)
    weights = (0.6, 0.4)
    scaling, offset = weights
    
    preliminary_score = (average * scaling + adjustment * offset) * 100

    # Apply penalty for inconsistent performance (based on variance distractor)
    squared_diffs = [(x - average)**2 for x in cleaned_metrics]
    variance = sum(squared_diffs) / len(squared_diffs) if squared_diffs else 0
    stability_penalty = 0
    if variance > 0.02:
        stability_penalty = int(variance * 100)  # Minor penalty

    # Final score computation — stability_penalty is small but included
    final_score = int(preliminary_score - stability_penalty)

    # Irrelevant post-processing: format summary (dead code path)
    summary_stats = {
        'entries': len(cleaned_metrics),
        'mean': average,
        'penalty': stability_penalty,
        'final_int': final_score
    }
    summary_string = f"Report:{summary_stats['entries']}-{summary_stats['final_int']}"
    summary_string.upper()  # No side effect

    return final_score

# Input data setup
benchmark_data = [
    {'metric': ' Perf_A ', 'value': '92'},
    {'metric': ' Perf_B ', 'value': '76'},
    {'metric': ' Perf_C ', 'value': '89'},
    {'metric': ' Perf_D ', 'value': '61'},
    {'metric': ' Latency_X ', 'value': 'invalid'},  # ignored due to filter
    {'metric': ' Perf_E ', 'value': '45'}
]

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")