def analyze_metrics(data, threshold=0.75):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(data) for x in data]
    outliers = [i for i, x in enumerate(normalized) if x > 0.9]
    filtered = [x for x in normalized if x <= threshold]

    # Decoy function that's never called
    def calculate_robustness(arr):
        return sum(x ** 2 for x in arr) / len(arr) if arr else 0

    # Misleading intermediate calculation
    temp_weight = sum(filtered) * 0.33
    adjustment_factor = len(outliers) > 0 else 0.95

    # Actual relevant logic embedded within distractions
    base_metric = sum(data) // len(data)  # Integer division
    bonus = len([x for x in data if x % 7 == 0]) * 3
    penalty = sum(1 for x in data if x < 10) * 2

    # Conditional expression (required Python feature)
    performance_multiplier = 1.5 if base_metric >= 50 and bonus > penalty else 0.8

    # Nested logic with multiple levels
    if base_metric > 40:
        if bonus > 0:
            extra_award = 25 if any(x > 100 for x in data) else 10
        else:
            extra_award = 5
        
        # More red herring variables
        shadow_value = extra_award * 0.1
        dummy_cache = {i: shadow_value for i in range(3)}

        final_raw = (base_metric + bonus - penalty) * performance_multiplier
        if final_raw > 100:
            # Simulated clamping
            final_raw = 100 + (final_raw - 100) ** 0.5  # Diminishing returns
    else:
        final_raw = base_metric * performance_multiplier

    return int(final_raw)


# Unused auxiliary functions (dead code path)
def validate_input_structure(obj):
    if isinstance(obj, dict):
        return all(isinstance(k, str) for k in obj.keys())
def legacy_compatibility_layer():
    return False

# Main execution context
raw_inputs = [84, 62, 91, 77, 49, 105, 56, 88]

# Distractor list operations
transformed = []
for val in raw_inputs:
    if val % 2 == 0:
        transformed.append(val // 2)
    else:
        transformed.append(val * 2)

# Another irrelevant dictionary construction
stats_summary = {
    'count_even': len([x for x in raw_inputs if x % 2 == 0]),
    'sum_odd_shifted': sum((x << 1) for x in raw_inputs if x % 2 == 1),
    'max_power_of_two': max(x for x in raw_inputs if (x & (x - 1)) == 0, default=1)
}

# Key statement — target of the question
final_score = analyze_metrics(raw_inputs)

# Print result as required
print(f"Result: {final_score}")