def analyze_performance(records):
    stats = {}
    total_entries = len(records)
    valid_count = 0
    temp_sum = 0
    outlier_count = 0

    for record in records:
        value = record['value']
        category = record['category']
        
        if category not in stats:
            stats[category] = {'count': 0, 'sum': 0, 'squares': 0}
        
        stats[category]['count'] += 1
        stats[category]['sum'] += value
        stats[category]['squares'] += value ** 2
        
        temp_sum += value
        
        if value < 5 or value > 95:
            outlier_count += 1

    avg_value = temp_sum / total_entries if total_entries else 0
    
    # Irrelevant normalization attempt (not used later)
    normalized_stats = {}
    for cat, data in stats.items():
        mean = data['sum'] / data['count']
        variance = (data['squares'] / data['count']) - (mean ** 2)
        normalized_stats[cat] = {
            'mean': round(mean, 2),
            'std_dev': round(variance ** 0.5, 2) if variance > 0 else 0
        }
    
    return stats, avg_value, outlier_count


def calculate_weighted_trend(data_map):
    # Dummy function to add distraction
    trend_score = 0
    for key in sorted(data_map.keys()):
        trend_score += len(data_map[key]) * 0.1
    return round(trend_score, 2)


def process_results(raw_results, limits):
    processed = {}
    base_threshold = limits['base']
    penalty_factor = limits['penalty']
    bonus_shift = limits['bonus']

    internal_total = 0
    adjustment_counter = 0

    for k, v in raw_results.items():
        count = v['count']
        raw_sum = v['sum']

        if raw_sum > base_threshold:
            adjustment_counter += 1
            
        entry_avg = raw_sum / count if count else 0
        
        # Core logic influencing final result
        if entry_avg >= 40:
            internal_total += int(entry_avg // 2)
        else:
            internal_total -= int(entry_avg % 7)

        # Dead computation branch (never accessed due to logic above)
        if entry_avg < 0:
            internal_total += 100  # unreachable

    # Additional irrelevant transformation
    temp_array = [i**2 for i in range(adjustment_counter)]
    checksum = sum(temp_array) % 17 if temp_array else 0

    final_value = internal_total - penalty_factor + bonus_shift + checksum
    return int(final_value)

# Main execution
if __name__ == '__main__':
    input_data = [
        {'category': 'A', 'value': 45},
        {'category': 'B', 'value': 82},
        {'category': 'A', 'value': 67},
        {'category': 'C', 'value': 12},
        {'category': 'B', 'value': 58},
        {'category': 'C', 'value': 33},
        {'category': 'A', 'value': 71},
        {'category': 'D', 'value': 5},
        {'category': 'D', 'value': 96},  # outlier
        {'category': 'C', 'value': 41}
    ]

    # Extract analysis
    result_stats, average, outliers = analyze_performance(input_data)

    # Unused sorting (distractor)
    sorted_categories = sorted(result_stats.keys(), key=lambda x: result_stats[x]['sum'], reverse=True)

    # Another unused helper call (misleading path)
    dummy_trend = calculate_weighted_trend(result_stats)

    # Threshold configuration (affects final score)
    config = {
        'base': 100,
        'penalty': 3,
        'bonus': 5
    }

    # Key statement
    final_score = process_results(result_stats, config)

    print(f"Result: {final_score}")