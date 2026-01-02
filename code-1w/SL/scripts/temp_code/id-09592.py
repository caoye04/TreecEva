def analyze_response_time(rt_list, base):
    avg = sum(rt_list) / len(rt_list)
    normalized = [round((rt - avg) / avg * 100) for rt in rt_list]
    return sum(normalized) // len(normalized)


def validate_input(data_str):
    if not data_str.isnumeric():
        return False
    checksum = sum(int(d) for d in data_str)
    return checksum % 2 == 0

# Simulated system performance metrics
task_completion_times = [120, 145, 130, 155, 160]
error_rates = [0.02, 0.01, 0.03, 0.02, 0.04]
dummy_data = "123456"

# Irrelevant intermediate calculations
response_deviation = analyze_response_time(task_completion_times, base=100)
valid_input = validate_input(dummy_data)
adjusted_errors = [int(e * 100) for e in error_rates]

# Key metric processing with distractors
total_time = sum(task_completion_times)
effective_rate = total_time // len(task_completion_times)
penalty_factor = 0
if effective_rate > 140:
    penalty_factor += 5
else:
    penalty_factor += 2

# Simulated score components
raw_scores = [max(100 - t//2, 0) for t in task_completion_times]
bonus = len([s for s in raw_scores if s >= 90])

# Distractor: unused computation path
temp_weights = [0.8, 1.1, 0.9, 1.2, 1.0]
scaled_scores = [raw_scores[i] * temp_weights[i] for i in range(len(raw_scores))]

# Threshold logic with string method involvement
category_label = "performance_high"
threshold = 85
if category_label.endswith("high") and valid_input:
    threshold -= 5
else:
    threshold += 3

# Core assignment with multiple influences
metrics = [raw_scores[i] - adjusted_errors[i] for i in range(len(raw_scores))]

# Final computation with conditional adjustment
def process_performance(mets, thresh):
    count_above = 0
    for val in mets:
        if val > thresh:
            count_above += 1
    base_score = sum(mets) // len(mets)
    extra_weight = bonus if response_deviation < 10 else 0  # uses outer-scope var
    return base_score + extra_weight - penalty_factor

final_score = process_performance(metrics, threshold)
print(f"Result: {final_score}")