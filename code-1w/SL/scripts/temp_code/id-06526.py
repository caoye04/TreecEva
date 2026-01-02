def normalize_data(data_list):
    min_val, max_val = min(data_list), max(data_list)
    if max_val == min_val:
        return [0.5 for _ in data_list]
    return [(x - min_val) / (max_val - min_val) for x in data_list]

# Irrelevant function - dead code path
def legacy_calculate(x):
    return sum([i**2 for i in range(x)]) // 2

# Misleading intermediate variables
temp_buffer = [12, 18, 24, 36]
scaling_factor = 3.14159
dummy_weights = [0.1, 0.2, 0.7]  # Not used in final calculation

# Real data processing begins
raw_metrics = [88, 72, 91, 65, 83]
processing_mode = 'optimized'

if processing_mode == 'legacy':
    processed = [x * 0.95 for x in raw_metrics]
elif processing_mode == 'experimental':
    processed = [x + 5 for x in raw_metrics if x < 80]
else:
    processed = raw_metrics

# Normalize the selected metrics
normalized = normalize_data(processed)

# Simulate string-based configuration parsing (uses string method)
config_str = "threshold:0.7|activation:relu|version:2.1"
config_pairs = config_str.split('|')
config_dict = {pair.split(':')[0]: pair.split(':')[1] for pair in config_pairs}

activation_fn = config_dict.get('activation')
threshold = float(config_dict.get('threshold'))

# Distractor: unused sorting
sorted_normalized = sorted(normalized, reverse=True)

# Weight assignment with red herring logic
weights = []
for i in range(len(normalized)):
    if i % 2 == 0:
        weights.append(0.3)
    else:
        weights.append(0.2)

# Extra weight normalization (distractor)
total_weight = sum(weights)
normalized_weights = [w / total_weight for w in weights]

# Decoy function using bitwise operations (never called)
def bit_analysis(value):
    bin_str = bin(value)[2:]
    ones = bin_str.count('1')
    zeros = bin_str.count('0')
    return ones ^ zeros

# Real evaluation logic
weighted_sum = sum(n * w for n, w in zip(normalized, normalized_weights))

# Apply threshold logic based on activation
if activation_fn == 'relu' and weighted_sum > threshold:
    adjusted_score = (weighted_sum - threshold) * 100
else:
    adjusted_score = 50

# Final transformation using modular arithmetic
mod_value = int(adjusted_score * 100) % 89
final_score = round(adjusted_score + mod_value / 100.0, 4)

# Critical output statement
print(f"Result: {final_score}")