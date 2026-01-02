def transform_sequence(seq, modifier):
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2
    left = transform_sequence([x * 0.5 for x in seq[:mid]], modifier + 1)
    right = transform_sequence([x * 1.5 for x in seq[mid:]], modifier - 1)
    return [x + modifier for x in left + right]

# Irrelevant transformation chain (dead path)
def obsolete_conversion(data):
    return [chr((ord(ch) + 3) % 26 + ord('a')) for ch in data]

def evaluate_symmetry(value):
    s = str(value)
    return s == s[::-1]

def collect_metrics(raw_values):
    stats = {}
    stats['max'] = max(raw_values)
    stats['min'] = min(raw_values)
    stats['range'] = stats['max'] - stats['min']
    stats['median'] = sorted(raw_values)[len(raw_values)//2]
    # Distractor computation
    temp_calc = sum(x ** 0.5 for x in raw_values if x > 0) / len(raw_values)
    return stats

def filter_outliers(data_list, limit=50):
    # Unused filtering logic (misleading)
    return [x for x in data_list if abs(x - sum(data_list)/len(data_list)) < limit]

def integrate_series(n):
    if n <= 1:
        return n
    return n + integrate_series(n - 2)

# Core logic with distractors
def analyze_pattern(dataset, criteria):
    processed = []
    for item in dataset:
        if item in criteria:
            processed.append(item * 2)
        else:
            processed.append(item // 3)
    
    # Decoy aggregation
    fake_aggregate = sum(x * x for x in processed) % 97
    
    # Real result path
    base_sum = sum(processed)
    adjustment = len(criteria.intersection(set(processed)))
    final_score = base_sum + adjustment
    
    # More red herrings
    debug_trace = []
    for i in range(3):
        debug_trace.append({"step": i, "value": (i * final_score) % 43})
    
    return final_score

# Initialization block
raw_input = [12, 18, 24, 36, 48, 54]
scaling_factor = 3

# Apply non-essential transformation (distractor)
shifted_values = [x + scaling_factor for x in raw_input]

# Recursively transformed sequence (unused result)
transformed_chain = transform_sequence(shifted_values, 2)

# Collect metrics on original data
metrics_summary = collect_metrics(raw_input)

# Generate threshold set using set operations (critical)
threshold_candidates = {x for x in raw_input if x % 6 == 0}
evasion_set = {x for x in raw_input if x > 30}
threshold_set = threshold_candidates - evasion_set  # Final relevant set

# Simulate irrelevant system state
system_status = {"active": True, "mode": "diagnostic", "level": 7}

# Data collection with decoy processing
collected_data = []
counter = 0
for val in raw_input:
    counter += 1
    if evaluate_symmetry(val):  # Always false, dead condition
        collected_data.append(val * 10)
    else:
        collected_data.append(integrate_series(val % 25))

# Key statement
final_diagnostic = analyze_pattern(collected_data, threshold_set)

# Print result
print(f"Result: {final_diagnostic}")