def analyze_signal(values, threshold):
    count = 0
    temp_sum = 0
    for v in values:
        if v > threshold:
            count += 1
            temp_sum += v
    return count if temp_sum > 0 else 0

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    import math
    freq_map = {}
    total = len(data)
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0
    for freq in freq_map.values():
        p = freq / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Unused transformation (dead code path)
def transform_sequence(seq):
    return [x ** 2 - x for x in seq if x % 2 == 0]

# Misleading normalization function (not actually used in final result)
def normalize_scores(scores):
    max_val = max(scores)
    return [round(s / max_val, 4) for s in scores]

# Simulated sensor readings (distractor data)
sensor_readings = [12, 7, 15, 3, 9, 22, 4, 8]
baseline_noise = 5
active_peaks = analyze_signal(sensor_readings, baseline_noise)

# Dummy statistical calculation (red herring)
total_energy = sum(x ** 2 for x in sensor_readings)
avg_power = round(total_energy / len(sensor_readings), 2)

# Core logic begins here — metric_data is constructed from non-obvious conditions
raw_metrics = [3, 7, -2, 0, 11, 5, -1, 9, 4]
filter_mask = [(x > 0) and ((x % 3) == 0 or (x % 7) == 0) for x in raw_metrics]
selected_indices = [i for i, valid in enumerate(filter_mask) if valid]

# Conditional expression usage (required python feature)
base_threshold = 4 if len(selected_indices) > 3 else 6

# Complex data transformation with nesting and filtering
def evaluate_performance(data, limit):
    adjusted = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed = val * 2
        else:
            transformed = val + 3
        
        # Nested condition with short-circuiting
        if transformed > limit and (transformed % 4 == 0 or transformed < 10):
            adjusted.append(transformed)
    
    # Secondary filter using conditional expression
    refined = [x if x <= 15 else x - 5 for x in adjusted]
    
    # Final aggregation with modular arithmetic twist
    cumulative = 0
    for j, num in enumerate(refined):
        weight = (j % 3) + 1
        cumulative += num * weight
    
    # Inject irrelevant local variable (distraction)
    debug_trace = [cumulative % k for k in range(2, 5)]
    
    return cumulative % 100000  # Ensure answer in range

# Additional unused list comprehension (distractor)
duplicate_check = [x for x in raw_metrics for _ in range(2)]

# Character counting red herring (string manipulation unrelated to result)
text_snapshot = "Signal:OK|Node=7|Len=9"
char_count = sum(1 for c in text_snapshot if c.isdigit())

dummy_tuple = (char_count, avg_power, active_peaks)

# Key execution point
metric_data = [x * 2 + 1 for x in raw_metrics]  # Non-trivial preprocessing
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")