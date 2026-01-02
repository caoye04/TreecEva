def analyze_metrics(data):
    # Irrelevant preprocessing step (distractor)
    normalized = [x * 1.05 for x in data if x > 0]
    outliers = [x for x in normalized if x > 90]
    filtered = [x for x in data if x >= 10]

    # Semi-relevant transformation
    adjusted = []
    for val in filtered:
        if val % 2 == 0:
            adjusted.append(val * 0.9)
        else:
            adjusted.append(val * 1.1)

    # Unused aggregation (dead code path - distractor)
    avg_outlier = sum(outliers) / len(outliers) if outliers else 0

    return adjusted


def compute_weights(n):
    # Generates weights but only one value is actually used later
    weights = [(i ** 0.5) for i in range(1, n+1)]
    weight_sum = sum(weights)
    normalized_weights = [w / weight_sum for w in weights]
    
    # Return only the last weight for actual use (others are distractions)
    return normalized_weights[-1] if normalized_weights else 0


def calculate_performance(raw_input):
    # Main logic begins here
    processed = analyze_metrics(raw_input)
    
    # Key computation steps
    base_total = 0
    multiplier = compute_weights(len(processed))
    
    temp_results = []
    for idx, value in enumerate(processed):
        # Some values are skipped based on condition
        if value < 20:
            continue
        
        # Intermediate calculation stored but not all used
        squared = value ** 2
        mod_val = squared % 7
        adjusted_val = squared * multiplier
        
        if mod_val == 0:
            adjusted_val += 5
        
        temp_results.append(adjusted_val)
        
        # Early break to skip unnecessary iterations (optimization red herring)
        if len(temp_results) == 5:
            break
    
    # Only sum of first few matters
    partial_sum = sum(temp_results[:4])
    
    # Final adjustment using modular arithmetic
    scaling_factor = len(processed) % 6 or 1
    final_score = int(partial_sum / scaling_factor)
    
    return final_score

# Simulated benchmark dataset
benchmark_data = [5, 12, 18, 25, 30, 8, 42, 16, 35, 70, -5, 22]

# Execute main logic
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")