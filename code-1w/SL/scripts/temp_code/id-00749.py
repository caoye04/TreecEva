def analyze_metrics(data):
    base_values = [x * 1.5 for x in data if x > 10]
    offset = sum(base_values) / len(base_values) if base_values else 0
    adjustments = [abs(x - offset) for x in base_values]
    return offset, sum(adjustments)


def validate_input(raw):
    if not raw:
        return False
    total = sum(raw)
    return total > 0 and len(raw) < 20


def calculate_performance(entries):
    # Irrelevant pre-processing (distractor)
    temp_cache = {}
    for i, val in enumerate(entries):
        temp_cache[f'idx_{i}'] = val * val + 2  # Not used later

    # Core logic begins
    filtered = [x for x in entries if x % 2 == 1]  # Keep odd values
    
    # Secondary filtering based on position
    indexed = [(i, v) for i, v in enumerate(filtered) if i < 3 or v > 5]
    extracted = [v for i, v in indexed]

    # Compute moving average of window size 2 (semi-relevant)
    averages = []
    for j in range(len(extracted) - 1):
        averages.append((extracted[j] + extracted[j+1]) / 2)
    
    # Dummy branching with dead code
    correction_factor = 1.0
    if len(averages) > 10:
        correction_factor = 0.9  # Never reached
    elif len(averages) > 5:
        correction_factor = 1.1  # Also not triggered

    # Key computation
    baseline = sum(extracted) * 0.8
    penalty = len([p for p in extracted if p < 3]) * 2.5
    bonus = len(averages) * 0.7 if any(x > 6 for x in extracted) else 0

    # Final score calculation
    final_score = baseline - penalty + bonus

    # Extra red herring variables
    debug_info = {
        'raw_count': len(entries),
        'filtered_peaks': max(extracted) if extracted else 0,
        'phantom_metric': sum(temp_cache.values()) / 100 if temp_cache else 0
    }

    return final_score

# Main execution
benchmark_data = [12, 7, 3, 9, 2, 11, 4, 5, 8, 13]

# Validate input (always passes, but adds noise)
if validate_input(benchmark_data):
    offset_val, error_sum = analyze_metrics(benchmark_data)
    final_score = calculate_performance(benchmark_data)

print(f"Result: {final_score}")