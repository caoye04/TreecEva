import math

def analyze_component(x, y):
    # Irrelevant transformation (dead end)
    temp = (x ** 2 + y ** 2) ** 0.5
    if temp > 100:
        return temp / 4
    return x - y

def calculate_entropy(values):
    # Distractor function: looks important but unused in critical path
    total = sum(values)
    entropy = 0
    for v in values:
        p = v / total if total else 0
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

def filter_outliers(data, limit=50):
    # Semi-relevant but ultimately bypassed logic
    cleaned = [x for x in data if abs(x) < limit]
    return cleaned if len(cleaned) > 3 else data

def process_metrics(raw, mode='strict'):
    # Complex-looking preprocessing with red herring paths
    adjusted = []
    scaling_factor = 1.75
    offset = 0

    for val in raw:
        if mode == 'strict' and val < 0:
            offset += 0.1
        transformed = val * scaling_factor + offset
        adjusted.append(round(transformed, 2))

    # Dead code path based on unreachable condition
    if len(adjusted) > 100:
        return [x for x in adjusted if x > 10]
    
    return adjusted[:15]  # Truncate to manageable size

def evaluate_performance(metrics, threshold):
    # Core logic buried in distractions
    count_valid = 0
    cumulative = 0.0
    penalty = 0

    # Simulated state machine with decoy states
    state_flags = {'calibrated': True, 'verified': False, 'locked': None}
    if len(metrics) % 2 == 0:
        state_flags['verified'] = True
    if metrics[0] > 0:
        state_flags['locked'] = False

    # Real logic begins here — deeply nested
    for i, score in enumerate(metrics):
        # Red herring: complex conditional that doesn't affect final outcome
        if i % 4 == 0 and score > threshold * 1.2:
            penalty += 1
        elif i % 3 == 0 and score < threshold * 0.8:
            penalty += 2

        # Actual contribution to result
        if score >= threshold:
            count_valid += 1
            cumulative += score

    # Decoy calculation using state flags
    if state_flags['calibrated'] and not state_flags['locked']:
        cumulative *= 1.1  # Misleading adjustment

    # Critical result computation
    avg_contribution = cumulative / count_valid if count_valid else 0
    bonus = 10 if count_valid >= 6 else 5 if count_valid >= 4 else 0
    final_value = avg_contribution + bonus - penalty * 0.5

    return int(round(final_value))

# --- Main execution with layered distractions ---

# Irrelevant data initialization
raw_system_logs = [23, 15, -7, 44, 89, 12, 50, 31, 77, 65, 91, 4, 29]
log_entropies = calculate_entropy([len(raw_system_logs), 5, 3, 1])

# Distractor list comprehension with unused result
anomalies = [x for x in raw_system_logs if x < 0 or x > 80]

# Real input data hidden among noise
metric_data = [
    12, 18, 25, 30, 42,  
    55, 60, 63,         
    48, 33              
]

# Unused transformations
filtered_data = filter_outliers(metric_data, limit=55)
processed_data = process_metrics(metric_data, mode='loose')

# Key parameters mixed with decoys
base_threshold = 24
activation_limit = 19  # Looks important but unused
emergency_cap = 999      # Red herring constant

# Simulate irrelevant state tracking
system_state = {"active": True, "phase": 2, "debug": False}
if system_state["phase"] == 2:
    system_state["updated"] = True

# Critical assignment buried in context
final_score = evaluate_performance(metric_data, base_threshold)

# Output required format
print(f"Result: {final_score}")