def evaluate_performance(data, baseline):
    adjustments = []
    temp_buffer = []
    cumulative_shift = 0

    for i in range(len(data)):
        raw_value = data[i]
        normalized = raw_value / baseline
        
        # Irrelevant transformation (distractor)
        squared_deviation = (normalized - 1) ** 2
        temp_buffer.append(squared_deviation)

        if normalized > 1.1:
            adjustment = normalized * 0.95
        elif normalized < 0.9:
            adjustment = normalized * 1.05
        else:
            adjustment = normalized
        
        adjustments.append(adjustment)

    # Misleading secondary loop (dead logic path - not used in final result)
    filtered_adjustments = [x for x in adjustments if x > 0.95]
    aggregate = 0
    for val in filtered_adjustments:
        aggregate += val * 0.1  # Distractor computation

    # Core logic: average of adjusted values
    avg_adjusted = sum(adjustments) / len(adjustments)

    # Additional distraction: tuple unpacking with irrelevant components
    stats_summary = (avg_adjusted, len(adjustments), sum(temp_buffer))
    avg_result, count_used, _ = stats_summary

    # Slice-based selection (core concept): use middle third of sorted adjustments
    sorted_adjs = sorted(adjustments)
    mid_section = sorted_adjs[len(sorted_adjs)//3 : 2*len(sorted_adjs)//3]
    mid_avg = sum(mid_section) / len(mid_section)

    # Final score derived from mid_avg and baseline interaction
    final_score = int((mid_avg * baseline) + 0.5)  # Rounded to nearest integer

    return final_score

# Main execution block
metrics = [88, 92, 76, 95, 83, 99, 70, 85, 91]
benchmark = 85
interim_results = [x * 1.1 for x in metrics]  # Unused buffer (distractor)
scaling_factor = 1.0  # Unused variable
normalization_cache = {}  # Dead code placeholder

final_score = evaluate_performance(metrics, benchmark)
print(f"Result: {final_score}")