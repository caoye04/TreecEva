def evaluate_performance(metrics):
    base_threshold = 75
    penalty_factor = 0.8
    bonus_multiplier = 1.2
    temp_result = 0
    final_score = 0

    # Irrelevant computation - distractor
    placeholder_data = [x ** 0.5 for x in range(1, 6)]
    unused_sum = sum(placeholder_data)

    # Actual logic begins
    metric_set = set(metrics)
    required_metrics = {'latency', 'throughput', 'accuracy', 'energy_efficiency'}
    optional_metrics = {'memory_usage', 'startup_time'}

    # Check completeness
    missing_required = required_metrics - metric_set
    has_all_required = len(missing_required) == 0

    # Performance scoring
    base_score = 50
    if has_all_required:
        base_score += 30
        if 'energy_efficiency' in metric_set and 'accuracy' in metric_set:
            consistency_check = True
            for m in ['latency', 'throughput']:
                if m not in metric_set:
                    consistency_check = False
            if consistency_check:
                base_score += 10

    # Bonus for optional metrics
    optional_found = optional_metrics & metric_set
    bonus_per_metric = 5
    extra_credit = len(optional_found) * bonus_per_metric

    # Apply modular adjustment based on metric count
    total_count = len(metric_set)
    mod_adjustment = (total_count % 4) * 2

    # Final computation
    raw_final = base_score + extra_credit + mod_adjustment

    # Red herring: complex but unused bitwise transformation
    masked_value = raw_final ^ 255
    inverted = ~masked_value & 0xFF
    decoy_calc = (inverted + 100) % 77

    # Final score assignment
    final_score = raw_final  # This is the actual result

    # Debug print that doesn't affect outcome
    debug_flag = False
    if debug_flag:
        print(f"Missing: {missing_required}")

    return final_score

# Main execution
metrics_input = ['latency', 'throughput', 'accuracy', 'energy_efficiency', 'memory_usage']
intermediate = [x.upper() for x in metrics_input]
processed = list(map(str.lower, intermediate))
metric_data = set(processed)

# Key statement
final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")