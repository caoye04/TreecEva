def analyze_response_time(rt):
    if rt < 0.1:
        return 'critical'
    elif rt < 0.5:
        return 'optimal'
    elif rt < 1.0:
        return 'acceptable'
    else:
        return 'poor'

# Irrelevant function - distractor
def compute_bandwidth_utilization(packets, size, duration):
    total_bits = packets * size * 8
    return total_bits / duration if duration > 0 else 0

# Decoy data - misleading intermediate values
historical_metrics = [0.45, 0.67, 0.23, 0.89, 1.02, 0.11, 0.51]
decay_factor = 0.85
adjusted_history = [x * decay_factor for x in historical_metrics]

# Simulated feedback levels from system components
feedback_raw = [0.34, 0.72, 0.15, 0.93, 0.61, 0.27, 0.49, 0.88]
feedback_levels = []
for response in feedback_raw:
    category = analyze_response_time(response)
    if category == 'critical':
        feedback_levels.append(1)
    elif category == 'optimal':
        feedback_levels.append(2)
    elif category == 'acceptable':
        feedback_levels.append(3)
    else:
        feedback_levels.append(4)

# Unused weight schema - red herring
temporal_weights = [0.9, 0.7, 0.5, 0.3]

# Relevant weights for aggregation
weights = [0.1, 0.15, 0.05, 0.2, 0.1, 0.15, 0.1, 0.1]  # Sum = 1.0

# Bit manipulation distraction
obfuscation_key = 23
scrambled = [(w * 100) ^ obfuscation_key for w in weights]
deobfuscated = sum([(s ^ obfuscation_key) for s in scrambled]) / 100

# Linear search in weighted mapping (unnecessary but plausible)
def find_weight_index(lst, val):
    for i, v in enumerate(lst):
        if abs(v - val) < 1e-6:
            return i
    return -1

# Create enumerated pairs for no real benefit - demonstrates enumerate
weight_pairs = list(enumerate(zip(feedback_levels, weights)))

# Dummy transformation using zip and enumerate
transformed = []
for idx, (fb, wt) in enumerate(zip(feedback_levels, weights)):
    transformed.append((idx, fb * 2 + wt))

# Core logic buried in distractions
def aggregate_performance(scores, wts):
    weighted_sum = 0.0
    for i in range(len(scores)):
        contribution = scores[i] * wts[i]
        weighted_sum += contribution
    
    # Additional logic with short-circuit evaluation
    penalty = 0.0
    if len(scores) > 5 and (min(scores) == 1 or max(wts) > 0.18):
        if any(x > 3 for x in scores[:3]):  # Short-circuit OR context
            penalty = 0.5 * min(weighted_sum, 2.0)
    
    # Modular adjustment based on sum components
    control_flag = (sum([int(f * w * 10) for f, w in zip(scores, wts)]) % 4) == 0
    adjustment = 0.25 if control_flag else -0.15
    
    result = weighted_sum + adjustment - penalty
    return round(result, 6)

# Dead code path - never called
def legacy_aggregate(data):
    return sum(data) / len(data)

# Critical execution point
final_score = aggregate_performance(feedback_levels, weights)

# Print required output
print(f"Target result: {final_score}")