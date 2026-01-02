from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    trend_values = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            count += 1
            trend_values.append(sequence[i] - sequence[i-1])
    return count, sum(trend_values) if trend_values else 0

def validate_entry(tag):
    if not isinstance(tag, str):
        return False
    cleaned = tag.strip().lower()
    return cleaned.isalpha() and len(cleaned) >= 3

def compute_risk_factor(data_points):
    risk_counter = 0
    magnitude_total = 0.0
    temp_buffer = []
    for val in data_points:
        if val < 0:
            risk_counter += 1
        magnitude_total += abs(val)
        temp_buffer.append(abs(val) ** 0.5)
    avg_magnitude = magnitude_total / len(data_points) if data_points else 0
    filtered_sqrt = [x for x in temp_buffer if x > 1.0]
    return risk_counter, avg_magnitude, len(filtered_sqrt)

def process_performance_metrics(metrics_log, tags):
    base_accumulator = 0
    adjustment_factor = 0.0
    spike_count = 0
    total_length = 0
    
    # Real processing begins
    for entry in metrics_log:
        if len(entry) < 2:
            continue
        direction_change, trend_sum = analyze_pattern(entry)
        if direction_change > 0:
            base_accumulator += trend_sum
            spike_count += direction_change

    # Distractor: string processing with valid logic but indirect relevance
    valid_tags = [t.strip().upper() for t in tags if validate_entry(t)]
    tag_char_count = 0
    for tag in valid_tags:
        tag_char_count += len(tag.replace('X', '').replace('Z', ''))

    # Secondary analysis with partial overlap
    all_values = []    
    for lst in metrics_log:
        all_values.extend(lst)

    risk_level, avg_mag, high_sqrt = compute_risk_factor(all_values)

    # Dead computation branch: uses intermediate values but doesn't contribute
    hypothetical_pairs = list(combinations(all_values[:5], 2)) if len(all_values) >= 5 else [(0, 0)]
    pair_diff_sum = 0
    for a, b in hypothetical_pairs:
        pair_diff_sum += abs(a - b) * 0.1  # minor red herring

    # Core formula
    adjustment_factor = (avg_mag * 0.3) + (high_sqrt * 1.5)
    base_accumulator -= risk_level * 2
    total_length = len(all_values)

    # Final dependent calculation
    final_score = int((base_accumulator + tag_char_count * 1.2) - adjustment_factor)
    
    # Irrelevant transformations
    summary_str = "Metrics processed: {} entries".format(len(metrics_log))
    summary_str.upper().lstrip().replace(' ', '_')  # dead operation
    
    return final_score

# Input data
log_data = [
    [3, 5, 4, 8, 6],
    [2, 1, 4],
    [9, 11, 10, 13, 12, 14]
]
tag_list = ['core', 'alpha', 'betaZ', 'gamma', 'delta']

result = process_performance_metrics(log_data, tag_list)
print(f"Target result: {result}")