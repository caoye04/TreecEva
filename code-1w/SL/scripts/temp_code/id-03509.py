import math

def preprocess_data(raw_entries):
    # Irrelevant preprocessing function (dead end)
    cleaned = [x.strip().lower() for x in raw_entries if x]
    return [c for c in cleaned if c.isalpha()]

def compute_metric_a(entries):
    # Distractor computation: operates on strings, not used in final result
    return sum(len(e) for e in entries) % 7

def auxiliary_transform(value, mode):
    # Misleading transformation with multiple branches, only one relevant
    if mode == 'encode':
        return (value << 2) ^ 15
    elif mode == 'decode':
        return (value >> 1) + 3
    else:
        return value

def validate_sequence(seq):
    # Red herring validation that looks important but isn't connected
    if len(seq) < 5:
        return False
    checksum = sum(seq[i] * (i + 1) for i in range(len(seq)))
    return checksum % 10 == 0

def temperature_compensation(temp, humidity):
    # Decoy scientific calculation
    factor = math.log(humidity + 1) / (temp + 273.15)
    adjusted = temp - (factor * 10)
    return round(adjusted, 2)

def bitwise_weighted_sum(arr):
    # Real contributor: computes weighted XOR sum
    total = 0
    for i, val in enumerate(arr):
        if i % 2 == 0:
            total ^= (val * 3)
        else:
            total += (val & 7)
    return total

def filter_outliers(values, threshold=100):
    # Looks useful but actually bypassed in logic path
    return [v for v in values if abs(v) < threshold]

def evaluate_performance(log, threshold):
    # Core logic buried among distractions
    
    # Step 1: Extract and transform key data
    raw_metrics = [x[1] for x in log if x[0] > 10]  # Filter by timestamp
    
    # Step 2: Apply bit manipulation chain
    transformed = []
    for val in raw_metrics:
        v1 = val ^ 245                # XOR operation
        v2 = (v1 + 17) % 1000         # Modular arithmetic
        v3 = auxiliary_transform(v2, 'other')  # Pass through decoy
        transformed.append(v3)
    
    # Step 3: Compute primary score via bitwise aggregation
    score_component = bitwise_weighted_sum(transformed)
    
    # Step 4: Secondary adjustment using list comprehension
    adjustments = [abs(int(str(x)[0]) - 5) * 2 for x in transformed if x > 0 and str(x).isdigit()]
    adjustment_sum = sum(adjustments)
    
    # Step 5: Combine components
    preliminary = score_component + adjustment_sum
    
    # Step 6: Threshold-based modulation
    if preliminary > threshold:
        preliminary -= threshold
    else:
        preliminary += threshold
    
    # Step 7: Final scaling
    scaled = int((preliminary * 1.75))
    
    # Step 8: Apply string-based offset (hidden use of string method)
    code_key = "F9J2M8K4"
    digit_sum = sum(int(c) for c in code_key if c.isdigit())  # String method: isdigit
    final_score = scaled - digit_sum
    
    # Irrelevant late-stage operations (distractors)
    _ = temperature_compensation(25, 60)
    _ = compute_metric_a(['test', 'run', 'log'])
    
    return final_score

# Simulated input data
base_threshold = 42

# Dead data structure (misleading)
data_stream = [
    (5, 100), (8, 205), (12, 310), (15, 415), (18, 520),
    (22, 625), (25, 730), (28, 835), (30, 940)
]

data_log = [
    (11, 19), (14, 28), (17, 37), (20, 46), (23, 55),
    (26, 64), (29, 73), (32, 82), (35, 91)
]

# Unused sorting (red herring)
sorted_log = sorted(data_log, key=lambda x: x[1], reverse=True)

# Key execution point
final_score = evaluate_performance(data_log, base_threshold)

# Output result
print(f"Result: {final_score}")