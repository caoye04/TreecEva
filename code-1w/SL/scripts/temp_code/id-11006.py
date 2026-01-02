def analyze_metrics(raw_data):
    temp_buffer = []
    for item in raw_data:
        if item % 3 == 0:
            temp_buffer.append(item * 2)
        elif item % 5 == 0:
            temp_buffer.append(item + 10)
    return temp_buffer

# Irrelevant transformation chain (distractor)
def transform_sequence(seq):
    result = []
    for x in seq:
        if x < 50:
            result.append(x ** 0.5)
    return [round(r, 2) for r in result]

# Unused helper (dead code path)
def compute_baseline(values):
    total = 0
    for v in values:
        total += v % 7
    return total // len(values) if values else 0

# Core logic with red herrings
def filter_anomalies(data_stream):
    anomalies = []
    normal_vals = []
    threshold = sum(data_stream) / len(data_stream) if data_stream else 0
    
    for val in data_stream:
        if abs(val - threshold) > 15:
            anomalies.append(val)
        else:
            normal_vals.append(val)
    
    # Misleading intermediate: looks important but unused later
    anomaly_count_ratio = len(anomalies) / len(data_stream) if data_stream else 0
    
    return normal_vals  # Only normals used forward

# Data preprocessing with list comprehension (relevant)
def preprocess(signal):
    cleaned = [x for x in signal if x > 0]  # Remove negatives
    extended = cleaned + [sum(cleaned[:3])]   # Add synthetic feature
    return extended

# Bit manipulation decoy (irrelevant)
def flag_encoder(n):
    encoded = 0
    for i in range(8):
        encoded |= (n & 1) << (7 - i)
        n >>= 1
    return encoded

# Main evaluation logic
def evaluate_performance(metrics):
    base = sum(metrics)
    adjustment = 0
    
    # Conditional adjustments based on patterns
    if len(metrics) > 5:
        adjustment += 10
    if metrics[-1] > metrics[0]:
        adjustment += 5
    
    # Nested condition with distractors
    secondary_check = False
    temp_sum = 0
    for m in metrics:
        temp_sum += m
        if temp_sum > 100:
            secondary_check = True
            break
    
    # Decoy variable that seems impactful
    pseudo_weight = temp_sum * 0.1 if secondary_check else 0
    
    # Actual key logic
    if secondary_check and adjustment > 0:
        base -= 20  # Critical adjustment
    
    return base + adjustment

# --- Execution Flow ---
raw_input = [12, 18, 25, 9, 44, 7, 30, 3]
data_pipeline = analyze_metrics(raw_input)
processed_signal = preprocess(data_pipeline)  # [24, 36, 35, 18, 88] -> sum first 3: 24+36+35=95
filtered_results = filter_anomalies(processed_signal)  # No anomaly above threshold (~42.2)

# Red herring function call (no side effects)
decoy_flags = [flag_encoder(x) for x in filtered_results if x % 10 == 0]

# Linear search mimic (unnecessary but plausible)
index_marker = -1
for i, val in enumerate(filtered_results):
    if val == 88:
        index_marker = i

# Key statement
final_score = evaluate_performance(filtered_results)

print(f"Result: {final_score}")