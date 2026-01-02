def analyze_performance(logs):
    total_entries = len(logs)
    valid_count = 0
    temp_sum = 0
    score_map = {}
    
    for log in logs:
        if not log.get('active', True):
            continue
        category = log['category']
        value = log['value']
        if category not in score_map:
            score_map[category] = []
        score_map[category].append(value)
        temp_sum += value
        valid_count += 1

    averages = {}
    for cat in score_map:
        averages[cat] = sum(score_map[cat]) / len(score_map[cat])
    
    # Distractor: unused computation
    max_avg = max(averages.values()) if averages else 0
    min_avg = min(averages.values()) if averages else 0
    spread = max_avg - min_avg

    return averages, valid_count


def calculate_adjustment(averages):
    adjustment = 0
    for k, v in averages.items():
        if 'critical' in k.lower():
            adjustment += v * 0.1
    return adjustment if adjustment > 0 else 0.5


def validate_keys(data_dict):
    # Irrelevant validation function (dead code path)
    for key in data_dict:
        if not key.isalpha():
            return False
    return True

# Main execution
log_data = [
    {'category': 'network_io', 'value': 85, 'active': True},
    {'category': 'memory_usage', 'value': 70, 'active': True},
    {'category': 'cpu_critical', 'value': 90, 'active': True},
    {'category': 'disk_io', 'value': 60, 'active': True},
    {'category': 'security_critical', 'value': 95, 'active': True},
    {'category': 'temp_sensor', 'value': 45, 'active': False},  # Inactive
    {'category': 'gpu_load', 'value': 80, 'active': True}
]

bonus_weights = {'A': 1.1, 'B': 1.2, 'C': 1.05}
threshold_check = any(v > 90 for v in bonus_weights.values())

# Extract ranks based on category length
rank_data = {}
for entry in log_data:
    cat = entry['category']
    rank_data[cat] = len(cat) % 7 + entry['value'] // 10

# Secondary processing with string methods
modifiers = []
for key in rank_data.keys():
    clean_key = key.replace('_', ' ').strip().title()
    word_count = len(clean_key.split())
    modifiers.append(word_count * 0.5)

base_modifier = sum(modifiers) / len(modifiers) if modifiers else 1

# Core calculation chain
averages, count = analyze_performance(log_data)
correction = calculate_adjustment(averages)

# Composite scoring with distractors
raw_total = sum(rank_data.values())
dummy_offset = sum(1 for x in rank_data if 'io' in x) * 2  # Irrelevant offset
adjusted_total = raw_total - dummy_offset

scaling_factor = base_modifier + correction
interim = adjusted_total * scaling_factor

penalty = 0
for val in rank_data.values():
    if val < 5:
        penalty += 10

final_score = int(interim - penalty)

# Print result as required
Target result: {final_score}