def analyze_productivity(logs):
    total_entries = len(logs)
    valid_count = 0
    temp_sum = 0
    outliers = []

    for entry in logs:
        duration = entry['time_spent']
        if duration < 5:
            continue
        elif duration > 120:
            outliers.append(duration)
            continue
        else:
            valid_count += 1
            temp_sum += duration

    avg_time = temp_sum / valid_count if valid_count > 0 else 0
    return avg_time, len(outliers)


def calculate_efficiency_score(base, factor):
    if base <= 0:
        return 1
    score = 1
    while base > 1:
        base //= factor if factor > 1 else 1
        score += 1
        if factor <= 1:
            break
    return score

# Simulated daily activity metrics
activity_log = [
    {'task': 'login', 'time_spent': 3},
    {'task': 'edit_doc', 'time_spent': 45},
    {'task': 'review_data', 'time_spent': 150},
    {'task': 'send_email', 'time_spent': 12},
    {'task': 'meeting', 'time_spent': 78},
    {'task': 'debug_code', 'time_spent': 95},
    {'task': 'planning', 'time_spent': 2}
]

avg_duration, dropped = analyze_productivity(activity_log)
efficiency = calculate_efficiency_score(int(avg_duration), 15)

# Bonus logic based on string patterns in task names
task_names = [entry['task'] for entry in activity_log]
combined_name = '_'.join(task_names)
bonus_trigger = 'debug' in combined_name and 'edit' in combined_name
bonus_multiplier = 1.5 if bonus_trigger else 1.0

# Irrelevant distraction: counting vowels in task names
vowel_count = sum(1 for c in combined_name if c in 'aeiou')
dummy_ratio = vowel_count / len(combined_name) if len(combined_name) > 0 else 0

# Core metric computation with distractors
tier = 'senior' if avg_duration >= 40 else 'junior'
base_metrics = {
    'baseline': avg_duration,
    'efficiency': efficiency,
    'tier_bonus': 2 if tier == 'senior' else 1
}

scaling_factor = base_metrics['efficiency'] * base_metrics['tier_bonus']
raw_performance = base_metrics['baseline'] * scaling_factor

# Apply conditional adjustment using tuple unpacking
adjustments = (0.9, 1.1) if dropped < 3 else (0.7, 0.8)
lower_bound, upper_bound = adjustments
adjusted_performance = raw_performance * (upper_bound if bonus_multiplier > 1.2 else lower_bound)

# Final processing step
extra_buffer = (dummy_ratio * 100) // 1  # Distractor: not directly impactful

final_score = process_performance = lambda m, b: int(m['baseline'] + (adjusted_performance * b))
final_score = process_performance(base_metrics, bonus_multiplier)

print(f"Result: {final_score}")