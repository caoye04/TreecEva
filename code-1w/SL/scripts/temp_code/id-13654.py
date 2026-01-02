def process_timestamps(log_entries):
    processed = []
    for entry in log_entries:
        time_str = entry['time']
        hours, minutes = time_str.split(':')
        total_minutes = int(hours) * 60 + int(minutes)
        normalized = total_minutes / 1440.0
        processed.append(normalized)
    return processed


def filter_anomalies(data_list):
    # Irrelevant filtering function (dead-end)
    anomalies = [x for x in data_list if x < 0.1 or x > 0.9]
    clean_data = [x for x in data_list if x >= 0.1 and x <= 0.9]
    return clean_data


def calculate_final_score(log, weight_map):
    scores = {}
    temp_offsets = []
    
    for key, entries in log.items():
        base_value = len(entries)
        multiplier = weight_map.get(key, 1.0)
        raw_score = base_value * multiplier
        
        # Track intermediate stats (some irrelevant)
        avg_time = 0
        time_sum = 0
        count = 0
        for e in entries:
            t = e['time']
            h, m = t.split(':')
            time_in_minutes = int(h) * 60 + int(m)
            time_sum += time_in_minutes
            count += 1
            
        if count > 0:
            avg_time = time_sum / count
        
        temp_offsets.append(avg_time % 60)
        
        # Actual scoring logic
        adjustment = 1.0
        if base_value >= 5:
            adjustment = 1.2
        elif base_value == 0:
            adjustment = 0.5
            
        scores[key] = raw_score * adjustment
    
    # Use dictionary and set operations
    score_values = list(scores.values())
    unique_scores = set(score_values)
    
    # Red herring: complex but unused calculation
    outlier_count = 0
    if len(unique_scores) > 0:
        mean_score = sum(unique_scores) / len(unique_scores)
        variance = sum((x - mean_score) ** 2 for x in unique_scores) / len(unique_scores)
        std_dev = variance ** 0.5
        for s in unique_scores:
            if abs(s - mean_score) > 2 * std_dev:
                outlier_count += 1
    
    # Real final computation
    total_weighted = sum(scores.values())
    penalty_factor = len(temp_offsets) * 0.01
    final_result = total_weighted - penalty_factor
    
    # Additional distraction: case conversion on labels
    adjusted_keys = {k.upper().replace('_', '') for k in scores.keys()}
    extra_boost = 0
    for k in adjusted_keys:
        if 'ERROR' in k:
            extra_boost += 5
    
    # Final answer only depends on total_weighted and penalty_factor
    return round(final_result, 4)

# Main execution
weights = {
    'network_request': 1.5,
    'user_login': 2.0,
    'data_fetch': 1.8,
    'error_retry': 0.8
}

data_log = {
    'network_request': [
        {'time': '08:30', 'status': 200},
        {'time': '09:15', 'status': 200},
        {'time': '10:45', 'status': 200},
        {'time': '11:00', 'status': 200},
        {'time': '12:30', 'status': 200},
        {'time': '13:20', 'status': 200},
        {'time': '14:10', 'status': 200}
    ],
    'user_login': [
        {'time': '07:55', 'status': 200},
        {'time': '12:05', 'status': 200},
        {'time': '18:40', 'status': 200}
    ],
    'data_fetch': [
        {'time': '08:00', 'status': 200},
        {'time': '09:30', 'status': 200},
        {'time': '11:15', 'status': 200},
        {'time': '13:00', 'status': 200},
        {'time': '15:20', 'status': 200},
        {'time': '16:45', 'status': 200},
        {'time': '17:30', 'status': 200},
        {'time': '19:15', 'status': 200}
    ],
    'error_retry': [
        {'time': '08:35', 'status': 500},
        {'time': '09:20', 'status': 500}
    ]
}

timestamps = [entry['time'] for sublist in data_log.values() for entry in sublist]
processed_times = process_timestamps([{'time': t} for t in timestamps])
filtered_times = filter_anomalies(processed_times)

# Key statement
final_score = calculate_final_score(data_log, weights)

print(f"Target result: {final_score}")