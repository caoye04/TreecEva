def analyze_metrics(data):
    # Irrelevant transformation
    temp_normalized = [x * 1.05 for x in data if x > 0]
    offset_adjusted = [x - 0.7 for x in temp_normalized]
    
    # Actual relevant logic buried among distractions
    raw_total = sum(data)
    valid_count = len([x for x in data if x >= 5])
    avg_base = raw_total / len(data) if data else 0

    # Distractor: unused statistical calculation
    variance_proxy = sum([(x - avg_base) ** 2 for x in data]) / len(data) if data else 0

    return raw_total, avg_base, valid_count


def filter_outliers(sequence):
    threshold = sum(sequence) / len(sequence) * 1.1
    filtered = [x for x in sequence if x <= threshold]
    return filtered  # Not used directly in final result


def calculate_performance(log_entries):
    # Preprocessing with string manipulation
    processed_names = [''.join(reversed(name.lower())) for name in ['System', 'Core', 'Engine']]
    name_flag = len(processed_names[0]) > 4  # Always True, but adds cognitive load

    base_total, mean_val, qualified = analyze_metrics(log_entries)

    # Secondary distraction: case conversion and filtering
    tags = ['ERROR', 'WARNING', 'INFO']
    lower_tags = [tag.lower() for tag in tags]
    tag_initials = [t[0] for t in lower_tags]

    # Core logic hidden in conditional
    adjustment_factor = 0.9 if mean_val < 15 else 1.1
    adjusted_total = base_total * adjustment_factor

    # Additional red herring computation
    squared_sums = sum([x**2 for x in log_entries[:3]]) if len(log_entries) >= 3 else 0
    dummy_ratio = squared_sums / (adjusted_total + 1e-8)

    # Key decision point
    if qualified > 4:
        bonus = 12
    elif mean_val > 12:
        bonus = 8
    else:
        bonus = 3

    # Final score calculation
    final_score = int(adjusted_total + bonus)

    # Dead code branch (never reached due to prior conditions)
    if len(tag_initials) > 5:
        final_score -= 5

    return final_score

# Input data
benchmark_data = [10, 7, 13, 15, 9, 14, 6]

# Filter step that doesn't affect final input (distractor)
filtered_data = filter_outliers(benchmark_data)

# Critical execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")