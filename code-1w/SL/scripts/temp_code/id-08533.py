def analyze_pattern(sequence, threshold=3):
    count_map = {}
    for item in sequence:
        count_map[item] = count_map.get(item, 0) + 1

    excess_items = [k for k, v in count_map.items() if v > threshold]
    return excess_items


def transform_data(data_list):
    # Irrelevant transformation
    temp_result = []
    for idx, val in enumerate(data_list):
        if idx % 2 == 0:
            temp_result.append(val ** 2)
        else:
            temp_result.append(val + 1)
    return temp_result

# Misleading initialization
dummy_cache = {'status': 'inactive', 'data': [], 'version': 0.9}
tracking_log = []

# Core data
input_sequence = [4, 7, 4, 2, 8, 4, 9, 7, 4, 6, 7, 4]

# Distractor: unused function
def validate_entry(record):
    if isinstance(record, dict):
        return record.get('active', False)
    return False

# Another red herring: complex but unused logic
filtered_pairs = []
for i, x in enumerate(input_sequence):
    for j, y in enumerate(input_sequence):
        if i < j and (x + y) % 3 == 0:
            filtered_pairs.append((i, j, x, y))

# Real computation begins
freq_analysis = {}
for num in input_sequence:
    freq_analysis[num] = freq_analysis.get(num, 0) + 1

# Extract frequent elements above threshold
frequent_elements = [k for k, v in freq_analysis.items() if v >= 4]

# Secondary analysis: positional bias
even_index_values = [v for i, v in enumerate(input_sequence) if i % 2 == 0]
odd_index_values = [v for i, v in enumerate(input_sequence) if i % 2 == 1]

positional_bias = abs(sum(even_index_values) - sum(odd_index_values))

# Compute weighted importance
weights = {k: 1.5 if k % 2 == 0 else 0.8 for k in set(input_sequence)}
weighted_total = sum(freq_analysis[k] * weights[k] for k in freq_analysis)

# Decoy structure
audit_trail = []
for item in input_sequence:
    audit_trail.append(f"Processed: {item}")

# Tuple unpacking distraction
count_four, count_seven, count_other = 0, 0, 0
for value in input_sequence:
    if value == 4:
        count_four += 1
    elif value == 7:
        count_seven += 1
    else:
        count_other += 1

# Critical computation path
aggregation_keys = sorted(frequent_elements)
base_score = len(aggregation_keys) * 100

# Use of zip and enumerate together (required Python feature)
indexed_weights = list(enumerate(zip(aggregation_keys, [weights[k] for k in aggregation_keys])))
bonus_points = 0
for index, (key, w) in indexed_weights:
    bonus_points += index * key // max(1, int(w))

# Final calculation
final_score = base_score + bonus_points - positional_bias

# Dead code: never used
consistency_check = all(count_four >= count_seven, count_other < sum(freq_analysis.keys()) // 5)

# Print result as required
print(f"Result: {final_score}")