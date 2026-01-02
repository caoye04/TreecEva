def analyze_pattern(sequence):
    count = 0
    for char in sequence:
        if char.isdigit():
            count += int(char) % 3
    return count

sequence = "x9y3z1a5b2"

# Irrelevant transformation (distractor)
transformed = ''.join([c.upper() if c.isalpha() else c for c in sequence])

# Dummy metric with partial relevance
offset = len(transformed) // 2

# Real data used in computation
raw_values = [7, -2, 5, 4, 8]
weights = [0.1, 0.3, 0.2, 0.3, 0.1]

# Misleading normalization (not actually used)
normalized = [val / max(raw_values) for val in raw_values if val > 0]

# Auxiliary function that appears important but only used once
def apply_weight(val, weight):
    return val * weight * 1.0

# Another distractor: checksum with no impact
checksum = 0
for i, c in enumerate(transformed):
    if c.isalpha():
        checksum ^= i + ord(c)

# State tracker (semi-relevant)
cumulative = 0
for v in raw_values:
    cumulative += abs(v)

# Key processing logic
weighted_sum = 0.0
for i in range(len(raw_values)):
    weighted_sum += apply_weight(raw_values[i], weights[i])

# Use of string method (required feature)
token_list = sequence.split('y')
length_metric = len(token_list[0]) + analyze_pattern(token_list[1])

# Dictionary operation (required feature)
metrics = {
    'base': weighted_sum,
    'adjustment': length_metric * 0.5,
    'penalty': offset // 3
}

# Final computation
final_score = int(metrics['base'] + metrics['adjustment'] - metrics['penalty'])

Result: final_score