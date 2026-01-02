def preprocess_records(raw_entries):
    cleaned = []
    temp_sum = 0
    outlier_count = 0

    for entry in raw_entries:
        name = entry['name'].strip().upper()
        value = entry['value']
        category = entry['category'].replace(' ', '_')

        if len(name) == 0:
            continue

        if value < 0:
            outlier_count += 1
            continue

        normalized_value = round(value ** 0.5, 2)
        temp_sum += normalized_value

        cleaned.append({
            'id': name,
            'score': normalized_value,
            'type': category
        })

    summary_stats = {
        'total_processed': len(cleaned),
        'aggregate_temp': temp_sum,
        'ignored_outliers': outlier_count
    }

    return cleaned, summary_stats


def group_by_type(items):
    mapping = {}
    for item in items:
        t = item['type']
        if t not in mapping:
            mapping[t] = []
        mapping[t].append(item['score'])
    
    # Irrelevant sorting - doesn't impact final result
    for k in mapping:
        mapping[k].sort(reverse=True)
    
    return mapping


def calculate_diversity_index(groups):
    diversity = 0
    total_keys = len(groups)
    
    for key, values in groups.items():
        if len(values) > 1:
            diff = max(values) - min(values)
            diversity += diff * 0.1
    
    # Dead computation - never used
    if total_keys == 0:
        dummy = [x for x in range(100)]
        return 0.0
    
    return round(diversity / (total_keys + 1e-8), 4)


def calculate_final_score(data_package):
    entries, stats = data_package
    grouped = group_by_type(entries)
    
    base_total = sum(sum(scores) for scores in grouped.values())
    diversity_bonus = calculate_diversity_index(grouped)
    size_penalty = len(entries) * 0.05
    
    # Distractor variables
    temp_debug_log = f'Records: {len(entries)}, Outliers: {stats["ignored_outliers"]}'
    debug_flag = True if 'ERR' in temp_debug_log else False
    
    intermediate_result = base_total + diversity_bonus - size_penalty
    
    # Extra transformation with string-based key lookup (irrelevant to logic)
    config_weights = {'A': 1.1, 'B': 0.9, 'C': 1.0}
    adjustment_key = 'A' if base_total > 50 else 'B'
    adjusted_score = intermediate_result * config_weights.get(adjustment_key, 1.0)
    
    # Final score calculation
    final_score = int(round(adjusted_score))
    
    # This print is required to expose the result
    print(f"Result: {final_score}")
    return final_score

# Main execution
raw_data = [
    {'name': 'alice', 'value': 25, 'category': 'research'},
    {'name': 'bob', 'value': 36, 'category': 'development'},
    {'name': 'charlie', 'value': 49, 'category': 'research'},
    {'name': 'diana', 'value': 64, 'category': 'development'},
    {'name': 'eve', 'value': 16, 'category': 'research'},
    {'name': 'frank', 'value': 81, 'category': 'strategy'},
    {'name': 'grace', 'value': 9, 'category': 'strategy'},
    {'name': 'heidi', 'value': -5, 'category': 'research'},  # outlier
    {'name': 'ivan', 'value': 100, 'category': 'development'}
]

processed_data = preprocess_records(raw_data)
final_score = calculate_final_score(processed_data)