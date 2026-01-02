def analyze_productivity(logs):
    total_entries = len(logs)
    valid_records = []
    temp_sum = 0
    outlier_count = 0

    for entry in logs:
        duration = entry['time_spent']
        category = entry['category']
        status = entry['status']

        # Irrelevant filtering based on string length
        if len(category) > 5 and 'debug' not in category.lower():
            adjusted_duration = duration * 0.9
n        else:
            adjusted_duration = duration

        # Real logic: filter out outliers
        if 5 <= adjusted_duration <= 60:
            valid_records.append(adjusted_duration)
            temp_sum += adjusted_duration
        else:
            outlier_count += 1

    average_time = temp_sum / len(valid_records) if valid_records else 0
    return average_time, len(valid_records)


def calculate_consistency_factor(data):
    # Distractor function with dead logic
    if not data:
        return 0
    
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val

    # Fake consistency metric (not used)
    fake_metric = (max_val + min_val) / 2 if range_val < 30 else 0

    # Actual contribution: count of stable performers
    stable_count = sum(1 for x in data if x >= 20)
    return stable_count

# Simulated dataset
log_data = [
    {'time_spent': 45, 'category': 'Development', 'status': 'completed'},
    {'time_spent': 120, 'category': 'Meeting', 'status': 'review'},
    {'time_spent': 30, 'category': 'Testing', 'status': 'completed'},
    {'time_spent': 8, 'category': 'Deployment', 'status': 'failed'},
    {'time_spent': 55, 'category': 'Documentation', 'status': 'completed'},
    {'time_spent': 3, 'category': 'Planning', 'status': 'pending'},
    {'time_spent': 40, 'category': 'Refactoring', 'status': 'completed'}
]

# Intermediate processing with red herrings
raw_durations = [entry['time_spent'] for entry in log_data]
duration_labels = [str(d) + '_sec' for d in raw_durations]
dropped_tasks = [label for label in duration_labels if '120_sec' in label or '3_sec' in label]

avg_productivity, valid_task_count = analyze_productivity(log_data)

# Use of string method as required
label_summary = ''.join(duration_labels)
numeric_chars = ''.join(filter(str.isdigit, label_summary))
sum_of_digits = sum(int(c) for c in numeric_chars if c.isdigit())

consistency_bonus = calculate_consistency_factor([45, 30, 55, 40])

# Core accumulation logic
base_performance = avg_productivity * valid_task_count
penalty = 0
if valid_task_count < 5:
    penalty = 10

adjustment_factor = 1.1 if 'Dev' in log_data[0]['category'][:3] else 0.9

# Key statement
final_score = calculate_adjusted_performance()

# Definition delayed to increase cognitive load
def calculate_adjusted_performance():
    base = base_performance
    if consistency_bonus > 2:
        base += 15
    adjusted = base - penalty
    adjusted *= adjustment_factor
    return int(adjusted)

print(f"Result: {final_score}")