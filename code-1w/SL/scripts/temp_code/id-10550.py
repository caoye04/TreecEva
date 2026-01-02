from itertools import combinations

# Simulate sensor data with noise and relevant signals
def generate_processed_data(raw):
    filtered = [x for x in raw if x > 30]
    smoothed = list(map(lambda y: round(y * 0.9), filtered))
    return smoothed

# Misleading auxiliary function that computes unused statistic
def compute_entropy(arr):
    from math import log
    freq_map = {}
    for val in arr:
        freq_map[val] = freq_map.get(val, 0) + 1
    total = len(arr)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Core computation with distractors
raw_readings = [25, 32, 35, 28, 45, 50, 33, 60, 29, 31]
noise_floor = 20
baseline_offset = 7

# Process data through pipeline
clean_data = generate_processed_data(raw_readings)

# Irrelevant transformations (distractors)
doubled_pairs = list(combinations(clean_data, 2))
summed_pairs = [a + b for a, b in doubled_pairs if a != b]
avg_pair_sum = sum(summed_pairs) / len(summed_pairs) if summed_pairs else 0

# Weight configuration (some weights are decoys)
weights = {
    'primary': 0.7,
    'secondary': 0.2,
    'tertiary': 0.1,
    'deprecated': 0.0  # unused weight
}

# Another red herring: string-based tag processing
tags = ['A', 'B', 'C']
tag_weights = {t: i + 1 for i, t in enumerate(tags)}
combined_tag_score = sum(len(t) * tag_weights[t] for t in tags)  # unused

# Real calculation begins here
def calculate_component_a(data):
    return sum(x ** 0.5 for x in data) * weights['primary']

def calculate_component_b(data):
    max_val = max(data) if data else 0
    min_val = min(data) if data else 0
    spread_bonus = (max_val - min_val) * weights['secondary']
    return spread_bonus

def calculate_auxiliary_factor(data):
    # This looks important but only adds fixed offset
    count = len(data)
    if count > 5:
        return weights['tertiary'] * 15
    return 0

def calculate_final_score(data, w):
    comp_a = calculate_component_a(data)
    comp_b = calculate_component_b(data)
    aux_f = calculate_auxiliary_factor(data)
    
    # Actual answer depends only on these components
    final_score = comp_a + comp_b + aux_f
    
    # Dead code branch (never executed but looks active)
    if False:
        fallback = sum(data) * w['deprecated']
        final_score = max(final_score, fallback)
    
    return final_score

# Key execution point
final_score = calculate_final_score(clean_data, weights)

# Output result as required
print(f"Target result: {final_score}")