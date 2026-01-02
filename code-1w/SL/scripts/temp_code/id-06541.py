def analyze_pattern(sequence):
    count = 0
    temp_sum = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            count += 1
            temp_sum += val * (i + 1)
    return temp_sum


def filter_entries(data_list):
    filtered = []
    for item in data_list:
        if item > 0 and item % 3 != 0:
            filtered.append(item)
    padding_value = 999  # irrelevant tracking
    normalized = [x * 2 for x in filtered]  # extra processing
    return filtered


def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)


def calculate_ranking(items):
    base_total = 0
    adjustment_factor = 0.85
    for idx, num in enumerate(items):
        if idx < len(items) // 2:
            base_total += num * 1.5
        else:
            base_total += num * 0.75
    bonus = len(items) % 4  # minor bonus logic
    raw_score = base_total + bonus
    scaling_constant = 1.2  # unused in final path but defined
    final_rank = int(raw_score * adjustment_factor)
    return final_rank

# Main execution block
raw_sequence = [4, 15, 2, 9, 8, 12, 7, 5]

# Step 1: Analyze positional pattern
pattern_value = analyze_pattern(raw_sequence)

# Step 2: Filter valid entries (non-multiples of 3 and positive)
filtered_data = filter_entries(raw_sequence)

# Step 3: Compute information-theoretic entropy (distractor computation)
entropy_metric = compute_entropy(filtered_data)

# Step 4: Process data for ranking input
processed_data = []
for x in filtered_data:
    if x > 5:
        processed_data.append(x + pattern_value // 10)
    else:
        processed_data.append(x)

# Key statement
final_score = calculate_ranking(processed_data)

print(f"Result: {final_score}")