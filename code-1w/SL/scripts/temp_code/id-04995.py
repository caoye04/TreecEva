def analyze_performance(records):
    totals = {}
    for record in records:
        user_id = record['id']
        raw_points = sum(record['scores'])
        bonus = len(record['scores']) > 5
        penalty = 1 if record['attempts'] > 3 else 0
        totals[user_id] = raw_points + (2 if bonus else 0) - penalty
    return totals


def normalize_values(data_map):
    total_sum = sum(data_map.values())
    normalized = {}
    for k, v in data_map.items():
        normalized[k] = round(v / total_sum * 100, 2)
    return normalized


def filter_eligible_entries(entries, min_threshold):
    filtered = {}
    temp_debug_log = []
    for key, value in entries.items():
        status_flag = 'ELIGIBLE' if value >= min_threshold else 'PENDING'
        temp_debug_log.append(f'{key}:{status_flag}')
        if value >= min_threshold:
            filtered[key] = int(value)
    # Simulated logging (irrelevant to final result)
    log_size = len(temp_debug_log)
    avg_length = sum(len(entry) for entry in temp_debug_log) / log_size if log_size else 0
    return filtered


def process_results(data, limit):
    processed = analyze_performance(data)
    scaled = normalize_values(processed)
    kept = filter_eligible_entries(scaled, limit)
    base_accum = 0
    multiplier = 3
    for val in kept.values():
        base_accum += val * multiplier
    adjustment = len(kept) % 4 == 0
    final_accum = base_accum + (1.5 if adjustment else 0.7)
    
    # Distractor variables
    dummy_calc = sum(kept.values()) * 0.1
    shadow_copy = kept.copy()
    temp_factor = len(data) - len(kept)
    
    return round(final_accum, 2)

# Main execution
assessment_data = [
    {'id': 'A1', 'scores': [8, 7, 9, 6, 8, 7], 'attempts': 2},
    {'id': 'B2', 'scores': [5, 6, 5, 7], 'attempts': 4},
    {'id': 'C3', 'scores': [9, 9, 8, 9, 8, 9, 9], 'attempts': 1},
    {'id': 'D4', 'scores': [4, 5, 6], 'attempts': 3},
    {'id': 'E5', 'scores': [7, 7, 8, 8, 7, 8, 7, 8], 'attempts': 2}
]

threshold = 18.5

final_score = process_results(assessment_data, threshold)
print(f"Result: {final_score}")