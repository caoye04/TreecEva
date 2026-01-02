from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] + sequence[j] == 10:
                count += 1
    return count

def calculate_efficiency(data):
    total_pairs = sum(1 for x in data if x > 0)
    valid_triplets = 0
    temp_result = 0

    # Real computation: count triplets where sum is divisible by 3
    for triplet in combinations(data, 3):
        if sum(triplet) % 3 == 0:
            valid_triplets += 1

    # Distractor: irrelevant lambda and unused transformation
    transform = lambda x: (x ** 2) + 1
    transformed = [transform(x) for x in data]

    # Another distractor loop: computes but doesn't impact final logic
    max_gap = 0
    for i in range(len(transformed) - 1):
        gap = abs(transformed[i] - transformed[i+1])
        if gap > max_gap:
            max_gap = gap

    # Core formula
    efficiency_score = valid_triplets * 3 - len(data)

    # Dead code branch (never executed due to prior logic)
    if False:
        fallback = sum(transformed) / len(transformed)
        efficiency_score = int(fallback)

    return efficiency_score

# Initial dataset
raw_input = [2, 4, 5, 7, 8, 10]

# Irrelevant preprocessing (not used in final calculation)
duplicate_filtered = [x for x in raw_input if x != 5]
sorted_version = sorted(duplicate_filtered, reverse=True)

# Actual processing pipeline
processed_data = raw_input.copy()

# Key analysis step (distraction)
pattern_count = analyze_pattern(processed_data)

# Critical statement
efficiency_score = calculate_efficiency(processed_data)

print(f"Result: {efficiency_score}")