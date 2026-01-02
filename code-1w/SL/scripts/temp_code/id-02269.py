from collections import defaultdict
import math

def analyze_pattern(sequence):
    freq = defaultdict(int)
    for item in sequence:
        freq[item] += 1
    return freq

def normalize(value, min_val, max_val):
    if max_val == min_val:
        return 0.5
    return (value - min_val) / (max_val - min_val)

def process_metrics(converged, data_list):
    # Core logic variables
    base_metric = 0
    adjustment = 0
    temp_buffer = []

    # Irrelevant tracking (distractor)
    history_log = []
    for i in range(len(data_list)):
        if data_list[i] > 0:
            history_log.append(math.log(data_list[i] + 1))

    # Semi-relevant preprocessing
    filtered_data = [x for x in data_list if x >= 0]
    if not filtered_data:
        return 0

    avg_val = sum(filtered_data) / len(filtered_data)
    variance = sum((x - avg_val) ** 2 for x in filtered_data) / len(filtered_data)
    std_dev = math.sqrt(variance)

    # Normalization using min/max from data (semi-relevant)
    min_d = min(filtered_data)
    max_d = max(filtered_data)
    normalized_avg = normalize(avg_val, min_d, max_d)

    # Key branching logic
    if converged:
        base_metric = int(avg_val * 1.5)
        if std_dev < 10:
            adjustment = 8
        else:
            adjustment = 3
    else:
        base_metric = int(avg_val * 0.7)
        if avg_val > 25:
            adjustment = -5
        else:
            adjustment = 2

    # Dead computation path (distractor)
    checksum = 0
    for i, val in enumerate(filtered_data):
        if i % 3 == 0:
            checksum ^= int(val % 7)

    # String processing red herring
    status_flag = "Converged" if converged else "Pending"
    flag_lower = status_flag.lower()
    flag_upper = flag_lower.upper()
    flag_len = len(flag_upper.strip())

    # Final computation with tuple unpacking distraction
    offset, multiplier = (adjustment, 2) if base_metric > 30 else (adjustment, 1)
    intermediate = base_metric + offset
    final_score = intermediate * multiplier

    # Additional irrelevant aggregation
    letter_count = defaultdict(int)
    for c in flag_upper:
        letter_count[c] += 1

    # Only this line matters for output
    return final_score

# Simulate sensor readings
readings = [12, 15, 14, 10, 13, 16, 14, 12, 15]
convergence = True

# Execute main logic
temp_analysis = analyze_pattern([r % 5 for r in readings])
scaled_readings = [r * 1.1 for r in readings]
final_score = process_metrics(convergence, readings)
print(f"Result: {final_score}")