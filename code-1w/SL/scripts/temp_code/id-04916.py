from collections import defaultdict, Counter
from itertools import zip_longest

def analyze_transitions(sequence):
    transitions = defaultdict(int)
    for curr, next_val in zip(sequence, sequence[1:]):
        transitions[(curr, next_val)] += 1
    return transitions

def filter_outliers(values, threshold=2):
    count_freq = Counter(values)
    avg_freq = sum(count_freq.values()) / len(count_freq)
    filtered = [v for v, c in count_freq.items() if c >= avg_freq - threshold]
    return filtered if filtered else values

def calculate_final_score(data_list):
    temp_buffer = []
    running_total = 0
    adjustment_factor = 0.5
    
    for item in data_list:
        processed_item = [x * 2 for x in item if x % 2 == 1]  # double odd numbers
        temp_buffer.extend(processed_item)
    
    # Irrelevant statistical tracking (distractor)
    stats_summary = {}
    for idx, val in enumerate(temp_buffer):
        if val not in stats_summary:
            stats_summary[val] = {'first_seen': idx, 'count': 0}
        stats_summary[val]['count'] += 1

    # Dummy loop with no impact on result (distractor)
    cumulative_shift = 0
    for _ in range(3):
        cumulative_shift += len(stats_summary) // (3 - _ + 1)

    # Actual computation path
    valid_entries = [x for x in temp_buffer if x > 10]
    base_sum = sum(valid_entries)
    
    # Simulate correction based on transition patterns (real logic)
    if len(valid_entries) > 1:
        transition_map = analyze_transitions(valid_entries)
        bonus_points = sum(1 for k, v in transition_map.items() if k[0] < k[1] and v >= 1)
        penalty_reduction = len([v for v in transition_map.values() if v == 1]) // 4
        running_total += base_sum + (bonus_points * 3) - penalty_reduction
    else:
        running_total += sum(temp_buffer)

    # Dead code branch (distractor)
    if len(temp_buffer) < 5:
        fallback = sum(x ** 0.5 for x in temp_buffer)
        running_total = int(fallback)

    final_score = int(running_total * adjustment_factor)
    return final_score

# Main execution block
raw_input = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9],
    [10, 11, 12, 13, 14, 15]
]

intermediate_results = []
for row in raw_input:
    shifted = [x + 1 for x in row]
    cleaned = [x for x in shifted if x != 10]  # remove tens
    intermediate_results.append(cleaned)

processed_data = []
for i, seq in enumerate(intermediate_results):
    if i % 2 == 0:
        processed_data.append([x - 1 for x in seq])
    else:
        processed_data.append(seq)

# Additional irrelevant transformation chain (distractor)
data_stats = defaultdict(int)
flat_view = [item for sublist in processed_data for item in sublist]
for num in flat_view:
    data_stats['even' if num % 2 == 0 else 'odd'] += 1

# Real target computation
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")