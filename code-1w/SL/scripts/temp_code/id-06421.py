def analyze_metrics(data_points):
    total = 0
    count = 0
    temp_offset = 0.0
    for val in data_points:
        if val > 0:
            total += val ** 0.5
            count += 1
        else:
            temp_offset += 1.5
    return int(total // (count or 1))

status_flags = {'active': True, 'verified': False}
data_set = [16, -5, 9, 25, -3]

interim_result = 0
for x in data_set:
    if x % 2 == 0:
        interim_result += x // 2
    else:
        interim_result -= x // 3

baseline = analyze_metrics(data_set)
adjustment_factor = 7 if status_flags['active'] else 3

bonus_tracker = []
counter_sim = 0
while counter_sim < len(data_set):
    if data_set[counter_sim] > 10:
        bonus_tracker.append(baseline * 2)
    elif data_set[counter_sim] > 0:
        bonus_tracker.append(baseline + adjustment_factor)
    else:
        bonus_tracker.append(0)
    counter_sim += 1

# Misleading auxiliary computation
phantom_sum = 0
for i in range(len(bonus_tracker)):
    phantom_sum += i * bonus_tracker[i] // (i + 1) if i % 2 == 0 else 0

# Core logic disguised among other operations
def calculate_performance(logs):
    base_perf = sum(logs)
    penalty = 0
    for entry in logs:
        if entry > 10:
            penalty += entry // 10
    # Additional distraction
    shift_value = 5 << 1
    dummy_mask = shift_value & 3
    return base_perf - penalty + (dummy_mask if len(logs) > 5 else 2)

final_score = calculate_performance(bonus_tracker)
print(f"Target result: {final_score}")