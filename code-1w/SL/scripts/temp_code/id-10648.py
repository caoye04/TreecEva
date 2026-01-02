def analyze_readings(readings):
    # Irrelevant data processing (red herring)
    avg = sum(readings) / len(readings)
    squared_devs = [(x - avg)**2 for x in readings]
    variance = sum(squared_devs) / len(squared_devs)
    return variance

# Decoy dataset (not used in final computation)
data_stream = [12, 15, 18, 22, 25, 30, 35]
analyze_readings(data_stream)

threshold_map = {'low': 10, 'high': 30}

def filter_critical(values, mode='exclude'):
    # Unused function - dead code path
    if mode == 'exclude':
        return [v for v in values if threshold_map['low'] <= v <= threshold_map['high']]
    return values

# Core logic begins here
def transform_sequence(seq):
    # Apply bitwise and arithmetic transformations
    transformed = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            transformed.append((val << 1) + 3)  # Left shift and add
        else:
            transformed.append(val ^ 7)  # XOR with 7
    return transformed

def compute_entropy(values):
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)

# Distractor: unused entropy call on decoy data
compute_entropy([1, 1, 2, 3, 5])

base_metrics = [4, 8, 15, 16]

# Multi-step transformation chain
stage_one = transform_sequence(base_metrics)
stage_two = [x * 2 for x in stage_one if x > 10]  # Filter and scale

# Introduce set operations (required feature)
observed_set = {x % 19 for x in stage_two}
expected_set = {2, 4, 6, 8, 12, 14, 16}
metric_set = observed_set & expected_set  # Intersection: relevant

# Dead computation with misleading name
phantom_score = len(observed_set | expected_set) * 17

# Conditional logic with red herring branch
if len(metric_set) > 10:
    adjustment = -5
elif len(metric_set) > 5:
    adjustment = 3
else:
    adjustment = 1  # This will be taken

# Sorting and linear search (suggested paradigms)
sorted_metrics = sorted(list(metric_set), reverse=True)
position = -1
for idx, val in enumerate(sorted_metrics):
    if val == 12:
        position = idx
        break

# Final evaluation function with nested logic
def evaluate_performance(metrics):
    base = sum(metrics)
    
    # Nested conditionals (3 levels deep)
    if base > 0:
        if len(metrics) % 2 == 0:
            for m in metrics:
                if m % 3 == 0:
                    base *= 1.5
                    break
            else:
                base *= 0.9
        else:
            base += 5
    else:
        base = 100
    
    # Logical operations and short-circuiting
    bonus = (len(metrics) >= 3) and (sorted_metrics[0] > 10) or (adjustment > 5)
    penalty = not (base > 20) and (position != -1)
    
    result = base + (10 if bonus else 0) - (8 if penalty else 0)
    return int(round(result))

# Key statement
final_score = evaluate_performance(metric_set)
print(f"Target result: {final_score}")