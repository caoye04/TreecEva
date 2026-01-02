def analyze_metrics(data):
    # Irrelevant preprocessing step (distractor)
    normalized = [x * 1.05 for x in data if x > 0]
    offset = sum(normalized) / len(normalized) if normalized else 0

    # Semi-relevant transformation
    adjusted = [(x + offset) * 0.95 for x in data]

    # Key computation path
    valid_entries = [x for x in adjusted if x > 10]
    if len(valid_entries) == 0:
        return 0

    peak = max(valid_entries)
    base = min(data)  # Use original data minimum
    volatility = (peak - base) / base if base != 0 else 0

    # Red herring: unused complex calculation
    entropy = 0
    for x in data:
        if x > 0:
            entropy -= (x / sum(data)) * ((x / sum(data))) ** 0.5

    return volatility * 100


def calculate_performance(raw_input):
    # Simulate multi-stage processing with distractions
    filtered = [x for x in raw_input if x % 2 == 1]  # Only odd numbers
    shifted = [x << 1 for x in filtered]  # Bitwise distraction

    # Core logic embedded within noise
    summary_stats = {
        'avg': sum(filtered) / len(filtered) if filtered else 0,
        'count': len([x for x in raw_input if x > 50]),  # semi-relevant
        'level': 'high' if sum(filtered) > 150 else 'low'
    }

    # Unused helper structure (dead code path)
    debug_info = {}
    for idx, val in enumerate(shifted):
        debug_info[f'entry_{idx}'] = {
            'raw': val >> 1,
            'squared': (val >> 1) ** 2,
            'flagged': (val >> 1) % 7 == 0
        }

    # Actual critical calculation
    processed = [x for x in raw_input if 10 <= x <= 90]
    if not processed:
        return 0

    threshold = sum(processed) / len(processed)
    above_threshold = len([x for x in processed if x > threshold])
    below_threshold = len([x for x in processed if x <= threshold])
    balance_ratio = above_threshold / below_threshold if below_threshold != 0 else 0

    # Final score derived from balance and volatility
    volatility_metric = analyze_metrics(raw_input)
    final_component = balance_ratio * (volatility_metric / 100)

    # Introduce misleading variable with similar name
    final_score_temp = final_component * 2  # Not used
    final_score = int((final_component + summary_stats['avg'] / 50) * 100)

    return final_score

# Main execution
benchmark_data = [12, 45, 67, 83, 29, 50, 74, 18, 62, 35]
intermediate_result = [x for x in benchmark_data if x < 70]
dummy_shift = [x ^ 25 for x in intermediate_result]  # XOR distraction

final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")