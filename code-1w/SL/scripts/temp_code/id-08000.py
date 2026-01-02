from itertools import combinations

def analyze_transmission_efficiency(data_stream):
    base_threshold = 7
    temp_results = []
    efficiency_map = {}
    
    for i, chunk in enumerate(data_stream):
        chunk_value = sum([b * (2 ** idx) for idx, b in enumerate(reversed(chunk))])
        if chunk_value > base_threshold:
            temp_results.append(chunk_value)
            efficiency_map[i] = chunk_value % 5
    
    # Irrelevant aggregation
    total_pairs = 0
    for pair in combinations(temp_results, 2):
        if (pair[0] + pair[1]) % 3 == 0:
            total_pairs += 1

    return temp_results, efficiency_map


def calculate_entropy(values):
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    entropy = 0
    total = len(values)
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)


def calculate_final_score(data):
    raw_scores = [x % 13 for x in data]
    adjusted_scores = [x + 5 for x in raw_scores if x > 3]
    bonus = len(adjusted_scores) * 2
    penalty = 0
    
    status_flags = {i: (score % 2 == 0) for i, score in enumerate(adjusted_scores)}
    
    for flag in status_flags.values():
        if not flag:
            penalty += 3
    
    # Key computation
    final_score = sum(adjusted_scores) + bonus - penalty
    
    # Dead code - never used
    debug_trace = [f"Step {i}: {v}" for i, v in enumerate(adjusted_scores)]
    
    return final_score

# Main execution
raw_signal = [
    [1, 0, 1],      # 5
    [1, 1, 1],      # 7
    [1, 1, 0, 1],   # 13
    [1, 0, 0, 1],   # 9
    [1, 1, 1, 1],   # 15
    [0, 1, 1]       # 3
]

filtered_data, metadata = analyze_transmission_efficiency(raw_signal)
entropy_metric = calculate_entropy(filtered_data)
processed_data = [x for x in filtered_data if x in metadata.values() or x % 4 == 1]
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")