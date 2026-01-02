from itertools import combinations

def analyze_patterns(sequence):
    # Irrelevant pattern analysis (distractor)
    pair_count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] + sequence[i+1] > 10:
            pair_count += 1

    # Real computation: count descending pairs
    desc_pairs = sum(1 for a, b in zip(sequence, sequence[1:]) if a > b)
    return desc_pairs

def calculate_final_score(data):
    base_score = sum(x ** 0.5 for x in data if x % 2 == 0)
    bonus = 0
    
    # Semi-relevant grouping logic
    grouped = {k: [v for v in data if v // 10 == k] for k in set(d // 10 for d in data)}
    
    # Dead code path - never executed due to condition (distractor)
    temp_result = None
    if len(grouped) > 100:
        temp_result = max(grouped.keys()) * min(grouped.keys())
    
    # Conditional expression with actual impact
    adjustment = 5.5 if any(len(v) >= 3 for v in grouped.values()) else -2.2
    
    # Real bonus logic
    for val in data:
        if val > 20 and val % 4 == 0:
            bonus += val / 4
    
    # Use of set operations - relevant filtering
    unique_bases = set(int(x ** 0.5) for x in data)
    penalty = len(unique_bases.intersection({2, 3, 5, 7}))  # prime single-digit roots

    return base_score + bonus + adjustment - penalty

# Main execution flow
raw_input = [16, 25, 36, 18, 22, 44, 50, 14, 28, 32]

# Preprocessing step with distractors
filtered_data = [x for x in raw_input if x > 15]
sorted_data = sorted(filtered_data, reverse=True)

# Irrelevant combination generation (uses itertools - distractor)
distinct_pairs = list(combinations(sorted_data, 2))
long_pair_chain = sum(1 for a, b in distinct_pairs if a - b > 10)

# Another distraction: counting something unused
shift_register = 0
for val in sorted_data:
    shift_register ^= val << 1

# Actual processing pipeline
processed_data = [x + 1 for x in filtered_data if x % 3 != 0]  # modifies input meaningfully

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")