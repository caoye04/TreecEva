def detect_outliers(data, threshold):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return {x for x in data if abs(x - mean_val) > threshold * std_dev}

baseline_data = [12, 15, 18, 19, 20, 22, 25, 27, 30, 32]
baseline_set = set(baseline_data)

# Simulate sensor readings with noise
temp_readings = [14, 17, 19, 20, 21, 23, 26, 28, 33, 35, 100, 102]
noise_floor = 1.5

# Detect anomalies using statistical method
anomalies = detect_outliers(temp_readings, noise_floor)

# Irrelevant helper: computes pairwise XOR (not used in final logic)
def compute_pairwise_xor(vals):
    result = 0
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            result ^= (vals[i] ^ vals[j])
    return result

unused_xor_sum = compute_pairwise_xor([10, 20, 30])  # Dead computation

# Auxiliary metric: count transitions across median
sorted_vals = sorted(temp_readings)
median_val = sorted_vals[len(sorted_vals) // 2]
transitions = sum(1 for i in range(1, len(sorted_vals))
                   if (sorted_vals[i-1] < median_val) != (sorted_vals[i] < median_val))

# Secondary distraction: simulate redundant filtering
filtered_during_stream = [x for x in temp_readings if x < 90]
duplicate_check_set = {x for x in filtered_during_stream if x % 2 == 0}

# Core evaluation logic
evaluate_performance = lambda outliers, base: \
    len(outliers) * 10 - len(base.intersection(outliers)) + \
    (5 if len(outliers) > 2 else 0)

intermediate_diagnostic = len(anomalies.intersection(baseline_set))

# Key statement
current_state_flag = True if len(anomalies) >= 2 else False
final_score = evaluate_performance(anomalies, baseline_set)

print(f"Result: {final_score}")