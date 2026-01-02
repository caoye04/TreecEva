from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    magnitude = 0
    temp_result = []
    
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] + sequence[j] == 7:
                count += 1
                magnitude += abs(i - j)
    
    # Irrelevant transformation (distractor)
    reversed_seq = [x * 2 for x in sequence[::-1]]
    avg_reversed = sum(reversed_seq) / len(reversed_seq) if reversed_seq else 0
    
    return count, magnitude

def compute_aggregate(data, threshold=3):
    raw_pairs, spread = analyze_pattern(data)
    
    # Real computation path
    base_score = raw_pairs * 10
    adjustment = 0
    
    # Conditional logic affecting final result
    if spread > 10:
        adjustment += 5
    elif spread > 5:
        adjustment += 2
    else:
        adjustment -= 1
    
    # Dummy dictionary operations (semi-relevant)
    stats = {
        'max_val': max(data),
        'min_val': min(data),
        'range': max(data) - min(data),
        'ignored_metric': sum(x ** 2 for x in data)
    }
    
    # Simulated noise: unused combination analysis
    triplets = list(combinations(data, 3))
    valid_triplets = [t for t in triplets if sum(t) % 2 == 0]
    complexity_factor = len(valid_triplets) // 10  # Not used but looks important
    
    # Final score calculation
    final_score = base_score + adjustment
    
    # Dead code branch (never executed due to fixed input)
    if False and len(data) > 100:
        fallback = sum(stats.values()) / 1000
        final_score = fallback
    
    return final_score

data_stream = [1, 6, 2, 5, 3, 4]
intermediate_sum = sum(x for x in data_stream if x % 2 == 0)
duplicate_check = {x: data_stream.count(x) for x in set(data_stream)}

# Key execution point
final_score = compute_aggregate(data_stream)
print(f"Result: {final_score}")