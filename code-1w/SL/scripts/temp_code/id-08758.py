def analyze_trends(data_map):
    trend_sum = 0
    noise_counter = 0
    temp_factor = 1.5

    for key in data_map:
        if key.startswith('temp_'):
            noise_counter += len(data_map[key])
            continue
        
        base_value = sum(data_map[key])
        adjustment = len(data_map[key]) * 0.1
        trend_sum += int(base_value + adjustment)

    scaling_factor = 2.0 if noise_counter > 10 else 1.0
    return int(trend_sum * scaling_factor)


def calculate_rating(metrics):
    total_weight = 0
    category_bonus = {'social': 3, 'search': 2, 'media': 4}
    debug_log = []
    intermediate_vals = []

    for cat, values in metrics.items():
        raw_total = sum(x ** 0.5 for x in values if x > 0)
        weight = raw_total * 0.75

        if cat in category_bonus:
            weight += category_bonus[cat]

        # Irrelevant transformation
        inverted = [1/x for x in values if x != 0]
        avg_inv = sum(inverted) / len(inverted) if inverted else 0
        debug_log.append(avg_inv)

        intermediate_vals.append(weight)

        if weight > 25:
            break  # Early exit based on partial processing

    total_weight = sum(intermediate_vals)
    
    # Additional irrelevant accumulation
    phantom_sum = 0
    for i in range(len(debug_log)):
        phantom_sum += debug_log[i] * (i + 1)

    final_rating = int(total_weight + 1.5)
    return final_rating

# Main execution
engagement_data = {
    'social': [16, 25, 9],
    'search': [36, 49],
    'media': [64],
    'temp_buffer': [1, 2, 3, 4, 5],
    'cache_warmup': [10, 10]
}

result_analysis = analyze_trends(engagement_data)
counted_items = len(engagement_data)
baseline_adjust = counted_items * 2

final_score = calculate_rating(engagement_data)
print(f"Result: {final_score}")