from collections import defaultdict, Counter

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_readings(raw):    
    # Irrelevant transformation (dead path)
    temp_offsets = [x * 0.1 for x in raw if x > 50]
    adjusted = [x + 5 for x in raw]
    filtered = [x for x in adjusted if x < 100]
    return filtered

# Distractor function – never called
def compute_gradient(data):
    return [data[i+1] - data[i] for i in range(len(data)-1)]

# Another decoy: statistical outlier removal (unused)
def remove_outliers(values, factor=1.5):
    q1, q3 = sorted(values)[len(values)//4], sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    return [v for v in values if q1 - factor*iqr <= v <= q3 + factor*iqr]

# Real processing begins here
raw_input = [23, 85, 67, 44, 91, 58, 67, 33, 42]

# Misleading normalization path
normalized = []
total = sum(raw_input)
for val in raw_input:
    norm_val = (val / total) * 100
    if norm_val > 20:
        normalized.append(int(norm_val))

# Actual relevant transformation chain
encoded = [(x ^ 7) + 2 for x in raw_input]  # Bit manipulation + arithmetic
masked = [x for x in encoded if x % 2 == 1]  # Only odd values retained

# Decoy data structure
stats_summary = {
    'count': len(raw_input),
    'peak': max(raw_input),
    'average': sum(raw_input)/len(raw_input),
    'ignored_metric': sum(x*x for x in raw_input)
}

# Build frequency map (partially relevant)
freq_map = Counter(masked)

# Create threshold logic with red herring conditions
threshold_map = defaultdict(lambda: 2)
for k in freq_map:
    if k > 50:
        threshold_map[k] = 3
    elif k < 40:
        threshold_map[k] = 1  # Rare case
    else:
        threshold_map[k] = 2  # Default override

# Transform based on frequency and thresholds
dynamic_weights = []
for val in set(masked):
    weight = freq_map[val] * threshold_map[val]
    # Dead condition below (never triggers due to data)
    if weight > 10:
        weight = 10
    dynamic_weights.append(weight)

# Apply non-linear transformation
transformed_data = []
for i, w in enumerate(dynamic_weights):
    # Conditional expression twist
    transformed_value = (w ** 2) if i % 2 == 0 else (w + 5) * 1.5
    # Artificial truncation
    if transformed_value > 50:
        transformed_value = 49.9
    transformed_data.append(round(transformed_value, 3))

# Real analysis function
def analyze_pattern(data, thresholds):
    score = 0
    # Linear search over transformed data
    for val in data:
        if val >= 20.0:
            score += int(val // 3)
        else:
            score -= 1
    # Conditional branch based on length
    if len(data) > 3:
        score *= 2
    else:
        score += 5
    
    # Hidden dependency: count of original masked elements above 50
    special_bonus = sum(1 for x in masked if x > 50)
    score += special_bonus * 4

    # Final obfuscation via bitwise shift
    score = (score << 1) >> 1  # No change, but looks complex

    return score

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold_map)

print(f"Result: {final_diagnostic}")