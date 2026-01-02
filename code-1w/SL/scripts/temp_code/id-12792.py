def analyze_trends(data, threshold=10):
    trend_count = 0
    temp_buffer = []
    for val in data:
        if val > threshold:
            trend_count += 1
            temp_buffer.append(val * 0.1)
    return trend_count

legacy_data = [5, 12, 15, 8, 20]
backup_copy = legacy_data[:]
discardable_sum = sum(x ** 2 for x in backup_copy if x < 10)

primary_metrics = [3, 14, 18, 7, 19, 22]
secondary_metrics = [x for x in primary_metrics if x > 12]

size_flag = 'L' if len(secondary_metrics) > 3 else 'S'

interim_result = 0
for i, val in enumerate(primary_metrics):
    if i % 2 == 0 and val > 10:
        interim_result += val // 2

reference_map = {i: v * 2 for i, v in enumerate(primary_metrics)}
scaled_values = [reference_map[i] for i in range(len(primary_metrics)) if i % 2 == 1]

feedback_set = set()
counter_var = 0
for val in scaled_values:
    if val > 15:
        feedback_set.add(counter_var)
        counter_var += 1

auxiliary_total = 0
for i in range(len(scaled_values)):
    auxiliary_total += i * 2 if i < 5 else i * 3

snapshot_log = []
for entry in feedback_set:
    snapshot_log.append(f"Entry_{entry}")

status_flags = ['active' if x in feedback_set else 'idle' for x in range(5)]

adjusted_interim = interim_result + 1 if interim_result < 30 else interim_result - 5

outlier_check = any(x > 40 for x in scaled_values)

metadata_enriched = {k: v for k, v in enumerate(status_flags)}

buffer_overflow_sim = 0
for _ in range(3):
    buffer_overflow_sim += 2  # Simulated overhead, no real impact

final_score = 0
def evaluate_performance(feedbacks):
    base = len(feedbacks) * 5
    bonus = 2 if adjusted_interim >= 20 else 0
    penalty = 1 if outlier_check else 0
    return base + bonus - penalty

final_score = evaluate_performance(feedback_set)
print(f"Result: {final_score}")