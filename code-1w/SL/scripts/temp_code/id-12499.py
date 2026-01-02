def analyze_trend(values):
    trend_scores = []
    for i, val in enumerate(values):
        if i == 0:
            trend_scores.append(0)
        else:
            diff = val - values[i-1]
            trend_scores.append(1 if diff > 0 else (-1 if diff < 0 else 0))
    return trend_scores

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 0.5 for x in data if x > 10]

# Misleading computation with unused variables
temp_offset = 3.1415
counter_shadow = [0] * 5
useless_matrix = [[i*j for j in range(3)] for i in range(3)]

benchmark_data = [12, 15, 15, 18, 20, 19, 25, 25, 26]
smoothing_factor = 0.2
adjusted_values = [round(x * smoothing_factor) for x in benchmark_data]

# Semi-relevant transformation
trend_sequence = analyze_trend(benchmark_data)

# Dictionary-based scoring map
category_map = {
    'up': 3,
    'flat': 1,
    'down': -2
}

score_lookup = {}
for idx, trend in enumerate(trend_sequence):
    key = f'trend_{idx}'
    if trend == 1:
        score_lookup[key] = category_map['up']
    elif trend == 0:
        score_lookup[key] = category_map['flat']
    else:
        score_lookup[key] = category_map['down']

# Simulate redundant string-based tagging
tagged_scores = []
for k, v in score_lookup.items():
    tag = k.replace('trend', 'entry').upper()
    padded_tag = tag + 'X' * (10 - len(tag))
    tagged_scores.append(v)

# Secondary transformation with zip and enumerate
double_weighted = []
for i, (orig, adj) in enumerate(zip(benchmark_data, adjusted_values)):
    if adj > 3:
        double_weighted.append(orig // 2)
    else:
        double_weighted.append(orig)

# Final performance calculation
running_total = 0
penalty_count = 0
for i, val in enumerate(double_weighted):
    if i > 0 and double_weighted[i] < double_weighted[i-1]:
        penalty_count += 1
    running_total += val % 7

base_score = sum(tagged_scores)
adjustment = running_total - penalty_count * 2

# Key computation with distractor variables around it
auxiliary_flag = len([x for x in benchmark_data if x % 5 == 0])
dummy_cache = {i: i**2 for i in range(10)}
scaling_constant = 1.0  # Never updated

final_score = calculate_performance(benchmark_data)

# Redefine function to avoid undefined error — contains logic
# Note: This function uses multiple concepts and distractors
def calculate_performance(data):
    n = len(data)
    if n == 0:
        return 0
    
    # String method distraction
    data_name = "performance_run"
    suffix = data_name.split('_')[-1].title()
    
    # Actual logic begins
    diffs = [data[i+1] - data[i] for i in range(n-1)]
    pos_changes = sum(1 for d in diffs if d > 0)
    zero_changes = sum(1 for d in diffs if d == 0)
    neg_changes = sum(1 for d in diffs if d < 0)
    
    # Weighted contribution
    raw_score = 5 * pos_changes + 2 * zero_changes - 3 * neg_changes
    
    # Normalize by length with rounding
    normalized = int(raw_score / (n - 1)) if n > 1 else raw_score
    
    # Use dictionary get with default
    multiplier = {'early': 2, 'late': 1}.get(suffix.lower(), 1)
    
    # Use enumerate and zip together in filtering
    filtered_pairs = []
    for idx, (a, b) in enumerate(zip(data, data[1:])):
        if a <= b:
            filtered_pairs.append((idx, a, b))
    
    # Additional contribution based on ascending pairs
    bonus = sum((b - a) for _, a, b in filtered_pairs if b - a < 5)
    
    # Final formula
    result = normalized + bonus
    
    # Dead code branch (never executed but looks relevant)
    if False:
        fallback = 0
        for k in dummy_cache:
            fallback += k
        result = fallback
    
    return result

# Recompute final_score after function definition
def calculate_performance(data):
    n = len(data)
    if n == 0:
        return 0
    
    diffs = [data[i+1] - data[i] for i in range(n-1)]
    pos_changes = sum(1 for d in diffs if d > 0)
    zero_changes = sum(1 for d in diffs if d == 0)
    neg_changes = sum(1 for d in diffs if d < 0)
    
    raw_score = 5 * pos_changes + 2 * zero_changes - 3 * neg_changes
    normalized = int(raw_score / (n - 1)) if n > 1 else raw_score
    
    filtered_pairs = []
    for idx, (a, b) in enumerate(zip(data, data[1:])):
        if a <= b:
            filtered_pairs.append((idx, a, b))
    
    bonus = sum((b - a) for _, a, b in filtered_pairs if b - a < 5)
    
    return normalized + bonus

final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")