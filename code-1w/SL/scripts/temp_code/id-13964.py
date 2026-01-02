def evaluate_performance(data, limits):
    score = 0
    penalty_adjustment = 0.0
    temp_buffer = []

    for key, value in data.items():
        if key.startswith('metric_'):
            base_weight = len(key) % 3 + 1
            raw_value = value['raw']
            norm_factor = value.get('normalized', 1)
            
            # Irrelevant normalization buffer (distractor)
            normalized_val = raw_value / (norm_factor if norm_factor > 0 else 1)
            temp_buffer.append(normalized_val)

            threshold_set = limits.get(key, {})
            warning_level = threshold_set.get('warning', 50)
            critical_level = threshold_set.get('critical', 75)

            # Real scoring logic
            if raw_value > critical_level:
                score -= 2 * base_weight
                penalty_adjustment += 0.25
            elif raw_value > warning_level:
                score -= 1 * base_weight
            else:
                score += base_weight

            # Dead computation: affects no outcome
            dummy_calc = (raw_value ** 0.5) * (base_weight % 2)
            dummy_calc = round(dummy_calc, 2)

    # Additional distraction: unused sorting
    temp_buffer.sort(reverse=True)
    if len(temp_buffer) > 3:
        temp_buffer = temp_buffer[:3]

    # Another red herring variable
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0

    # Final adjustment unrelated to main logic
    if score > 0 and penalty_adjustment > 0:
        score = int(score * (1 - penalty_adjustment))

    return score

# Main execution
config_flags = {'debug': False, 'trace': 0, 'mode': 'balanced'}
metric_data = {
    'metric_cpu': {'raw': 85, 'normalized': 100},
    'metric_memory': {'raw': 65, 'normalized': 90},
    'metric_disk': {'raw': 45, 'normalized': 80},
    'metric_network': {'raw': 90, 'normalized': 95}
}
thresholds = {
    'metric_cpu': {'warning': 60, 'critical': 80},
    'metric_memory': {'warning': 60, 'critical': 70},
    'metric_disk': {'warning': 50, 'critical': 85},
    'metric_network': {'warning': 70, 'critical': 85}
}

initial_offset = 5
final_score = 0
final_score = evaluate_performance(metric_data, thresholds)

# Simulate logging (irrelevant)
log_entry = f"Score computed: {final_score} with offset {initial_offset}"
message_parts = log_entry.split(' ')
formatted_log = ' | '.join([part.upper() for part in message_parts if len(part) > 2])

Result: {final_score}