import math

# Simulated health monitoring system with data processing and diagnostics

def analyze_heart_rate(data):
    avg_hr = sum(data) / len(data)
    variability = math.sqrt(sum((x - avg_hr) ** 2 for x in data) / len(data))
    return avg_hr, variability

# Irrelevant helper (distractor)
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Unused function (dead code path)
def legacy_normalize(x):
    return (x - min(x)) / (max(x) - min(x)) if max(x) != min(x) else 0

# Bit manipulation decoy
def encrypt_signal(signal):
    return signal ^ 0xFFFF & 0xAAAA

# Real processing chain
health_data = [72, 75, 68, 74, 71, 69, 73, 70, 76, 67]

# Conditional expression with lambda distractors
baseline_check = lambda x: 'normal' if x < 74 else 'elevated'
threshold_func = lambda x: x > 70 and (x + 5) % 17 != 0

# Irrelevant transformations
shifted_data = [encrypt_signal(x << 1) for x in health_data]  # Distractor using bitwise and encryption
filtered_data = [x for x in health_data if x > 68]  # Partial filtering (misleading)

# Set operations as per requirement
data_set = set(health_data)
expected_range = set(range(65, 80))
overlap = data_set & expected_range  # Relevant but indirect
anomaly_flags = data_set ^ {70, 71, 72, 73}  # XOR-based anomaly (red herring)

# Multiple assignment distraction
mean_val, var_val = analyze_heart_rate(health_data)
std_dev = math.sqrt(var_val)

# Complex conditional expression with nested logic
risk_level = 'low' if std_dev < 3 else 'medium' if mean_val < 73 else 'high'

# Core logic embedded within distractions
def process_metrics(data, threshold):
    # Step 1: Compute moving average over 3 elements
    mov_avg = [sum(data[i:i+3]) / 3 for i in range(len(data) - 2)]
    
    # Step 2: Apply threshold to detect anomalies
    anomalies = [i for i, x in enumerate(mov_avg) if threshold(int(x))]
    
    # Step 3: Transform using lambda and set reduction
    transformed = list(map(lambda x: int(x * 1.05), mov_avg))
    
    # Step 4: Use set difference to filter noise
    valid_indices = set(range(len(transformed))) - {0, len(transformed)-1}
    clean_vals = [transformed[i] for i in valid_indices]
    
    # Step 5: Compute weighted diagnostic score
    weights = [0.8, 1.0, 1.2, 0.9, 1.1][:len(clean_vals)]
    weighted_sum = sum(w * v for w, v in zip(weights, clean_vals))
    
    # Step 6: Adjust by logical conditions
    adjustment = 1.0
    if len(anomalies) > 0 and risk_level == 'low':
        adjustment = 0.95
    elif 'elevated' == baseline_check(mean_val):
        adjustment = 1.05
    
    # Step 7: Final computation
    diagnostic_score = weighted_sum * adjustment
    
    # Step 8: Floor and bit correction (final step)
    final_value = int(diagnostic_score) | (len(anomalies) << 2)
    
    return final_value

# Misleading intermediate call (does nothing)
_ = calculate_bmi(70, 1.75)

# Key statement
final_diagnostic = process_metrics(health_data, threshold_func)

# Output result
print(f"Result: {final_diagnostic}")