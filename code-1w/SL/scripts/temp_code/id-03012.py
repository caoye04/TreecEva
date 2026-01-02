import math

def preprocess_signal(samples):
    # Irrelevant preprocessing function (dead code path)
    return [s * 0.95 for s in samples if s > 0]

def compute_entropy(values):
    # Misleading entropy calculation (not actually used in final result)
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)

def shift_cipher(text, offset):
    # Distractor: string manipulation unrelated to main logic
    return ''.join(chr((ord(c) - 97 + offset) % 26 + 97) if c.isalpha() else c for c in text)

def detect_anomalies(records, threshold=0.75):
    # Red herring function with complex logic but no impact
    anomalies = []
    for i, r in enumerate(records):
        if sum(r) / len(r) > threshold and i % 2 == 0:
            anomalies.append(i)
    return anomalies

def aggregate_metrics(stream, key):
    # Core function — actual computation path
    raw_values = []
    masks = [0b1010, 0b1100, 0b0110, 0b0011]
    temp_result = 0
    
    for i, chunk in enumerate(stream):
        # Use enumerate meaningfully
        masked_chunk = [(x ^ masks[i % 4]) & 0b1111 for x in chunk]  # Bitwise XOR and AND
        filtered = [v for v in masked_chunk if v % 3 == i % 3]  # Conditional filtering
        
        # Accumulate using modular arithmetic
        for j, val in enumerate(filtered):
            temp_result += (val * (j + 1)) % (i + 2)
        
        raw_values.append(sum(masked_chunk))
    
    # Combine with zip: pair with descending powers
    exponents = [4, 3, 2, 1]
    paired = zip(raw_values, exponents)
    weighted_sum = sum(value ** exp for value, exp in paired)  # Exponentiation chain
    
    # Final transformation based on key
    adjustment = 0
    for k in range(1, key + 1):
        if key % k == 0:
            adjustment += k
    
    # Actual answer computed here
    final_diagnostic = (weighted_sum // adjustment) - temp_result
    
    # Dead code: irrelevant list comprehension
    decoy_list = [math.sqrt(x) for x in range(100) if x % 7 == 0 and x not in raw_values]
    
    # Unused logical expression
    flag_status = (len(decoy_list) > 5) or (adjustment < 0) and not (weighted_sum < 1000)
    
    return final_diagnostic

# Simulated sensor data stream (4 chunks)
data_stream = [
    [12, 8, 14, 6],
    [10, 15, 7, 13],
    [9, 11, 16, 5],
    [14, 10, 8, 12]
]

analysis_key = 12

# Unused variables — red herrings
baseline = [10, 12, 11, 9]
calibration_offset = sum(baseline) / len(baseline)
entropy_score = compute_entropy(baseline)

# Trigger irrelevant functions
detect_anomalies([[0.8, 0.9], [0.6, 0.7], [0.85, 0.95]])
shift_cipher('debugmode', 13)

# Critical execution point
final_diagnostic = aggregate_metrics(data_stream, analysis_key)

print(f"Result: {final_diagnostic}")