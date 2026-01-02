def analyze_trend(values):
    if len(values) < 2:
        return 0
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
    return trend

# Irrelevant helper (distractor)
def compute_entropy(data):
    import math
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Unused function (dead code path)
def validate_input(arr):
    return all(isinstance(x, (int, float)) for x in arr) and len(arr) > 0

# Decoy transformation
def shift_sequence(seq, offset=3):
    result = [0] * len(seq)
    for idx, val in enumerate(seq):
        result[(idx + offset) % len(seq)] = val
    return result

# Misleading normalization routine (not actually used in final logic)
def normalize_weights(ws):
    total = sum(ws)
    return [w / total for w in ws] if total != 0 else ws

# Core logic disguised among noise
def process_metrics(metrics, importance):
    base = 0
    adjustments = 0
    
    # Real computation starts here
    for index, (val, weight) in enumerate(zip(metrics, importance)):
        if val < 0:
            continue
        temp_val = val ** 0.5
        if index % 2 == 0:
            base += temp_val * weight
        else:
            adjustments += weight * (temp_val * 0.1)
    
    # Secondary real operation: correction factor based on trend
    trend_factor = analyze_trend(metrics)
    if trend_factor > 2:
        base *= 1.2
    elif trend_factor == 0:
        base *= 0.8
    
    # Final score calculation (this is the key line)
    final_score = int(base + adjustments)
    
    # Red herring: unused intermediate
    decoy_result = shift_sequence(importance)
    entropy_check = compute_entropy(metrics)
    
    return final_score

# Irrelevant data block
dummy_logs = [
    {'event': 'start', 'ts': 1001},
    {'event': 'ping', 'ts': 1005},
    {'event': 'pong', 'ts': 1009}
]

# Actual input data
raw_data = [16, 25, 9, 0, 49, 36]
weights = [1, 2, 3, 4, 5, 6]

# Trigger processing
data = [x - 10 for x in raw_data]  # Introduce negatives
final_score = process_metrics(data, weights)

# Output result as required
print(f"Target result: {final_score}")